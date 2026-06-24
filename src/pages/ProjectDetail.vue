<template>
  <article v-if="project" class="detail">
    <!-- Cover header -->
    <div class="detail__cover">
      <img :src="project.cover" :alt="project.title" />
      <div class="detail__cover-mask" />
      <div class="detail__cover-inner">
        <div class="detail__tags">
          <span v-for="t in project.tags" :key="t" class="detail__tag">{{ t }}</span>
        </div>
        <h1 class="detail__title">{{ project.title }}</h1>
        <p class="detail__summary">{{ project.summary }}</p>
        <div class="detail__meta">
          <span>📅 {{ formatDate(project.date) }}</span>
          <button class="detail__back" @click="goBack">← 返回橱窗</button>
        </div>
      </div>
    </div>

    <!-- Markdown body -->
    <div class="prose" v-html="html" />

    <div class="detail__footer">
      <router-link to="/" class="detail__back-link">← 回到项目橱窗</router-link>
    </div>
  </article>

  <div v-else class="detail__missing">
    <h2>找不到这个项目</h2>
    <p>可能链接已失效，或者 slug 拼错了。</p>
    <router-link to="/" class="detail__back-link">← 回到项目橱窗</router-link>
  </div>
</template>

<script setup>
import { computed, onMounted, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { findProject } from '../data/projects.js'
import { renderMarkdown } from '../utils/markdown.js'

const route = useRoute()
const router = useRouter()
const slug = computed(() => route.params.slug)
const project = computed(() => findProject(slug.value))

// Vite 的 import.meta.glob：构建时把所有 markdown 文件打包成模块
const articles = import.meta.glob('../content/projects/*.md', {
  query: '?raw',
  import: 'default',
})

const html = ref('')

async function loadArticle(slugVal) {
  const path = `../content/projects/${slugVal}.md`
  const loader = articles[path]
  if (!loader) {
    html.value = '<p>该项目的文章还没写好，敬请期待。</p>'
    return
  }
  const mod = await loader()
  html.value = renderMarkdown(mod)
}

onMounted(() => loadArticle(slug.value))
watch(slug, (v) => loadArticle(v))

function formatDate(iso) {
  if (!iso) return ''
  const d = new Date(iso)
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(
    d.getDate()
  ).padStart(2, '0')}`
}

function goBack() {
  if (window.history.length > 1) router.back()
  else router.push('/')
}
</script>

<style scoped>
.detail {
  width: 100%;
}

.detail__cover {
  position: relative;
  width: 100%;
  aspect-ratio: 21 / 9;
  max-height: 420px;
  overflow: hidden;
  background: #1f2937;
}
.detail__cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: brightness(0.55) saturate(1.05);
}
.detail__cover-mask {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0.05) 0%,
    rgba(0, 0, 0, 0.55) 100%
  );
}
.detail__cover-inner {
  position: absolute;
  inset: 0;
  padding: 0 24px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding-bottom: 32px;
  max-width: 900px;
  margin: 0 auto;
  color: #fff;
}
.detail__tags {
  display: flex;
  gap: 8px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}
.detail__tag {
  background: rgba(255, 255, 255, 0.18);
  border: 1px solid rgba(255, 255, 255, 0.35);
  backdrop-filter: blur(4px);
  color: #fff;
  font-size: 12px;
  padding: 3px 10px;
  border-radius: 999px;
}
.detail__title {
  font-size: 32px;
  font-weight: 800;
  margin: 0 0 8px;
  letter-spacing: -0.5px;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}
.detail__summary {
  font-size: 15px;
  margin: 0 0 16px;
  opacity: 0.92;
  max-width: 640px;
  text-shadow: 0 1px 4px rgba(0, 0, 0, 0.3);
}
.detail__meta {
  display: flex;
  align-items: center;
  gap: 16px;
  font-size: 13px;
  opacity: 0.9;
}
.detail__back {
  background: rgba(255, 255, 255, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.4);
  color: #fff;
  padding: 4px 12px;
  border-radius: 999px;
  font-size: 12px;
  transition: background 0.15s ease;
}
.detail__back:hover {
  background: rgba(255, 255, 255, 0.32);
}

.detail__footer {
  max-width: 760px;
  margin: 24px auto 0;
  padding: 0 20px;
}
.detail__back-link {
  display: inline-block;
  color: var(--accent);
  font-size: 14px;
  font-weight: 500;
  border: 1px solid var(--accent);
  padding: 6px 14px;
  border-radius: 999px;
  transition: all 0.15s ease;
}
.detail__back-link:hover {
  background: var(--accent);
  color: #fff;
}

.detail__missing {
  max-width: 600px;
  margin: 80px auto;
  text-align: center;
  padding: 0 20px;
}
.detail__missing h2 {
  font-size: 24px;
  margin-bottom: 8px;
}
.detail__missing p {
  color: var(--text-muted);
  margin-bottom: 24px;
}

@media (max-width: 640px) {
  .detail__cover {
    aspect-ratio: 4 / 3;
  }
  .detail__title {
    font-size: 24px;
  }
  .detail__summary {
    font-size: 14px;
  }
}
</style>