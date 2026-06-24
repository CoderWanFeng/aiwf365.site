<template>
  <header class="site-header">
    <div class="site-header__inner">
      <router-link to="/" class="site-header__brand" @click="clearSearch">
        <span class="site-header__logo">🌿</span>
        <div class="site-header__brand-text">
          <strong>晚枫 AI 项目集</strong>
          <span>aiwf365.site</span>
        </div>
      </router-link>

      <form class="site-search" role="search" @submit.prevent>
        <span class="site-search__icon" aria-hidden="true">🔍</span>
        <input
          ref="inputRef"
          v-model="searchQuery"
          type="search"
          class="site-search__input"
          placeholder="搜项目：AI 短剧、知识库、ComfyUI …"
          aria-label="搜索项目"
          enterkeyhint="search"
          @keydown.esc="searchQuery = ''"
        />
        <button
          v-if="searchQuery"
          type="button"
          class="site-search__clear"
          aria-label="清空搜索"
          @click="searchQuery = ''"
        >
          ✕
        </button>
        <kbd v-else class="site-search__hint" aria-hidden="true">/</kbd>
      </form>

      <nav class="site-header__nav">
        <router-link to="/" exact-active-class="is-active">项目</router-link>
        <router-link to="/tutorials" active-class="is-active">教程</router-link>
        <router-link to="/about" active-class="is-active">关于</router-link>
        <router-link to="/contact" active-class="is-active">联系</router-link>
      </nav>

      <a
        v-if="primarySocial"
        :href="primarySocial.url"
        target="_blank"
        rel="noopener"
        class="site-header__github"
        :aria-label="primarySocial.label"
      >
        <svg
          class="site-header__github-icon"
          viewBox="0 0 24 24"
          width="16"
          height="16"
          fill="currentColor"
          aria-hidden="true"
        >
          <path
            d="M12 .5C5.73.5.67 5.56.67 11.84c0 4.99 3.23 9.21 7.72 10.71.56.1.77-.24.77-.54 0-.27-.01-1-.01-1.95-3.14.68-3.8-1.51-3.8-1.51-.51-1.3-1.25-1.65-1.25-1.65-1.02-.7.08-.69.08-.69 1.13.08 1.72 1.16 1.72 1.16 1 1.72 2.63 1.22 3.27.94.1-.72.39-1.22.71-1.5-2.51-.28-5.16-1.25-5.16-5.58 0-1.23.44-2.24 1.16-3.03-.12-.29-.5-1.44.11-3 0 0 .95-.3 3.11 1.16.9-.25 1.87-.38 2.83-.38s1.93.13 2.83.38c2.16-1.46 3.11-1.16 3.11-1.16.61 1.56.23 2.71.11 3 .72.79 1.16 1.8 1.16 3.03 0 4.34-2.66 5.3-5.18 5.58.4.35.76 1.04.76 2.1 0 1.52-.01 2.74-.01 3.11 0 .3.21.65.78.54 4.49-1.5 7.71-5.72 7.71-10.71C23.33 5.56 18.27.5 12 .5z"
          />
        </svg>
        <span class="site-header__github-label">View on GitHub</span>
      </a>
    </div>
  </header>
</template>

<script setup>
import { onMounted, onBeforeUnmount, ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import { searchQuery } from '../stores/search.js'
import { siteConfig } from '../data/site.js'

const route = useRoute()
const inputRef = ref(null)

// 优先展示 GitHub 链接，没有就展示列表里的第一个
const primarySocial = computed(
  () => siteConfig.socials.find((s) => s.key === 'github') || siteConfig.socials[0]
)

// 全局快捷键：按 / 聚焦搜索框（详情页也能用）
function onKeydown(e) {
  if (e.key !== '/') return
  const tag = (e.target?.tagName || '').toLowerCase()
  if (tag === 'input' || tag === 'textarea' || e.target?.isContentEditable) return
  if (e.metaKey || e.ctrlKey || e.altKey) return
  e.preventDefault()
  inputRef.value?.focus()
}

onMounted(() => window.addEventListener('keydown', onKeydown))
onBeforeUnmount(() => window.removeEventListener('keydown', onKeydown))

// 点击 logo 回首页时，顺便清掉搜索词
function clearSearch() {
  if (route.path !== '/') searchQuery.value = ''
}
</script>

<style scoped>
.site-header {
  position: sticky;
  top: 0;
  z-index: 50;
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: saturate(180%) blur(12px);
  border-bottom: 1px solid var(--border);
}
.site-header__inner {
  max-width: 1180px;
  margin: 0 auto;
  padding: 12px 20px;
  display: flex;
  align-items: center;
  gap: 16px;
}
.site-header__brand {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
}
.site-header__logo {
  font-size: 24px;
}
.site-header__brand-text {
  display: flex;
  flex-direction: column;
  line-height: 1.2;
}
.site-header__brand-text strong {
  font-size: 15px;
  font-weight: 700;
}
.site-header__brand-text span {
  font-size: 11px;
  color: var(--text-muted);
}

.site-search {
  flex: 1;
  max-width: 460px;
  position: relative;
  display: flex;
  align-items: center;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 999px;
  transition: border-color 0.15s ease, box-shadow 0.15s ease, background 0.15s ease;
}
.site-search:focus-within {
  background: #fff;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px var(--accent-soft);
}
.site-search__icon {
  padding: 0 4px 0 14px;
  font-size: 14px;
  opacity: 0.6;
}
.site-search__input {
  flex: 1;
  border: none;
  outline: none;
  background: transparent;
  padding: 8px 8px 8px 4px;
  font-size: 14px;
  color: var(--text);
  font-family: inherit;
  min-width: 0;
}
.site-search__input::placeholder {
  color: var(--text-muted);
}
.site-search__input::-webkit-search-cancel-button {
  appearance: none;
}
.site-search__clear {
  margin-right: 8px;
  border: none;
  background: var(--border);
  color: var(--text-soft);
  width: 22px;
  height: 22px;
  border-radius: 50%;
  font-size: 11px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.site-search__clear:hover {
  background: var(--accent-soft);
  color: var(--accent);
}
.site-search__hint {
  margin-right: 10px;
  background: var(--bg-elev);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 1px 6px;
  font-family: ui-monospace, monospace;
  font-size: 11px;
  color: var(--text-muted);
}

.site-header__nav {
  display: flex;
  gap: 18px;
  font-size: 14px;
  flex-shrink: 0;
  align-items: center;
  margin-left: auto;
}
.site-header__nav a {
  color: var(--text-soft);
  font-weight: 500;
  transition: color 0.15s ease;
}
.site-header__nav a:hover {
  color: var(--accent);
}
.site-header__nav a.is-active {
  color: var(--accent);
}

/* GitHub 按钮：右上角深色 pill */
.site-header__github {
  flex-shrink: 0;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #1f2328;
  color: #fff !important;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 600;
  line-height: 1;
  white-space: nowrap;
  transition: background 0.15s ease, transform 0.15s ease;
}
.site-header__github:hover {
  background: #2d333b;
  transform: translateY(-1px);
}
.site-header__github-icon {
  flex-shrink: 0;
}

@media (max-width: 900px) {
  .site-header__nav {
    gap: 14px;
  }
}

@media (max-width: 760px) {
  .site-header__inner {
    gap: 10px;
    padding: 10px 14px;
  }
  .site-header__brand-text span {
    display: none;
  }
  .site-search__input {
    font-size: 13px;
  }
  .site-search__hint {
    display: none;
  }
  .site-header__nav {
    gap: 10px;
    font-size: 13px;
  }
  .site-header__github {
    padding: 6px 10px;
  }
  .site-header__github-label {
    display: none;
  }
}

@media (max-width: 480px) {
  .site-search {
    max-width: none;
  }
  .site-search__input::placeholder {
    color: transparent;
    text-shadow: none;
  }
  .site-header__nav a:not(.is-active):not([href="/contact"]):not([href="/"]) {
    display: none;
  }
}
</style>