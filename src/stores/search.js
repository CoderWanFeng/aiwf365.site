import { ref } from 'vue'

// 全站共享的搜索词：Header 输入，Home 过滤；详情页只读展示
export const searchQuery = ref('')