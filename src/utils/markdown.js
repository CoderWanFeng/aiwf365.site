import MarkdownIt from 'markdown-it'

// 单例 markdown-it 实例
const md = new MarkdownIt({
  html: false, // 安全：禁止内嵌 HTML
  linkify: true, // 自动识别链接
  typographer: true, // 智能引号
  breaks: false, // 不把单个换行变成 <br>，保持可读
})

// 给所有外链自动加 target=_blank，避免站内跳出
const defaultLinkOpen =
  md.renderer.rules.link_open ||
  function (tokens, idx, options, env, self) {
    return self.renderToken(tokens, idx, options)
  }

md.renderer.rules.link_open = function (tokens, idx, options, env, self) {
  const token = tokens[idx]
  const hrefIdx = token.attrIndex('href')
  if (hrefIdx >= 0) {
    const href = token.attrs[hrefIdx][1]
    if (/^https?:\/\//i.test(href)) {
      token.attrSet('target', '_blank')
      token.attrSet('rel', 'noopener noreferrer')
    }
  }
  return defaultLinkOpen(tokens, idx, options, env, self)
}

export function renderMarkdown(source) {
  return md.render(source || '')
}