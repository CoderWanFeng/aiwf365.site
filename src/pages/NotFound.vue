<template>
  <div class="not-found">
    <h1>404</h1>
    <p>页面飞走了 🌿</p>
    <router-link to="/" class="not-found__link">回到首页</router-link>
  </div>
</template>

<style scoped>
.not-found {
  max-width: 600px;
  margin: 120px auto;
  text-align: center;
  padding: 0 20px;
}
.not-found h1 {
  font-size: 72px;
  font-weight: 900;
  color: var(--accent);
  margin: 0;
  letter-spacing: -2px;
}
.not-found p {
  font-size: 16px;
  color: var(--text-muted);
  margin: 8px 0 28px;
}
.not-found__link {
  display: inline-block;
  background: var(--accent);
  color: #fff;
  padding: 10px 22px;
  border-radius: 999px;
  font-size: 14px;
  font-weight: 500;
  transition: opacity 0.15s ease;
}
.not-found__link:hover {
  opacity: 0.9;
}
</style>