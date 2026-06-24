<template>
  <div class="app-shell">
    <SiteHeader />
    <main class="app-main">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>
    <footer class="app-footer">
      <p>© {{ year }} 晚枫 AI 项目集 · aiwf365.site</p>
    </footer>
  </div>
</template>

<script setup>
import SiteHeader from './components/SiteHeader.vue'
const year = new Date().getFullYear()
</script>

<style scoped>
.app-shell {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: var(--bg);
  color: var(--text);
}
.app-main {
  flex: 1;
  width: 100%;
}
.app-footer {
  text-align: center;
  padding: 32px 16px 40px;
  color: var(--text-muted);
  font-size: 13px;
  border-top: 1px solid var(--border);
  margin-top: 48px;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.18s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>