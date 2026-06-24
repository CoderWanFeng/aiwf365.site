<template>
  <div class="home">
    <!-- Hero -->
    <section class="hero">
      <div class="hero__inner">
        <h1 class="hero__title">把每一类 AI 项目，<br />拆成可复用的操作手册。</h1>
        <p class="hero__subtitle">
          这里收录我做过的 {{ projects.length }} 个 AI 主题项目——
          AI 短剧、自动化流水线、数字人、知识库……点开任意卡片即可看到完整实现步骤。
        </p>
        <div class="hero__stats">
          <div class="hero__stat">
            <strong>{{ projects.length }}</strong>
            <span>个项目</span>
          </div>
          <div class="hero__stat">
            <strong>{{ allTags.length }}</strong>
            <span>个分类</span>
          </div>
          <div class="hero__stat">
            <strong>100%</strong>
            <span>亲手跑过</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 筛选 -->
    <section class="filters">
      <div class="filters__inner">
        <button
          class="filters__chip"
          :class="{ 'is-active': activeTag === '' }"
          @click="activeTag = ''"
        >
          全部
        </button>
        <button
          v-for="t in allTags"
          :key="t"
          class="filters__chip"
          :class="{ 'is-active': activeTag === t }"
          @click="activeTag = t"
        >
          {{ t }}
        </button>
      </div>
    </section>

    <!-- 当前过滤摘要 -->
    <section v-if="hasFilter" class="filter-summary">
      <div class="filter-summary__inner">
        <span class="filter-summary__text">
          匹配到 <strong>{{ filtered.length }}</strong> 个项目
          <template v-if="searchQuery">
            · 搜索词：<em>"{{ searchQuery }}"</em>
          </template>
          <template v-if="activeTag">
            · 分类：<em>{{ activeTag }}</em>
          </template>
        </span>
        <button class="filter-summary__reset" @click="resetFilters">清空筛选</button>
      </div>
    </section>

    <!-- 卡片网格 -->
    <section class="grid">
      <div class="grid__inner">
        <ProjectCard
          v-for="p in filtered"
          :key="p.slug"
          :project="p"
        />
        <div v-if="filtered.length === 0" class="grid__empty">
          <p>没找到匹配的项目</p>
          <button class="grid__empty-btn" @click="resetFilters">清空筛选条件</button>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'
import ProjectCard from '../components/ProjectCard.vue'
import { projects, allTags } from '../data/projects.js'
import { searchQuery } from '../stores/search.js'

const activeTag = ref('')

function matchesSearch(p, q) {
  if (!q) return true
  const needle = q.toLowerCase().trim()
  if (!needle) return true
  return (
    p.title.toLowerCase().includes(needle) ||
    p.summary.toLowerCase().includes(needle) ||
    p.tags.some((t) => t.toLowerCase().includes(needle))
  )
}

const filteredAll = computed(() => projects)

const filtered = computed(() => {
  return projects.filter((p) => {
    if (activeTag.value && !p.tags.includes(activeTag.value)) return false
    if (!matchesSearch(p, searchQuery.value)) return false
    return true
  })
})

const hasFilter = computed(
  () => Boolean(searchQuery.value) || Boolean(activeTag.value)
)

function resetFilters() {
  activeTag.value = ''
  searchQuery.value = ''
}
</script>

<style scoped>
.home {
  width: 100%;
}

/* Hero */
.hero {
  background: linear-gradient(135deg, #fff 0%, #fff1ea 100%);
  border-bottom: 1px solid var(--border);
}
.hero__inner {
  max-width: 1180px;
  margin: 0 auto;
  padding: 64px 20px 48px;
}
.hero__title {
  font-size: 36px;
  font-weight: 800;
  line-height: 1.25;
  letter-spacing: -0.5px;
  margin: 0 0 16px;
  color: var(--text);
}
.hero__subtitle {
  font-size: 16px;
  color: var(--text-soft);
  max-width: 640px;
  margin: 0 0 28px;
  line-height: 1.7;
}
.hero__stats {
  display: flex;
  gap: 28px;
  flex-wrap: wrap;
}
.hero__stat {
  display: flex;
  align-items: baseline;
  gap: 6px;
}
.hero__stat strong {
  font-size: 24px;
  font-weight: 800;
  color: var(--accent);
}
.hero__stat span {
  font-size: 13px;
  color: var(--text-muted);
}

/* Filters */
.filters {
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 60px;
  z-index: 10;
}
.filters__inner {
  max-width: 1180px;
  margin: 0 auto;
  padding: 14px 20px;
  display: flex;
  gap: 8px;
  overflow-x: auto;
  scrollbar-width: none;
}
.filters__inner::-webkit-scrollbar {
  display: none;
}
.filters__chip {
  flex-shrink: 0;
  border: 1px solid var(--border);
  background: var(--bg-elev);
  padding: 6px 14px;
  border-radius: 999px;
  font-size: 13px;
  color: var(--text-soft);
  transition: all 0.15s ease;
}
.filters__chip:hover {
  color: var(--accent);
  border-color: var(--accent);
}
.filters__chip.is-active {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
}

/* Filter summary */
.filter-summary {
  background: var(--accent-soft);
  border-bottom: 1px solid var(--border);
}
.filter-summary__inner {
  max-width: 1180px;
  margin: 0 auto;
  padding: 10px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  font-size: 13px;
  color: var(--text-soft);
}
.filter-summary__text strong {
  color: var(--accent);
  font-weight: 700;
}
.filter-summary__text em {
  font-style: normal;
  background: #fff;
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 1px 6px;
  color: var(--text);
}
.filter-summary__reset {
  border: none;
  background: transparent;
  color: var(--accent);
  font-size: 13px;
  font-weight: 500;
}
.filter-summary__reset:hover {
  text-decoration: underline;
}

/* Grid */
.grid {
  background: var(--bg);
}
.grid__inner {
  max-width: 1180px;
  margin: 0 auto;
  padding: 32px 20px 48px;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 20px;
}
.grid__empty {
  grid-column: 1 / -1;
  padding: 80px 20px;
  text-align: center;
  color: var(--text-muted);
}
.grid__empty p {
  font-size: 15px;
  margin: 0 0 14px;
}
.grid__empty-btn {
  border: 1px solid var(--accent);
  background: transparent;
  color: var(--accent);
  padding: 6px 16px;
  border-radius: 999px;
  font-size: 13px;
}
.grid__empty-btn:hover {
  background: var(--accent);
  color: #fff;
}

@media (max-width: 640px) {
  .hero__title {
    font-size: 26px;
  }
  .hero__subtitle {
    font-size: 14px;
  }
  .hero__inner {
    padding: 40px 16px 32px;
  }
  .filters {
    top: 56px;
  }
}
</style>