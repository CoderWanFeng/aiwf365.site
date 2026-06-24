<template>
  <div class="about">
    <!-- Hero -->
    <section class="about-hero">
      <div class="about-hero__inner">
        <div class="about-hero__avatar" aria-hidden="true">{{ siteConfig.name.charAt(0) }}</div>
        <h1 class="about-hero__title">你好，我是 {{ siteConfig.name }}</h1>
        <p class="about-hero__bio">{{ siteConfig.bio }}</p>
        <div class="about-hero__meta">
          <span v-if="siteConfig.location">📍 {{ siteConfig.location }}</span>
          <span v-if="siteConfig.workingOn">🛠 {{ siteConfig.workingOn }}</span>
        </div>
      </div>
    </section>

    <!-- 一句话定位 -->
    <section class="about-block">
      <div class="about-block__inner">
        <p class="about-tagline">
          每一篇都跑通了再写。<br />
          不是教程，是「我自己做过的笔记」。
        </p>
      </div>
    </section>

    <!-- 工具栈 -->
    <section class="about-block">
      <div class="about-block__inner">
        <h2 class="about-block__title">我常用的工具</h2>
        <div class="stack-grid">
          <div v-for="g in siteConfig.stack" :key="g.group" class="stack-card">
            <h3 class="stack-card__group">{{ g.group }}</h3>
            <div class="stack-card__items">
              <span v-for="item in g.items" :key="item" class="stack-chip">
                {{ item }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 项目时间线 -->
    <section class="about-block">
      <div class="about-block__inner">
        <h2 class="about-block__title">最近的项目</h2>
        <ol class="timeline">
          <li v-for="p in latestProjects" :key="p.slug" class="timeline__item">
            <span class="timeline__date">{{ formatDate(p.date) }}</span>
            <router-link :to="`/project/${p.slug}`" class="timeline__link">
              {{ p.title }}
            </router-link>
            <span class="timeline__summary">{{ p.summary }}</span>
          </li>
        </ol>
        <p class="about-block__more">
          <router-link to="/">查看全部项目 →</router-link>
        </p>
      </div>
    </section>

    <!-- CTA -->
    <section class="about-cta">
      <div class="about-cta__inner">
        <h2>想一起做点什么？</h2>
        <p>聊项目、提需求、单纯交个朋友都行。</p>
        <router-link to="/contact" class="about-cta__btn">联系我</router-link>
      </div>
    </section>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { siteConfig } from '../data/site.js'
import { projects } from '../data/projects.js'

const latestProjects = computed(() =>
  [...projects]
    .sort((a, b) => (a.date > b.date ? -1 : 1))
    .slice(0, 5)
)

function formatDate(iso) {
  if (!iso) return ''
  const d = new Date(iso)
  return `${d.getFullYear()}.${String(d.getMonth() + 1).padStart(2, '0')}`
}
</script>

<style scoped>
.about {
  width: 100%;
}

/* Hero */
.about-hero {
  background: linear-gradient(135deg, #fff 0%, #fff1ea 100%);
  border-bottom: 1px solid var(--border);
}
.about-hero__inner {
  max-width: 760px;
  margin: 0 auto;
  padding: 72px 20px 56px;
  text-align: center;
}
.about-hero__avatar {
  width: 84px;
  height: 84px;
  border-radius: 50%;
  margin: 0 auto 18px;
  background: linear-gradient(135deg, var(--accent), #ec4899);
  color: #fff;
  font-size: 36px;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 8px 24px rgba(255, 90, 31, 0.25);
}
.about-hero__title {
  font-size: 32px;
  font-weight: 800;
  margin: 0 0 14px;
  letter-spacing: -0.5px;
}
.about-hero__bio {
  font-size: 16px;
  color: var(--text-soft);
  line-height: 1.8;
  margin: 0 auto 18px;
  max-width: 580px;
}
.about-hero__meta {
  display: inline-flex;
  gap: 18px;
  font-size: 13px;
  color: var(--text-muted);
  flex-wrap: wrap;
  justify-content: center;
}

/* 通用 block */
.about-block {
  border-bottom: 1px solid var(--border);
}
.about-block__inner {
  max-width: 760px;
  margin: 0 auto;
  padding: 48px 20px;
}
.about-block__title {
  font-size: 22px;
  font-weight: 800;
  margin: 0 0 20px;
  border-left: 4px solid var(--accent);
  padding-left: 12px;
}
.about-block__more {
  margin: 20px 0 0;
  text-align: right;
}
.about-block__more a {
  color: var(--accent);
  font-size: 14px;
  font-weight: 500;
}
.about-block__more a:hover {
  text-decoration: underline;
}

/* Tagline */
.about-tagline {
  font-size: 22px;
  font-weight: 700;
  line-height: 1.6;
  margin: 0;
  text-align: center;
  color: var(--text);
}

/* Stack */
.stack-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 16px;
}
.stack-card {
  background: var(--bg-elev);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 16px 18px;
}
.stack-card__group {
  font-size: 13px;
  font-weight: 700;
  color: var(--accent);
  margin: 0 0 10px;
  letter-spacing: 0.5px;
}
.stack-card__items {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}
.stack-chip {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 999px;
  padding: 4px 10px;
  font-size: 12px;
  color: var(--text-soft);
}

/* Timeline */
.timeline {
  list-style: none;
  margin: 0;
  padding: 0;
}
.timeline__item {
  display: grid;
  grid-template-columns: 90px 1fr;
  gap: 8px 16px;
  padding: 14px 0;
  border-bottom: 1px dashed var(--border);
  align-items: baseline;
}
.timeline__item:last-child {
  border-bottom: none;
}
.timeline__date {
  font-size: 12px;
  color: var(--text-muted);
  font-variant-numeric: tabular-nums;
}
.timeline__link {
  font-weight: 700;
  font-size: 15px;
  color: var(--text);
  grid-column: 2;
  transition: color 0.15s ease;
}
.timeline__link:hover {
  color: var(--accent);
}
.timeline__summary {
  grid-column: 2;
  font-size: 13px;
  color: var(--text-muted);
  margin-top: 2px;
}

/* CTA */
.about-cta {
  background: var(--accent-soft);
}
.about-cta__inner {
  max-width: 760px;
  margin: 0 auto;
  padding: 56px 20px;
  text-align: center;
}
.about-cta h2 {
  font-size: 24px;
  margin: 0 0 8px;
  font-weight: 800;
}
.about-cta p {
  color: var(--text-soft);
  margin: 0 0 20px;
}
.about-cta__btn {
  display: inline-block;
  background: var(--accent);
  color: #fff;
  padding: 10px 26px;
  border-radius: 999px;
  font-size: 14px;
  font-weight: 600;
  transition: opacity 0.15s ease, transform 0.15s ease;
}
.about-cta__btn:hover {
  opacity: 0.92;
  transform: translateY(-1px);
}

@media (max-width: 640px) {
  .about-hero__inner {
    padding: 48px 16px 40px;
  }
  .about-hero__title {
    font-size: 24px;
  }
  .about-block__inner {
    padding: 36px 16px;
  }
  .timeline__item {
    grid-template-columns: 1fr;
  }
  .timeline__link,
  .timeline__summary {
    grid-column: 1;
  }
}
</style>