# aiwf365.site 部署脚本

默认流程：**构建 → 同步 → （可选）nginx reload**。

构建产物 `dist/` 是真正推送到远程的内容；源码、`node_modules`、`.env` 都不会上服务器。

## 一次性准备

```bash
cp .env.example .env
# 编辑 .env，写入 TENCENT_SERVER_HOST=你的服务器 IP
```

`.env` 不会被 rsync 推上去（脚本默认排除）。

## 一键部署

```bash
python3 scripts/deploy/deploy.py
```

脚本会自动：

1. 检测到没有 `node_modules` 时跑 `npm install`
2. 跑 `npm run build` 生成 `dist/`
3. 用 rsync 把 `dist/` 推到服务器目标目录（默认 `/opt/website/aiwf365/aiwf365.site`）

## 可选环境变量

| 变量名 | 默认值 | 说明 |
| --- | --- | --- |
| `TENCENT_SERVER_HOST` | （必填） | 服务器 IP 或域名 |
| `TENCENT_SERVER_USER` | `root` | SSH 用户 |
| `TENCENT_SERVER_PORT` | `22` | SSH 端口 |
| `TENCENT_SSH_KEY` | `~/.ssh/id_rsa` | SSH 私钥路径 |
| `REMOTE_DIR` | `/opt/website/aiwf365/aiwf365.site` | 远端目标目录 |
| `LOCAL_DIR` | `<repo>/dist` | 本地源目录（构建产物） |
| `SKIP_BUILD` | `false` | 设 `true` 跳过 `npm run build` |
| `NGINX_RELOAD` | `false` | 设 `true` 在同步后远程 `nginx -s reload` |
| `DRY_RUN` | `false` | 只打印命令，不实际同步 |
| `DEPLOY_VERBOSE` | `false` | 显示子进程完整命令 |

## 远程 nginx 提示

因为我们用 Vue Router 的 `createWebHistory`（HTML5 History 模式），直接访问 `/project/xxx` 时 nginx 需要 fallback 到 `index.html`：

```nginx
server {
    listen 80;
    server_name aiwf365.site www.aiwf365.site;
    root /opt/website/aiwf365/aiwf365.site;
    index index.html;

    # 静态资源缓存
    location /assets/ {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # SPA fallback：所有不存在的路径都返回 index.html
    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

加完 nginx 配置后：

```bash
NGINX_RELOAD=true python3 scripts/deploy/deploy.py
```

部署 + 自动 reload 一步到位。