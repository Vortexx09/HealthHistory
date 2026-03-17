<template>
  <div class="bg-white">
    <!-- Hero Section -->
    <section class="relative overflow-hidden px-4 py-20 sm:px-6 sm:py-24 lg:px-8 lg:py-32">
      <div class="mx-auto max-w-5xl">
        <div class="grid gap-12 lg:grid-cols-2 lg:gap-8 lg:items-center">
          <!-- Hero Content -->
          <div class="flex flex-col justify-center">
            <h1 class="text-4xl font-bold tracking-tight text-secondary-900 sm:text-5xl">
              Your Health Records,
              <span class="block text-primary-600">Always at Your Fingertips</span>
            </h1>
            <p class="mt-6 text-lg text-secondary-600">
              Securely manage your medical history in one place. Access your health records anytime, share with healthcare providers, and take control of your wellness journey.
            </p>
            <div class="mt-8 flex flex-col gap-4 sm:flex-row sm:gap-4">
              <router-link
                to="/register"
                class="inline-flex items-center justify-center rounded-lg bg-primary-600 px-6 py-3 text-base font-semibold text-white transition-colors hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2"
              >
                Start Free
              </router-link>
              <button
                @click="scrollToFeatures"
                class="inline-flex items-center justify-center rounded-lg border border-secondary-300 px-6 py-3 text-base font-semibold text-secondary-700 transition-colors hover:border-secondary-400 hover:bg-secondary-50"
              >
                Learn More
              </button>
            </div>
            <div class="mt-8 flex items-center gap-8">
              <div>
                <div class="text-2xl font-bold text-secondary-900">10,000+</div>
                <div class="text-sm text-secondary-600">Active Users</div>
              </div>
              <div>
                <div class="text-2xl font-bold text-secondary-900">99.9%</div>
                <div class="text-sm text-secondary-600">Uptime</div>
              </div>
              <div>
                <div class="text-2xl font-bold text-secondary-900">100%</div>
                <div class="text-sm text-secondary-600">Encrypted</div>
              </div>
            </div>
          </div>

          <!-- Hero Image -->
          <div class="hidden lg:block">
            <div class="relative mx-auto h-96 w-full rounded-2xl bg-gradient-to-br from-primary-100 to-primary-50 p-8 shadow-xl">
              <svg class="h-full w-full text-primary-600 opacity-30" fill="currentColor" viewBox="0 0 24 24">
                <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <div class="absolute inset-0 flex items-center justify-center">
                <div class="text-center">
                  <svg class="mx-auto h-16 w-16 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  <p class="mt-4 text-lg font-semibold text-primary-900">Medical Records</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section ref="featuresRef" class="bg-secondary-50 px-4 py-20 sm:px-6 sm:py-24 lg:px-8">
      <div class="mx-auto max-w-5xl">
        <div class="text-center">
          <h2 class="text-3xl font-bold tracking-tight text-secondary-900 sm:text-4xl">
            Features Built for Your Health
          </h2>
          <p class="mt-4 text-lg text-secondary-600">
            Everything you need to manage your medical records efficiently
          </p>
        </div>

        <div class="mt-16 grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
          <!-- Feature 1 -->
          <div class="rounded-lg bg-white p-8 shadow-sm border border-secondary-200">
            <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-primary-100">
              <svg class="h-6 w-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
              </svg>
            </div>
            <h3 class="mt-4 text-lg font-semibold text-secondary-900">Easy Management</h3>
            <p class="mt-2 text-secondary-600">
              Organize and manage all your medical records in one secure location
            </p>
          </div>

          <!-- Feature 2 -->
          <div class="rounded-lg bg-white p-8 shadow-sm border border-secondary-200">
            <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-primary-100">
              <svg class="h-6 w-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
              </svg>
            </div>
            <h3 class="mt-4 text-lg font-semibold text-secondary-900">Bank-Level Security</h3>
            <p class="mt-2 text-secondary-600">
              Your data is encrypted with the highest security standards
            </p>
          </div>

          <!-- Feature 3 -->
          <div class="rounded-lg bg-white p-8 shadow-sm border border-secondary-200">
            <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-primary-100">
              <svg class="h-6 w-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m7 0a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <h3 class="mt-4 text-lg font-semibold text-secondary-900">Share Securely</h3>
            <p class="mt-2 text-secondary-600">
              Grant access to healthcare providers when you need it
            </p>
          </div>

          <!-- Feature 4 -->
          <div class="rounded-lg bg-white p-8 shadow-sm border border-secondary-200">
            <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-primary-100">
              <svg class="h-6 w-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <h3 class="mt-4 text-lg font-semibold text-secondary-900">Fast Access</h3>
            <p class="mt-2 text-secondary-600">
              Get instant access to your records anytime, anywhere
            </p>
          </div>

          <!-- Feature 5 -->
          <div class="rounded-lg bg-white p-8 shadow-sm border border-secondary-200">
            <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-primary-100">
              <svg class="h-6 w-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
            </div>
            <h3 class="mt-4 text-lg font-semibold text-secondary-900">Health Insights</h3>
            <p class="mt-2 text-secondary-600">
              Track trends and get insights about your health over time
            </p>
          </div>

          <!-- Feature 6 -->
          <div class="rounded-lg bg-white p-8 shadow-sm border border-secondary-200">
            <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-primary-100">
              <svg class="h-6 w-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 5.636l-3.536 3.536m0 5.656l3.536 3.536M9.172 9.172L5.636 5.636m3.536 9.192l-3.536 3.536M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-5 0a4 4 0 11-8 0 4 4 0 018 0z" />
              </svg>
            </div>
            <h3 class="mt-4 text-lg font-semibold text-secondary-900">24/7 Support</h3>
            <p class="mt-2 text-secondary-600">
              Our team is always available to help you
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="px-4 py-20 sm:px-6 sm:py-24 lg:px-8">
      <div class="mx-auto max-w-2xl text-center">
        <h2 class="text-3xl font-bold tracking-tight text-secondary-900 sm:text-4xl">
          Take Control of Your Health Today
        </h2>
        <p class="mt-4 text-lg text-secondary-600">
          Join thousands of users who trust HealthHistory with their medical records
        </p>
        <div class="mt-8">
          <router-link
            to="/register"
            class="inline-flex items-center justify-center rounded-lg bg-primary-600 px-8 py-3 text-lg font-semibold text-white transition-colors hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2"
          >
            Create Your Account
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const featuresRef = ref<HTMLElement | null>(null)

const scrollToFeatures = () => {
  if (featuresRef.value) {
    featuresRef.value.scrollIntoView({ behavior: 'smooth' })
  }
}
</script>
