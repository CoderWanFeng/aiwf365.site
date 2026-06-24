/**
 * 项目数据：以后新增项目只需：
 *   1) 在 src/content/projects/<slug>.md 写文章正文
 *   2) 在 PUBLIC_COVERS 放封面图片
 *   3) 在下面数组里加一项
 *
 * 字段说明：
 *   slug        路由段，作为 URL 和 markdown 文件名（不要带空格）
 *   title       卡片标题
 *   summary     卡片副标题（一句话）
 *   cover       封面路径（public 目录下绝对路径，例如 /covers/xxx.jpg）
 *   tags        标签数组，首页用作筛选
 *   date        发布日期 ISO 字符串
 *   featured    是否精选（首页顶部额外突出）
 */

export const projects = [
  {
    slug: 'ai-short-drama',
    title: 'AI 短剧《回声》全流程',
    summary: '从剧本到成片，11 分钟说清楚 AI 短剧的工业化路径',
    cover: '/covers/ai-short-drama.svg',
    tags: ['AI 视频', '短剧', '创作'],
    date: '2026-06-12',
    featured: true,
  },
  {
    slug: 'auto-podcast',
    title: '全自动播客流水线',
    summary: '选题→脚本→TTS→剪辑一条龙，每周一更不加班',
    cover: '/covers/auto-podcast.svg',
    tags: ['自动化', 'TTS', '内容'],
    date: '2026-06-02',
    featured: true,
  },
  {
    slug: 'face-swap-workflow',
    title: 'ComfyUI 换脸工作流',
    summary: '本地部署 ReActor，一键批量替换视频人脸',
    cover: '/covers/face-swap-workflow.svg',
    tags: ['ComfyUI', '视频', '本地部署'],
    date: '2026-05-21',
  },
  {
    slug: 'kb-qa-bot',
    title: '私域知识库问答机器人',
    summary: '把 Notion / 飞书文档喂给大模型，做专属客服',
    cover: '/covers/kb-qa-bot.svg',
    tags: ['RAG', '知识库', '客服'],
    date: '2026-05-10',
  },
  {
    slug: 'ai-cover-artist',
    title: 'AI 封面生成器',
    summary: 'Stable Diffusion + LoRA，统一画风批量出图',
    cover: '/covers/ai-cover-artist.svg',
    tags: ['SD', 'LoRA', '封面'],
    date: '2026-04-29',
  },
  {
    slug: 'wechat-article-bot',
    title: '公众号爆文仿写机器人',
    summary: '抓取爆款 → 风格解构 → 改写 → 一键排版',
    cover: '/covers/wechat-article-bot.svg',
    tags: ['公众号', '改写', '自动化', '教程入门'],
    date: '2026-04-15',
  },
  {
    slug: 'digital-human-live',
    title: '数字人直播搭子',
    summary: 'Wav2Lip + SadTalker 跑通 24h 不掉线的虚拟主播',
    cover: '/covers/digital-human-live.svg',
    tags: ['数字人', '直播', '音视频'],
    date: '2026-04-01',
  },
  {
    slug: 'paper-digest',
    title: '每日论文摘要 Agent',
    summary: 'arXiv 新论文自动爬取、总结、推送到飞书',
    cover: '/covers/paper-digest.svg',
    tags: ['Agent', '研究', '自动化'],
    date: '2026-03-18',
  },
  {
    slug: 'midjourney-ad',
    title: 'MJ 商业广告图 Prompt 库',
    summary: '100 条实战过的产品广告 prompt 拆解',
    cover: '/covers/midjourney-ad.svg',
    tags: ['Midjourney', '广告', 'Prompt'],
    date: '2026-03-04',
  },
  {
    slug: 'audiobook-pipeline',
    title: '电子书 → 有声书流水线',
    summary: '拆书 + TTS + 拼接 + 封面，零成本做一本有声书',
    cover: '/covers/audiobook-pipeline.svg',
    tags: ['TTS', '电子书', '有声书'],
    date: '2026-02-22',
  },
]

// 全部 tag（首页筛选用），按字母排序去重
export const allTags = Array.from(
  new Set(projects.flatMap((p) => p.tags))
).sort((a, b) => a.localeCompare(b, 'zh-Hans-CN'))

export function findProject(slug) {
  return projects.find((p) => p.slug === slug)
}