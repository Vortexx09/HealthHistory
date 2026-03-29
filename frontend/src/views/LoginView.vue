<template>
  <div class="min-h-screen bg-gradient-to-br from-primary-50 to-secondary-50 px-4 py-12 sm:px-6 sm:py-16 lg:px-8">
    <div class="mx-auto w-full max-w-md">
      <!-- Logo Section -->
      <div class="mb-8 text-center">
        <div class="mx-auto mb-4 flex h-12 w-12 items-center justify-center rounded-lg bg-primary-600">
          <svg class="h-8 w-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 016 0v6a3 3 0 01-3 3z" />
          </svg>
        </div>
        <h1 class="text-2xl font-bold text-secondary-900">Welcome Back</h1>
        <p class="mt-2 text-secondary-600">Sign in to your HealthHistory account</p>
      </div>

      <!-- Form Card -->
      <div class="rounded-lg bg-white p-8 shadow-sm border border-secondary-200">
        <form @submit.prevent="handleLogin" class="space-y-6">
          <!-- ID Input -->
          <div>
            <label for="id_number" class="block text-sm font-medium text-secondary-900">
              Identification Number
            </label>
            <input
              id="id_number"
              v-model="form.id_number"
              type="id_number"
              required
              class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
              placeholder="123456789"
            />
          </div>

          <!-- Password Input -->
          <div>
            <label for="password" class="block text-sm font-medium text-secondary-900">
              Password
            </label>
            <input
              id="password"
              v-model="form.password"
              type="password"
              required
              class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
              placeholder="••••••••"
            />
          </div>

          <!-- Remember Me & Forgot Password -->
          <div class="flex items-center justify-between">
            <label class="flex items-center gap-2">
              <input
                v-model="form.rememberMe"
                type="checkbox"
                class="h-4 w-4 rounded border-secondary-300 text-primary-600 focus:ring-2 focus:ring-primary-500"
              />
              <span class="text-sm text-secondary-600">Remember me</span>
            </label>
            <a href="#" class="text-sm font-medium text-primary-600 hover:text-primary-700">
              Forgot password?
            </a>
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            :disabled="isLoading"
            class="w-full rounded-lg bg-primary-600 px-4 py-2.5 text-center font-semibold text-white transition-colors hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <span v-if="!isLoading">Sign In</span>
            <span v-else class="flex items-center justify-center gap-2">
              <svg class="h-4 w-4 animate-spin" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
              </svg>
              Signing in...
            </span>
          </button>

          <!-- Error Message -->
          <div v-if="errorMessage" class="rounded-lg bg-danger-50 p-3 text-sm text-danger-600 border border-danger-200">
            {{ errorMessage }}
          </div>

          <!-- Success Message -->
          <div v-if="successMessage" class="rounded-lg bg-success-50 p-3 text-sm text-success-600 border border-success-200">
            {{ successMessage }}
          </div>
        </form>

        <!-- Divider -->
        <div class="my-6 flex items-center gap-4">
          <div class="flex-1 border-t border-secondary-200" />
          <span class="text-xs text-secondary-500 font-medium">OR</span>
          <div class="flex-1 border-t border-secondary-200" />
        </div>

        <!-- Sign Up Link -->
        <div class="text-center">
          <p class="text-secondary-600">
            Don't have an account?
            <router-link to="/register" class="font-semibold text-primary-600 hover:text-primary-700">
              Create one
            </router-link>
          </p>
        </div>
      </div>

      <!-- Info Box -->
      <div class="mt-6 rounded-lg bg-blue-50 p-4 border border-blue-200">
        <p class="text-sm text-blue-900">
          <strong>Demo credentials:</strong> Use any id number and password to test the form (backend integration required)
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { user } from '../store/auth'
import { fetchUser, login } from '../services/authService'

const router = useRouter()

const form = ref({
  id_number: '',
  password: '',
  rememberMe: false,
})

const isLoading = ref(false)
const errorMessage = ref('')
const successMessage = ref('')

const handleLogin = async () => {
  try {
    isLoading.value = true
    errorMessage.value = ''
    successMessage.value = ''

    // Login and authentication
    await login(form.value.id_number, form.value.password)
    await fetchUser()

    // Sucess message
    successMessage.value = 'Login successful!'
    
    // Redirect after a short delay
    setTimeout(() => {
      const role = user.value?.user_type 
      if (role === 'doctor') {
        router.push('/dashboard')
      } else {
        router.push('/')
      }
    }, 500)

  } catch (error: any) {
    errorMessage.value = error.response?.data?.detail || 'Login failed. Please try again.'

  } finally {
    isLoading.value = false

  }
}


</script>