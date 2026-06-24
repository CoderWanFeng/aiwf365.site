<template>
  <div class="contact">
    <section class="contact-hero">
      <div class="contact-hero__inner">
        <h1 class="contact-hero__title">想聊点什么？</h1>
        <p class="contact-hero__sub">
          合作、提问、单纯交个朋友——都行。我{{ siteConfig.responseTime }}。
        </p>
      </div>
    </section>

    <!-- 主邮箱 -->
    <section class="contact-block">
      <div class="contact-block__inner">
        <a :href="`mailto:${siteConfig.email}`" class="email-card">
          <div class="email-card__icon">✉</div>
          <div class="email-card__body">
            <span class="email-card__label">写邮件给我</span>
            <strong class="email-card__addr">{{ siteConfig.email }}</strong>
            <span class="email-card__hint">点击直接打开邮件客户端</span>
          </div>
          <span class="email-card__arrow">→</span>
        </a>
      </div>
    </section>

    <!-- 社交账号 -->
    <section class="contact-block">
      <div class="contact-block__inner">
        <h2 class="contact-block__title">也可以在这里找我</h2>
        <div class="social-grid">
          <a
            v-for="s in siteConfig.socials"
            :key="s.key"
            :href="s.url"
            target="_blank"
            rel="noopener noreferrer"
            class="social-card"
          >
            <span class="social-card__icon">{{ s.icon }}</span>
            <span class="social-card__label">{{ s.label }}</span>
            <span class="social-card__arrow">↗</span>
          </a>
        </div>
      </div>
    </section>

    <!-- 微信 -->
    <section v-if="siteConfig.wechat" class="contact-block">
      <div class="contact-block__inner">
        <h2 class="contact-block__title">微信</h2>
        <div class="wechat-card">
          <div class="wechat-card__qr" aria-hidden="true">
            <!-- 占位 QR 区，用 SVG 画个方块示意，之后可换成真实二维码图片 -->
            <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
              <rect width="100" height="100" fill="#fff" stroke="#1a1a1a" stroke-width="4"/>
              <g fill="#1a1a1a">
                <rect x="10" y="10" width="20" height="20"/>
                <rect x="14" y="14" width="12" height="12" fill="#fff"/>
                <rect x="18" y="18" width="4" height="4"/>
                <rect x="70" y="10" width="20" height="20"/>
                <rect x="74" y="14" width="12" height="12" fill="#fff"/>
                <rect x="78" y="18" width="4" height="4"/>
                <rect x="10" y="70" width="20" height="20"/>
                <rect x="14" y="74" width="12" height="12" fill="#fff"/>
                <rect x="18" y="78" width="4" height="4"/>
                <rect x="38" y="14" width="4" height="4"/>
                <rect x="46" y="14" width="4" height="4"/>
                <rect x="38" y="22" width="4" height="4"/>
                <rect x="54" y="22" width="4" height="4"/>
                <rect x="38" y="38" width="4" height="4"/>
                <rect x="46" y="38" width="4" height="4"/>
                <rect x="54" y="38" width="4" height="4"/>
                <rect x="62" y="38" width="4" height="4"/>
                <rect x="38" y="46" width="4" height="4"/>
                <rect x="54" y="46" width="4" height="4"/>
                <rect x="62" y="46" width="4" height="4"/>
                <rect x="46" y="54" width="4" height="4"/>
                <rect x="54" y="54" width="4" height="4"/>
                <rect x="70" y="54" width="4" height="4"/>
                <rect x="78" y="54" width="4" height="4"/>
                <rect x="38" y="62" width="4" height="4"/>
                <rect x="46" y="62" width="4" height="4"/>
                <rect x="62" y="62" width="4" height="4"/>
                <rect x="70" y="62" width="4" height="4"/>
                <rect x="78" y="62" width="4" height="4"/>
                <rect x="38" y="70" width="4" height="4"/>
                <rect x="54" y="70" width="4" height="4"/>
                <rect x="62" y="70" width="4" height="4"/>
                <rect x="78" y="70" width="4" height="4"/>
                <rect x="46" y="78" width="4" height="4"/>
                <rect x="54" y="78" width="4" height="4"/>
                <rect x="70" y="78" width="4" height="4"/>
                <rect x="78" y="78" width="4" height="4"/>
              </g>
            </svg>
          </div>
          <div class="wechat-card__body">
            <div class="wechat-card__label">微信号</div>
            <div class="wechat-card__id">{{ siteConfig.wechat }}</div>
            <div class="wechat-card__tip">
              加我微信请备注「aiwf365」，不然可能不会通过。
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="contact-block contact-faq">
      <div class="contact-block__inner">
        <h2 class="contact-block__title">常被问到的</h2>
        <dl class="faq">
          <div class="faq__item">
            <dt>可以接外包/合作吗？</dt>
            <dd>看具体需求。如果是 AI 内容生产、自动化、ComfyUI 工作流方向，发邮件聊聊。</dd>
          </div>
          <div class="faq__item">
            <dt>项目里的素材能商用吗？</dt>
            <dd>工具与工作流可以；具体素材（视频、封面等）大多需要你替换为自己的源素材。</dd>
          </div>
          <div class="faq__item">
            <dt>想成为你徒弟/学员？</dt>
            <dd>暂时不开课。建议先把博客里的项目挨个跑一遍再说。</dd>
          </div>
        </dl>
      </div>
    </section>
  </div>
</template>

<script setup>
import { siteConfig } from '../data/site.js'
</script>

<style scoped>
.contact {
  width: 100%;
}

/* Hero */
.contact-hero {
  background: linear-gradient(135deg, #fff 0%, #fff1ea 100%);
  border-bottom: 1px solid var(--border);
}
.contact-hero__inner {
  max-width: 760px;
  margin: 0 auto;
  padding: 80px 20px 56px;
  text-align: center;
}
.contact-hero__title {
  font-size: 40px;
  font-weight: 800;
  margin: 0 0 14px;
  letter-spacing: -0.5px;
}
.contact-hero__sub {
  font-size: 16px;
  color: var(--text-soft);
  margin: 0;
  line-height: 1.7;
}

/* Blocks */
.contact-block {
  border-bottom: 1px solid var(--border);
}
.contact-block__inner {
  max-width: 760px;
  margin: 0 auto;
  padding: 40px 20px;
}
.contact-block__title {
  font-size: 20px;
  font-weight: 800;
  margin: 0 0 20px;
  border-left: 4px solid var(--accent);
  padding-left: 12px;
}

/* Email */
.email-card {
  display: flex;
  align-items: center;
  gap: 18px;
  background: var(--bg-elev);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 20px 24px;
  transition: all 0.18s ease;
}
.email-card:hover {
  border-color: var(--accent);
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}
.email-card__icon {
  width: 56px;
  height: 56px;
  border-radius: 16px;
  background: var(--accent-soft);
  color: var(--accent);
  font-size: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.email-card__body {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 2px;
  min-width: 0;
}
.email-card__label {
  font-size: 12px;
  color: var(--text-muted);
}
.email-card__addr {
  font-size: 18px;
  font-weight: 700;
  color: var(--text);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.email-card__hint {
  font-size: 12px;
  color: var(--text-muted);
}
.email-card__arrow {
  font-size: 22px;
  color: var(--text-muted);
  transition: transform 0.18s ease;
}
.email-card:hover .email-card__arrow {
  color: var(--accent);
  transform: translateX(4px);
}

/* Socials */
.social-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 12px;
}
.social-card {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 16px;
  background: var(--bg-elev);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  transition: all 0.15s ease;
}
.social-card:hover {
  border-color: var(--accent);
  transform: translateY(-1px);
}
.social-card__icon {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  background: linear-gradient(135deg, var(--accent), #ec4899);
  color: #fff;
  font-weight: 800;
  font-size: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.social-card__label {
  font-weight: 600;
  font-size: 14px;
  flex: 1;
}
.social-card__arrow {
  font-size: 14px;
  color: var(--text-muted);
  transition: transform 0.15s ease;
}
.social-card:hover .social-card__arrow {
  color: var(--accent);
  transform: translate(2px, -2px);
}

/* Wechat */
.wechat-card {
  display: flex;
  gap: 20px;
  align-items: center;
  background: var(--bg-elev);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 20px;
}
.wechat-card__qr {
  width: 120px;
  height: 120px;
  flex-shrink: 0;
  background: #fff;
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 6px;
}
.wechat-card__qr svg {
  width: 100%;
  height: 100%;
  display: block;
}
.wechat-card__body {
  flex: 1;
}
.wechat-card__label {
  font-size: 12px;
  color: var(--text-muted);
}
.wechat-card__id {
  font-size: 22px;
  font-weight: 800;
  letter-spacing: 1px;
  margin: 4px 0 8px;
  font-family: ui-monospace, monospace;
}
.wechat-card__tip {
  font-size: 13px;
  color: var(--text-soft);
  line-height: 1.6;
}

/* FAQ */
.faq {
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 14px;
}
.faq__item {
  background: var(--bg-elev);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 14px 18px;
}
.faq__item dt {
  font-weight: 700;
  margin: 0 0 6px;
  color: var(--text);
}
.faq__item dd {
  margin: 0;
  color: var(--text-soft);
  font-size: 14px;
  line-height: 1.7;
}

@media (max-width: 640px) {
  .contact-hero__inner {
    padding: 56px 16px 40px;
  }
  .contact-hero__title {
    font-size: 28px;
  }
  .email-card {
    flex-wrap: wrap;
    padding: 16px;
  }
  .email-card__addr {
    font-size: 16px;
  }
  .wechat-card {
    flex-direction: column;
    text-align: center;
  }
}
</style>