# ComfyUI 换脸工作流

> 本地部署 ReActor，一键批量替换视频人脸。隐私敏感场景完全离线。

## 一、环境

- Python 3.10
- ComfyUI 最新版
- ReActor 插件
- insightface 模型（自动下载）

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Gourieff/comfyui-reactor-node
pip install -r comfyui-reactor-node/requirements.txt
```

## 二、关键节点

工作流只有 4 个核心节点：

1. **Load Video** — 读取原始视频
2. **ReActor Fast Face Swap** — 换脸
3. **Video Combine** — 合并
4. **Save Output** — 保存

## 三、参数调优

| 参数 | 推荐值 | 说明 |
| --- | --- | --- |
| Face Detection | retinaface | 精度最高 |
| Face Restorer | codeformer-v0.1 | 兼顾清晰度和自然度 |
| Fidelity Weight | 0.7 | 太高会"塑料感" |
| Codeformer Weight | 0.5 | 平衡修复与原图 |

## 四、批量处理

写一个小脚本，遍历 `input/*.mp4`：

```python
from pathlib import Path
import subprocess

for video in Path("input").glob("*.mp4"):
    subprocess.run([
        "python", "run_reactor.py",
        "--source", "faces/target.jpg",
        "--target", str(video),
        "--output", f"output/{video.stem}.mp4"
    ])
```

## 五、注意事项

- ⚠️ **肖像权**：换脸只用于本人素材或已获授权的素材
- ⚠️ **法律风险**：国内生成式 AI 内容需标识，避免涉及公众人物
- ⚠️ **质量损失**：长视频每 200 帧会损失一次清晰度，建议分段处理

## 六、性能

- M2 Max：4 分钟视频 ≈ 8 分钟
- 4090：4 分钟视频 ≈ 2 分钟

## 七、产出物

- [x] ComfyUI workflow JSON
- [x] 批量处理脚本
- [x] 参数调优对照表

---

**下一步**：把这个流程接到 Stable Diffusion WebUI 的 API，做「视频 → 二次元」风格化迁移。