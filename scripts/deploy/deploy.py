#!/usr/bin/env python3
"""
aiwf365.site 一键部署脚本

默认流程:
  1. 用 rsync 把项目目录同步到远程服务器的目标目录

输出原则（默认安静模式）:
  - 只打印每个阶段做了什么、结果对不对
  - 失败时打印错误末尾
  - 不打印 rsync 文件级进度

环境变量:
  TENCENT_SERVER_HOST    必填，服务器 host (IP 或域名)
  TENCENT_SERVER_USER    可选，默认 root
  TENCENT_SERVER_PORT    可选，默认 22
  TENCENT_SSH_KEY        可选，默认 ~/.ssh/id_rsa
  REMOTE_DIR             可选，默认 /opt/website/aiwf365/aiwf365.site
   LOCAL_DIR              可选，默认 <repo>/dist
  DRY_RUN=true           只打印 rsync 命令不实际执行
  DEPLOY_VERBOSE=true    显示每个子进程的完整命令（调试用）
"""

from __future__ import annotations

import contextlib
import os
import shlex
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

# ---------- 配置 ----------
SCRIPT_DIR = Path(__file__).resolve().parent
# scripts/deploy/deploy.py -> 项目根
REPO_ROOT = SCRIPT_DIR.parent.parent

DEFAULT_LOCAL_DIR = REPO_ROOT / "dist"
DEFAULT_REMOTE_DIR = "/opt/website/aiwf365/aiwf365.site"
DEFAULT_SSH_KEY = Path.home() / ".ssh" / "id_rsa"

# 已经是压缩格式的文件类型，rsync 传输时不再二次压缩
SKIP_COMPRESS_EXTS = ",".join([
    "jpg", "jpeg", "png", "gif", "webp", "svg", "ico",
    "zip", "gz", "tgz", "bz2", "7z", "rar",
    "mp4", "mov", "webm", "mkv", "avi",
    "mp3", "ogg", "flac",
    "woff", "woff2", "ttf", "otf", "eot",
    "pdf",
])

# 调试模式：显示子进程完整命令
VERBOSE = os.environ.get("DEPLOY_VERBOSE", "").lower() in ("1", "true", "yes")

# ---------- 日志 ----------
USE_COLOR = sys.stdout.isatty()
RESET = "\033[0m" if USE_COLOR else ""
RED = "\033[0;31m" if USE_COLOR else ""
GREEN = "\033[0;32m" if USE_COLOR else ""
YELLOW = "\033[1;33m" if USE_COLOR else ""
BLUE = "\033[0;34m" if USE_COLOR else ""
BOLD = "\033[1m" if USE_COLOR else ""

# 脚本启动时间（用于统计总耗时）
SCRIPT_START = time.monotonic()


def _ts() -> str:
    return datetime.now().strftime("%H:%M:%S")


def _elapsed() -> str:
    """脚本启动至今耗时，例如 '12.3s'。"""
    return f"{time.monotonic() - SCRIPT_START:.1f}s"


def log(msg: str) -> None:
    """普通信息，写到 stdout。"""
    print(f"{BLUE}[{_ts()}]{RESET} {msg}")


def ok(msg: str) -> None:
    """成功标记，写到 stdout。"""
    print(f"{GREEN}✓{RESET} {msg}")


def warn(msg: str) -> None:
    """警告（不致命），写到 stderr。"""
    print(f"{YELLOW}⚠{RESET} {msg}", file=sys.stderr)


def err(msg: str) -> None:
    """错误，写到 stderr。"""
    print(f"{RED}✗{RESET} {msg}", file=sys.stderr)


def title(text: str) -> None:
    """脚本级别的总标题。"""
    print()
    print(f"{BOLD}========== {text} =========={RESET}")


def footer(text: str) -> None:
    """脚本级别的总结尾，附带总耗时。"""
    print()
    print(f"{BOLD}========== {text} (总耗时 {_elapsed()}) =========={RESET}")


def header(text: str) -> None:
    """阶段标题。"""
    print(f"{BOLD}── {text} ──{RESET}")


@contextlib.contextmanager
def step(name: str):
    """阶段上下文管理器。失败时不打印"完成"消息。"""
    log(f"开始 {name}...")
    start = time.monotonic()
    failed = False
    try:
        yield
    except BaseException:
        failed = True
        raise
    finally:
        elapsed = time.monotonic() - start
        if not failed:
            ok(f"{name} 完成 ({elapsed:.1f}s)")


def die(msg: str, code: int = 1) -> None:
    err(msg)
    sys.exit(code)


# ---------- 校验 ----------
def require_tools() -> None:
    for tool in ("rsync", "ssh"):
        if shutil.which(tool) is None:
            die(f"未找到 {tool}，请先安装 (brew install {tool})")


def load_config() -> dict:
    host = os.environ.get("TENCENT_SERVER_HOST", "").strip()
    if not host:
        die(
            "缺少环境变量 TENCENT_SERVER_HOST\n"
            "  方式 1: export TENCENT_SERVER_HOST=1.2.3.4\n"
            "  方式 2: 在项目根目录建 .env 文件写入 TENCENT_SERVER_HOST=1.2.3.4"
        )

    cfg = {
        "host": host,
        "user": os.environ.get("TENCENT_SERVER_USER", "root").strip() or "root",
        "port": int(os.environ.get("TENCENT_SERVER_PORT", "22") or "22"),
        "ssh_key": Path(os.environ.get("TENCENT_SSH_KEY", str(DEFAULT_SSH_KEY))).expanduser(),
        "remote_dir": os.environ.get("REMOTE_DIR", DEFAULT_REMOTE_DIR).strip() or DEFAULT_REMOTE_DIR,
        "local_dir": Path(
            os.environ.get("LOCAL_DIR", str(DEFAULT_LOCAL_DIR))
        ).expanduser()
        .resolve(),
        "dry_run": os.environ.get("DRY_RUN", "").lower() in ("1", "true", "yes"),
    }

    if not cfg["ssh_key"].exists():
        die(f"SSH 私钥不存在: {cfg['ssh_key']}")

    if not cfg["local_dir"].is_dir():
        die(f"本地目录不存在: {cfg['local_dir']}")

    return cfg


# ---------- 步骤 ----------
def step_sync(cfg: dict) -> None:
    rsync_cmd = [
        "rsync",
        "-az",
        "--delete",
        f"--skip-compress={SKIP_COMPRESS_EXTS}",
        "--exclude=.git",
        "--exclude=.DS_Store",
        "--exclude=.env",
        "--exclude=node_modules",
        "--exclude=scripts",
        "-e",
        f"ssh -i {shlex.quote(str(cfg['ssh_key']))} -p {cfg['port']} -o StrictHostKeyChecking=accept-new",
        f"{cfg['local_dir']}/",
        f"{cfg['user']}@{cfg['host']}:{cfg['remote_dir']}/",
    ]

    if cfg["dry_run"]:
        log("[DRY_RUN] 跳过实际同步")
        log("将执行: " + " ".join(shlex.quote(c) for c in rsync_cmd))
        return

    run(rsync_cmd, label="rsync 同步")


def step_build() -> None:
    """运行 npm run build，生成 dist/"""
    run(
        ["npm", "run", "build"],
        cwd=REPO_ROOT,
        label="npm run build",
    )


def step_nginx_reload(cfg: dict) -> None:
    """远程执行 nginx -s reload"""
    ssh_cmd = [
        "ssh",
        "-i", str(cfg["ssh_key"]),
        "-p", str(cfg["port"]),
        "-o", "StrictHostKeyChecking=accept-new",
        f"{cfg['user']}@{cfg['host']}",
        "sudo nginx -s reload",
    ]
    run(ssh_cmd, label="nginx reload")


def run(args: list[str], cwd: Path | None = None, label: str = "") -> None:
    """静默执行子命令。成功时静默，失败时 die 并显示 stderr 末尾。

    设置 DEPLOY_VERBOSE=true 可在执行前看到完整命令。
    """
    if VERBOSE:
        log("$ " + " ".join(shlex.quote(c) for c in args))

    result = subprocess.run(
        args,
        cwd=str(cwd) if cwd else None,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    if result.returncode != 0:
        err(f"{label or '命令'} 失败 (exit {result.returncode})")
        err("--- stdout 末尾 ---")
        for line in (result.stdout or "").strip().splitlines()[-15:]:
            err(f"  {line}")
        err("--- stderr 末尾 ---")
        for line in (result.stderr or "").strip().splitlines()[-15:]:
            err(f"  {line}")
        sys.exit(result.returncode)


# ---------- 入口 ----------
def main() -> int:
    title("aiwf365.site 一键部署")
    require_tools()
    cfg = load_config()

    log(f"目标: {cfg['user']}@{cfg['host']}:{cfg['remote_dir']}")
    log(f"本地: {cfg['local_dir']}")

    skip_build = os.environ.get("SKIP_BUILD", "").lower() in ("1", "true", "yes")
    nginx_reload = os.environ.get("NGINX_RELOAD", "").lower() in ("1", "true", "yes")

    steps = []
    if not skip_build:
        steps.append(("构建", "npm run build", step_build))
    steps.append(("同步", "rsync 同步", lambda: step_sync(cfg)))
    if nginx_reload:
        steps.append(("reload", "nginx reload", lambda: step_nginx_reload(cfg)))

    total = len(steps)
    for idx, (name, _, fn) in enumerate(steps, start=1):
        header(f"Step {idx}/{total}  {name}")
        with step(name):
            fn()

    footer("部署完成")
    ok(f"已部署到 {cfg['user']}@{cfg['host']}:{cfg['remote_dir']}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        die("用户中断")
