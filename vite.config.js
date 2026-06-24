import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// 部署在域名根目录，所以 base 用 '/'
// 如需挂在子路径，改这里即可，例如 '/aiwf365/'
export default defineConfig({
  plugins: [vue()],
  base: '/',
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    sourcemap: false,
    // 拆分 vendor 让首屏更快
    rollupOptions: {
      output: {
        manualChunks: {
          'vendor-vue': ['vue', 'vue-router'],
          'vendor-md': ['markdown-it'],
        },
      },
    },
  },
})