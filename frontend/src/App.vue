<script setup lang="ts">
import { onMounted } from 'vue'
import { user } from './store/auth'
import Header from './components/Header.vue'

onMounted(async () => {
})

</script>

<template>
  <div class="min-h-screen bg-white">
    <Header />
    <main>
      <router-view />
    </main>
  </div>
</template>

<style scoped></style>
