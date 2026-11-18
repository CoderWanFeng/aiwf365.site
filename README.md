# aiwf365.site

> 🌐 **线上地址**：<https://aiwf365.site/>
> ⚠️ **现状**：域名已解析到腾讯云 EdgeOne、http 会 301 跳转 https，但 https 握手当前失败（打不开），需检查 EdgeOne 的 https 证书 / 回源配置后再确认可达。

「晚枫 365」站点，Vue 3 + Vite 构建。

## 部署

- 线上地址：<https://aiwf365.site/>（独立域名 vhost，非 python-office.com 子路径）
- 部署脚本：`scripts/deploy/deploy.py`，用 rsync 把构建产物（`dist/`）同步到服务器 `/opt/website/aiwf365/aiwf365.site/`。
- 环境变量：`REMOTE_DIR`（默认 `/opt/website/aiwf365/aiwf365.site`）、`DRY_RUN=true` 仅打印命令。

## 本地开发

```bash
npm install
npm run dev      # 本地预览
npm run build    # 构建到 dist/
```
