#!/bin/bash

# aiwf365.site 启动脚本 - Vite 热加载模式

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$SCRIPT_DIR/preview.log"

# Vite 默认端口
DEV_PORT=5173

# 检查并清理过大的旧日志（>5M 或 >7天）
if [ -f "$LOG_FILE" ]; then
    file_size=$(stat -f%z "$LOG_FILE" 2>/dev/null || echo 0)
    file_mtime=$(stat -f%m "$LOG_FILE" 2>/dev/null || echo 0)
    now=$(date +%s)
    size_mb=$((file_size / 1024 / 1024))
    age_days=$(( (now - file_mtime) / 86400 ))

    if [ "$size_mb" -gt 5 ] || [ "$age_days" -gt 7 ]; then
        echo -e "${YELLOW}旧日志清理: ${size_mb}M, ${age_days}天前 -> 删除${NC}"
        rm "$LOG_FILE"
    fi
fi

# 清空旧日志，重新开始记录
> "$LOG_FILE"

# 日志写入函数
log() {
    echo -e "$1"
    echo -e "$1" | sed 's/\x1b\[[0-9;]*m//g' >> "$LOG_FILE"
}

echo -e "${CYAN}========================================${NC}"
echo -e "${CYAN}    启动 aiwf365.site (Vite 热加载)${NC}"
echo -e "${CYAN}========================================${NC}"
echo ""

# 进入项目根目录
PROJECT_DIR="$SCRIPT_DIR/.."
cd "$PROJECT_DIR" || exit 1

# 检查并安装依赖
if [ ! -d "node_modules" ]; then
    log "${YELLOW}首次运行，正在安装依赖...${NC}"
    npm install >> "$LOG_FILE" 2>&1
    log "${GREEN}依赖安装完成！${NC}"
    log ""
fi

# 自动杀掉占用端口的旧进程
if command -v lsof >/dev/null 2>&1; then
  old_pid=$(/usr/sbin/lsof -nP -iTCP:${DEV_PORT} -sTCP:LISTEN -t 2>/dev/null | head -1)
  if [ -n "$old_pid" ]; then
    log "${YELLOW}发现端口 ${DEV_PORT} 被占用（PID $old_pid），自动清理...${NC}"
    kill "$old_pid" 2>/dev/null
    sleep 1
    if /usr/sbin/lsof -nP -iTCP:${DEV_PORT} -sTCP:LISTEN >/dev/null 2>&1; then
      kill -9 "$old_pid" 2>/dev/null
      sleep 1
    fi
  fi
fi

# 启动 Vite dev server（自带 HMR 热加载）
log "${YELLOW}正在启动 Vite dev server...${NC}"
log "${YELLOW}HMR 已启用 - 修改文件后会自动热更新${NC}"
log ""

# 后台启动 dev server
npm run dev >> "$LOG_FILE" 2>&1 &
SERVER_PID=$!

# Ctrl+C 时一起清理
cleanup_server() {
  if kill -0 "$SERVER_PID" 2>/dev/null; then
    kill -TERM "$SERVER_PID" 2>/dev/null
    sleep 1
    kill -KILL "$SERVER_PID" 2>/dev/null
  fi
}
trap cleanup_server INT TERM EXIT

# 轮询端口是否就绪
log "${YELLOW}等待服务器就绪...${NC}"
SERVER_READY=0
for i in $(seq 1 60); do
  if /usr/sbin/lsof -nP -iTCP:${DEV_PORT} -sTCP:LISTEN >/dev/null 2>&1; then
    SERVER_READY=1
    log "${GREEN}✓ Vite dev server 已就绪（${i} 秒）${NC}"
    log ""
    log "${GREEN}网站地址: http://localhost:${DEV_PORT}${NC}"
    log "${YELLOW}按 Ctrl+C 停止服务器${NC}"
    log ""
    log "${CYAN}========================================${NC}"
    log ""
    break
  fi
  if ! kill -0 "$SERVER_PID" 2>/dev/null; then
    log "${RED}✗ Vite dev server 启动失败${NC}"
    log "${YELLOW}preview.log 末尾：${NC}"
    /usr/bin/tail -15 "$LOG_FILE" 2>/dev/null
    exit 1
  fi
  sleep 1
done

if [ "$SERVER_READY" -ne 1 ]; then
  log "${RED}✗ Vite dev server 60 秒内未就绪${NC}"
  kill -KILL "$SERVER_PID" 2>/dev/null
  exit 1
fi

# 让 server 跑前台（Ctrl+C 由 trap 处理）
wait "$SERVER_PID"
