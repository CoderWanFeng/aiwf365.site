/**
 * 网站配置：个人信息、社交账号、技术栈集中放在这里
 * TODO: 替换下方 email / socials 中的占位符为你自己的真实账号
 */

export const siteConfig = {
  // ===== 个人 =====
  name: '晚枫',
  brandShort: 'aiwf365',
  tagline: '把每一类 AI 项目，拆成可复用的操作手册。',
  bio: '我做 AI 项目——AI 短剧、自动化流水线、知识库、数字人。这里记录我跑通过的每个项目的实操笔记：工具选型、踩坑记录、产出清单。',
  location: '中国',
  workingOn: 'AI 内容生产 + 自动化',

  // ===== 联系 =====
  email: 'hello@aiwf365.site', // TODO: 改为真实邮箱
  wechat: 'aiwf365', // TODO: 改为微信号
  responseTime: '通常 24 小时内回复',

  // ===== 社交账号 =====
  socials: [
    { key: 'gzh', label: '公众号', url: 'https://mp.weixin.qq.com/s/P_o6azd0AwuraLkQQg6t2Q', icon: '公' },
    { key: 'bilibili', label: 'B 站', url: 'https://space.bilibili.com/259649365', icon: 'B' },
    { key: 'zhihu', label: '知乎', url: 'https://www.zhihu.com/people/CoderWanFeng', icon: '知' },
        { key: 'weibo', label: '微博', url: 'https://weibo.com/u/7726957925', icon: '微' },
    { key: 'douyin', label: '抖音', url: 'https://www.douyin.com/user/self?from_tab_name=main&showSubTab=compilation&showTab=favorite_collection', icon: '抖' },
    { key: 'red', label: '小红书', url: 'https://www.xiaohongshu.com/user/profile/611dcb820000000001014aca', icon: '红' },
    { key: 'github', label: 'GitHub', url: 'https://github.com/CoderWanFeng/aiwf365.site', icon: 'G' },
    { key: 'twitter', label: 'X', url: 'https://x.com/CoderWanFeng', icon: 'X' },
    { key: 'YouTube', label: 'YouTube', url: 'https://www.youtube.com/@CoderWanFeng', icon: 'Y' },
  ],

  // ===== 工具栈（用于 About 页）=====
  stack: [
    { group: '大模型', items: ['Claude', 'GPT-4o', 'Gemini', '通义千问'] },
    { group: '图像', items: ['Midjourney', 'Stable Diffusion', 'ComfyUI', 'IPAdapter'] },
    { group: '视频', items: ['可灵 Kling', 'Runway', 'Sora', 'Pika'] },
    { group: '语音', items: ['GPT-SoVITS', 'ChatTTS', 'Suno', 'ElevenLabs'] },
    { group: '开发', items: ['Python', 'Node.js', 'Vue', 'Vite', 'n8n'] },
  ],
}