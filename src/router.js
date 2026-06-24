import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('./pages/Home.vue'),
  },
  {
    path: '/tutorials',
    name: 'tutorials',
    component: () => import('./pages/Home.vue'),
    props: { initialTag: '教程入门' },
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('./pages/About.vue'),
  },
  {
    path: '/contact',
    name: 'contact',
    component: () => import('./pages/Contact.vue'),
  },
  {
    path: '/project/:slug',
    name: 'project',
    component: () => import('./pages/ProjectDetail.vue'),
    props: true,
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'not-found',
    component: () => import('./pages/NotFound.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition
    return { top: 0 }
  },
})

export default router