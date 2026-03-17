<template>
  <header class="border-b border-secondary-200 bg-white shadow-sm">
    <nav class="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
      <!-- Logo and Brand -->
      <router-link to="/" class="flex items-center gap-2">
        <div class="flex h-10 w-10 items-center justify-center rounded-lg bg-primary-600">
          <svg class="h-6 w-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 016 0v6a3 3 0 01-3 3z" />
          </svg>
        </div>
        <span class="hidden text-xl font-bold text-secondary-900 sm:inline">HealthHistory</span>
      </router-link>

      <!-- Navigation Links -->
      <div class="flex items-center gap-1 sm:gap-4">
        <router-link
          to="/"
          :class="[
            'px-3 py-2 text-sm font-medium rounded-md transition-colors',
            $route.path === '/'
              ? 'bg-primary-50 text-primary-700'
              : 'text-secondary-700 hover:text-primary-600',
          ]"
        >
          Home
        </router-link>

        <div class="flex items-center gap-2 sm:gap-3">
          <router-link
            to="/login"
            :class="[
              'px-3 py-2 text-sm font-medium rounded-md transition-colors',
              $route.path === '/login'
                ? 'bg-primary-50 text-primary-700'
                : 'text-secondary-700 hover:text-primary-600',
            ]"
          >
            Sign In
          </router-link>
          <router-link
            to="/register"
            class="rounded-md bg-primary-600 px-3 py-2 text-sm font-medium text-white transition-colors hover:bg-primary-700"
          >
            Get Started
          </router-link>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router'

const route = useRoute()
</script>
