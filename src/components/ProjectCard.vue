<template>
  <router-link :to="`/project/${project.slug}`" class="card">
    <div class="card__cover">
      <img :src="project.cover" :alt="project.title" loading="lazy" />
      <span v-if="project.featured" class="card__badge">精选</span>
    </div>
    <div class="card__body">
      <h3 class="card__title">{{ project.title }}</h3>
      <p class="card__summary">{{ project.summary }}</p>
      <div class="card__meta">
        <span v-for="t in project.tags.slice(0, 2)" :key="t" class="card__tag">
          {{ t }}
        </span>
        <span class="card__date">{{ formatDate(project.date) }}</span>
      </div>
    </div>
  </router-link>
</template>

<script setup>
defineProps({
  project: { type: Object, required: true },
})

function formatDate(iso) {
  if (!iso) return ''
  const d = new Date(iso)
  return `${d.getFullYear()}.${String(d.getMonth() + 1).padStart(2, '0')}.${String(
    d.getDate()
  ).padStart(2, '0')}`
}
</script>

<style scoped>
.card {
  display: flex;
  flex-direction: column;
  background: var(--bg-elev);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: transform 0.18s ease, box-shadow 0.18s ease,
    border-color 0.18s ease;
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
  border-color: rgba(255, 90, 31, 0.35);
}
.card__cover {
  position: relative;
  aspect-ratio: 16 / 10;
  overflow: hidden;
  background: linear-gradient(135deg, #f3f4f6, #e5e7eb);
}
.card__cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}
.card:hover .card__cover img {
  transform: scale(1.04);
}
.card__badge {
  position: absolute;
  top: 10px;
  left: 10px;
  background: var(--accent);
  color: #fff;
  font-size: 11px;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: 999px;
  letter-spacing: 0.5px;
}
.card__body {
  padding: 14px 16px 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  flex: 1;
}
.card__title {
  font-size: 16px;
  font-weight: 700;
  line-height: 1.4;
  margin: 0;
  color: var(--text);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.card__summary {
  margin: 0;
  font-size: 13px;
  color: var(--text-muted);
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.card__meta {
  margin-top: auto;
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
}
.card__tag {
  background: var(--accent-soft);
  color: var(--accent);
  font-size: 11px;
  padding: 2px 8px;
  border-radius: 4px;
  font-weight: 500;
}
.card__date {
  margin-left: auto;
  font-size: 11px;
  color: var(--text-muted);
}
</style>