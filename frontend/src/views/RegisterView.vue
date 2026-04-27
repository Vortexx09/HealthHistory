<template>
  <div class="min-h-screen bg-gradient-to-br from-primary-50 to-secondary-50 px-4 py-12 sm:px-6 sm:py-16 lg:px-8">
    <div class="mx-auto w-full max-w-md">
      <!-- Sección del logotipo -->
      <div class="mb-8 text-center">
        <div class="mx-auto mb-4 flex h-12 w-12 items-center justify-center rounded-lg bg-primary-600">
          <svg class="h-8 w-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 016 0v6a3 3 0 01-3 3z" />
          </svg>
        </div>
        <h1 class="text-2xl font-bold text-secondary-900">Comienza ahora</h1>
        <p class="mt-2 text-secondary-600">Crea tu cuenta de HealthHistory en minutos</p>
      </div>

      <!-- Tarjeta del formulario -->
      <div class="rounded-lg bg-white p-8 shadow-sm border border-secondary-200">
        <form @submit.prevent="handleRegister" class="space-y-5">
          <!-- Campo: Nombre -->
          <div>
            <label for="firstName" class="block text-sm font-medium text-secondary-900">
              Nombre
            </label>
            <input
              id="firstName"
              v-model="form.firstName"
              type="text"
              required
              class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
              placeholder="Juan"
            />
          </div>

          <!-- Campo: Apellido -->
          <div>
            <label for="lastName" class="block text-sm font-medium text-secondary-900">
              Apellido
            </label>
            <input
              id="lastName"
              v-model="form.lastName"
              type="text"
              required
              class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
              placeholder="Pérez"
            />
          </div>

          <!-- Campo: Tipo de documento -->
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

          <!-- Campo: Número de identificación -->
          <div>
            <label for="idNumber" class="block text-sm font-medium text-secondary-900">
              Número de identificación
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

          <!-- Campo: Correo electrónico -->
          <div>
            <label for="email" class="block text-sm font-medium text-secondary-900">
              Correo electrónico
            </label>
            <input
              id="email"
              v-model="form.email"
              type="email"
              required
              class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
              placeholder="tu@ejemplo.com"
            />
          </div>

          <!-- Campo: Número de teléfono -->
          <div>
            <label for="phone" class="block text-sm font-medium text-secondary-900">
              Número de teléfono
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

          <!-- Campo: Contraseña -->
          <div>
            <label for="password" class="block text-sm font-medium text-secondary-900">
              Contraseña
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
            <!-- Indicador de fortaleza de la contraseña -->
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
              La contraseña debe tener al menos 8 caracteres
            </p>
          </div>

          <!-- Campo: Confirmar contraseña -->
          <div>
            <label for="confirmPassword" class="block text-sm font-medium text-secondary-900">
              Confirmar contraseña
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
              Las contraseñas no coinciden
            </p>
          </div>

          <!-- Checkbox de términos -->
          <label class="flex items-start gap-3">
            <input
              v-model="form.agreeToTerms"
              type="checkbox"
              required
              class="mt-1 h-4 w-4 rounded border-secondary-300 text-primary-600 focus:ring-2 focus:ring-primary-500"
            />
            <span class="text-sm text-secondary-600">
              Acepto los
              <a href="#" class="font-medium text-primary-600 hover:text-primary-700">
                Términos de servicio
              </a>
              y la
              <a href="#" class="font-medium text-primary-600 hover:text-primary-700">
                Política de privacidad
              </a>
            </span>
          </label>

          <!-- Botón de envío -->
          <button
            type="submit"
            :disabled="isLoading || !isFormValid"
            class="w-full rounded-lg bg-primary-600 px-4 py-2.5 text-center font-semibold text-white transition-colors hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <span v-if="!isLoading">Crear cuenta</span>
            <span v-else class="flex items-center justify-center gap-2">
              <svg class="h-4 w-4 animate-spin" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
              </svg>
              Creando cuenta...
            </span>
          </button>

          <!-- Mensaje de error -->
          <div v-if="errorMessage" class="rounded-lg bg-danger-50 p-3 text-sm text-danger-600 border border-danger-200">
            {{ errorMessage }}
          </div>

          <!-- Mensaje de éxito -->
          <div v-if="successMessage" class="rounded-lg bg-success-50 p-3 text-sm text-success-600 border border-success-200">
            {{ successMessage }}
          </div>
        </form>

        <!-- Divisor -->
        <div class="my-6 flex items-center gap-4">
          <div class="flex-1 border-t border-secondary-200" />
          <span class="text-xs text-secondary-500 font-medium">O</span>
          <div class="flex-1 border-t border-secondary-200" />
        </div>

        <!-- Enlace de inicio de sesión -->
        <div class="text-center">
          <p class="text-secondary-600">
            ¿Ya tienes una cuenta?
            <router-link to="/login" class="font-semibold text-primary-600 hover:text-primary-700">
              Inicia sesión
            </router-link>
          </p>
        </div>
      </div>

      <!-- Caja de información -->
      <div class="mt-6 rounded-lg bg-blue-50 p-4 border border-blue-200">
        <p class="text-sm text-blue-900">
          <strong>Nota:</strong> Este es un formulario de demostración. Se requiere integración completa con Django REST Framework para uso en producción.
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
