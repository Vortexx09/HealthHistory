<template>
  <div class="min-h-screen bg-gradient-to-br from-secondary-50 to-primary-50 px-4 py-20 sm:px-6 sm:py-24 lg:px-8">
    <div class="mx-auto max-w-2xl text-center">
      <div class="mb-6 flex justify-center">
        <div class="rounded-full bg-primary-100 p-6">
          <svg class="h-12 w-12 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </div>
      </div>

      <h1 class="text-4xl font-bold text-secondary-900">Page Under Construction</h1>
      <p class="mt-4 text-lg text-secondary-600">
        This page is being built. Check back soon for the latest features!
      </p>

      <div class="mt-8 space-y-4">
        <p class="text-secondary-600">
          Would you like us to build this page? Let us know what you'd like to see here.
        </p>

        <div class="flex flex-col gap-4 sm:flex-row sm:justify-center">
          <router-link
            to="/"
            class="inline-flex items-center justify-center rounded-lg bg-primary-600 px-6 py-3 text-base font-semibold text-white transition-colors hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2"
          >
            Back to Home
          </router-link>
          <a
            href="mailto:support@healthhistory.com"
            class="inline-flex items-center justify-center rounded-lg border border-secondary-300 px-6 py-3 text-base font-semibold text-secondary-700 transition-colors hover:border-secondary-400 hover:bg-secondary-50"
          >
            Send Feedback
          </a>
        </div>
      </div>

      <!-- Feature Highlight -->
      <div class="mt-16 grid gap-8 sm:grid-cols-3">
        <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
          <div class="flex justify-center">
            <div class="flex h-10 w-10 items-center justify-center rounded-lg bg-success-100">
              <svg class="h-6 w-6 text-success-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
            </div>
          </div>
          <h3 class="mt-4 font-semibold text-secondary-900">Quick Setup</h3>
          <p class="mt-2 text-sm text-secondary-600">
            Get started with HealthHistory in just a few minutes
          </p>
        </div>

        <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
          <div class="flex justify-center">
            <div class="flex h-10 w-10 items-center justify-center rounded-lg bg-primary-100">
              <svg class="h-6 w-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
          </div>
          <h3 class="mt-4 font-semibold text-secondary-900">Powerful Features</h3>
          <p class="mt-2 text-sm text-secondary-600">
            Access all your medical records in one place
          </p>
        </div>

        <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
          <div class="flex justify-center">
            <div class="flex h-10 w-10 items-center justify-center rounded-lg bg-accent-100">
              <svg class="h-6 w-6 text-accent-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
          </div>
          <h3 class="mt-4 font-semibold text-secondary-900">Secure & Safe</h3>
          <p class="mt-2 text-sm text-secondary-600">
            Your health data is protected with top-level security
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// This is a placeholder view for pages that haven't been built yet
// It shows a friendly message and allows users to navigate back
</script>
