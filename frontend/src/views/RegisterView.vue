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
        <h1 class="text-2xl font-bold text-secondary-900">Get Started</h1>
        <p class="mt-2 text-secondary-600">Create your HealthHistory account in minutes</p>
      </div>

      <!-- Form Card -->
      <div class="rounded-lg bg-white p-8 shadow-sm border border-secondary-200">
        <form @submit.prevent="handleRegister" class="space-y-5">
          <!-- First Name Input -->
          <div>
            <label for="firstName" class="block text-sm font-medium text-secondary-900">
              First Name
            </label>
            <input
              id="firstName"
              v-model="form.firstName"
              type="text"
              required
              class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
              placeholder="John"
            />
          </div>

          <!-- Last Name Input -->
          <div>
            <label for="lastName" class="block text-sm font-medium text-secondary-900">
              Last Name
            </label>
            <input
              id="lastName"
              v-model="form.lastName"
              type="text"
              required
              class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
              placeholder="Doe"
            />
          </div>

          <!-- ID Type Dropdown -->
          <div>
            <label for="idType" class="block text-sm font-medium text-secondary-900">
              Tipo de documento
            </label>

            <select
              id="idType"
              v-model="form.idType"
              required
              class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
            >
              <option disabled value="">Selecciona un tipo de documento</option>
              <option value="CC">Cédula de Ciudadanía</option>
              <option value="TI">Tarjeta de Identidad</option>
              <option value="CE">Cédula de Extranjería</option>
              <option value="PP">Pasaporte</option>
              <option value="PPT">Permiso por Protección Temporal</option>
              <option value="PEP">Permiso Especial de Permanencia</option>
              <option value="RC">Registro Civil</option>
              <option value="NIT">NIT</option>
            </select>
          </div>

          <!-- ID Number Input -->
          <div>
            <label for="idNumber" class="block text-sm font-medium text-secondary-900">
              ID Number
            </label>
            <input
              id="idNumber"
              v-model="form.idNumber"
              type="text"
              required
              class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
              placeholder="123456789"
            />
          </div>

          <!-- Email Input -->
          <div>
            <label for="email" class="block text-sm font-medium text-secondary-900">
              Email Address
            </label>
            <input
              id="email"
              v-model="form.email"
              type="email"
              required
              class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
              placeholder="you@example.com"
            />
          </div>

          <!-- Phone Input -->
          <div>
            <label for="phone" class="block text-sm font-medium text-secondary-900">
              Phone Number
            </label>
            <input
              id="phone"
              v-model="form.phone"
              type="text"
              required
              class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
              placeholder="123 456 7890"
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
              @input="validatePassword"
              class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
              placeholder="••••••••"
            />
            <!-- Password Strength Indicator -->
            <div v-if="form.password" class="mt-2 flex gap-1">
              <div
                class="h-1 flex-1 rounded-full"
                :class="passwordStrength >= 1 ? 'bg-danger-500' : 'bg-secondary-300'"
              />
              <div
                class="h-1 flex-1 rounded-full"
                :class="passwordStrength >= 2 ? 'bg-accent-500' : 'bg-secondary-300'"
              />
              <div
                class="h-1 flex-1 rounded-full"
                :class="passwordStrength >= 3 ? 'bg-success-500' : 'bg-secondary-300'"
              />
            </div>
            <p class="mt-1 text-xs text-secondary-600">
              Password must be at least 8 characters
            </p>
          </div>

          <!-- Confirm Password Input -->
          <div>
            <label for="confirmPassword" class="block text-sm font-medium text-secondary-900">
              Confirm Password
            </label>
            <input
              id="confirmPassword"
              v-model="form.confirmPassword"
              type="password"
              required
              class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
              placeholder="••••••••"
            />
            <p
              v-if="form.confirmPassword && form.password !== form.confirmPassword"
              class="mt-1 text-xs text-danger-600"
            >
              Passwords do not match
            </p>
          </div>

          <!-- Terms Checkbox -->
          <label class="flex items-start gap-3">
            <input
              v-model="form.agreeToTerms"
              type="checkbox"
              required
              class="mt-1 h-4 w-4 rounded border-secondary-300 text-primary-600 focus:ring-2 focus:ring-primary-500"
            />
            <span class="text-sm text-secondary-600">
              I agree to the
              <a href="#" class="font-medium text-primary-600 hover:text-primary-700">
                Terms of Service
              </a>
              and
              <a href="#" class="font-medium text-primary-600 hover:text-primary-700">
                Privacy Policy
              </a>
            </span>
          </label>

          <!-- Submit Button -->
          <button
            type="submit"
            :disabled="isLoading || !isFormValid"
            class="w-full rounded-lg bg-primary-600 px-4 py-2.5 text-center font-semibold text-white transition-colors hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <span v-if="!isLoading">Create Account</span>
            <span v-else class="flex items-center justify-center gap-2">
              <svg class="h-4 w-4 animate-spin" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
              </svg>
              Creating account...
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

        <!-- Sign In Link -->
        <div class="text-center">
          <p class="text-secondary-600">
            Already have an account?
            <router-link to="/login" class="font-semibold text-primary-600 hover:text-primary-700">
              Sign in
            </router-link>
          </p>
        </div>
      </div>

      <!-- Info Box -->
      <div class="mt-6 rounded-lg bg-blue-50 p-4 border border-blue-200">
        <p class="text-sm text-blue-900">
          <strong>Note:</strong> This is a demo form. Complete backend integration with Django REST Framework is required for production use.
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

const form = ref({
  firstName: '',
  lastName: '',
  idType: '',
  idNumber: '',
  email: '',
  password: '',
  confirmPassword: '',
  phone: '',
  agreeToTerms: false,
})

const isLoading = ref(false)
const errorMessage = ref('')
const successMessage = ref('')
const passwordStrength = ref(0)

const isFormValid = computed(() => {
  return (
    form.value.firstName.trim() !== '' &&
    form.value.lastName.trim() !== '' &&
    form.value.email.trim() !== '' &&
    form.value.password.length >= 8 &&
    form.value.password === form.value.confirmPassword &&
    form.value.agreeToTerms
  )
})

const validatePassword = () => {
  const password = form.value.password
  let strength = 0

  if (password.length >= 8) strength++
  if (/[a-z]/.test(password) && /[A-Z]/.test(password)) strength++
  if (/\d/.test(password) || /[!@#$%^&*]/.test(password)) strength++

  passwordStrength.value = strength
}

const handleRegister = async () => {
  try {
    isLoading.value = true
    errorMessage.value = ''
    successMessage.value = ''

    // API call
    const response = await axios.post('http://127.0.0.1:8000/users/', {
      username: form.value.idNumber,
      first_name: form.value.firstName,
      last_name: form.value.lastName,
      email: form.value.email,
      password: form.value.password,
      id_number: form.value.idNumber,
      id_type: form.value.idType,
      phone: form.value.phone,
    })

    successMessage.value = 'Account created successfully!'

    // Redirect after a short delay
    setTimeout(() => {
      router.push('/login')
    }, 1500)
  } catch (error: any) {
    errorMessage.value = error.response?.data?.message || 'Registration failed. Please try again.'
  } finally {
    isLoading.value = false
  }
}
</script>
