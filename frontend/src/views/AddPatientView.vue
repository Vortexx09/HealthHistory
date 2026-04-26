<template>
  <div class="min-h-screen bg-secondary-50">
    <!-- Header -->
    <div class="border-b border-secondary-200 bg-white shadow-sm">
      <div class="mx-auto max-w-4xl px-4 py-6 sm:px-6 lg:px-8">
        <div class="flex items-center gap-4">
          <button
            @click="$router.back()"
            class="rounded-lg p-2 hover:bg-secondary-100 transition-colors"
          >
            <svg class="h-6 w-6 text-secondary-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
            </svg>
          </button>
          <div>
            <h1 class="text-3xl font-bold text-secondary-900">Agregar Nuevo Paciente</h1>
            <p class="mt-1 text-secondary-600">Complete los datos del paciente en los siguientes campos</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Form Content -->
    <div class="mx-auto max-w-4xl px-4 py-8 sm:px-6 lg:px-8">
      <form @submit.prevent="handleSubmit" class="space-y-6">
        <!-- Personal Data Section -->
        <div class="rounded-lg bg-white p-8 shadow-sm border border-secondary-200">
          <div class="mb-6 flex items-center gap-3">
            <div class="flex h-10 w-10 items-center justify-center rounded-lg bg-primary-100">
              <svg class="h-6 w-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <div>
              <h2 class="text-2xl font-bold text-secondary-900">Datos Personales</h2>
              <p class="text-secondary-600">Información básica del paciente</p>
            </div>
          </div>

          <div class="space-y-5">
            <!-- First and Last Name Row -->
            <div class="grid gap-5 sm:grid-cols-2">
              <div>
                <label for="firstName" class="block text-sm font-medium text-secondary-900">
                  Nombre Completo <span class="text-danger-600">*</span>
                </label>
                <input
                  id="firstName"
                  v-model="form.personal.first_name"
                  type="text"
                  required
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                  placeholder="Juan"
                />
              </div>
              <div>
                <label for="lastName" class="block text-sm font-medium text-secondary-900">
                  Apellido <span class="text-danger-600">*</span>
                </label>
                <input
                  id="lastName"
                  v-model="form.personal.last_name"
                  type="text"
                  required
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                  placeholder="Pérez"
                />
              </div>
            </div>

            <!-- ID Number and Type Row -->
            <div class="grid gap-5 sm:grid-cols-2">
              <div>
                <label for="idNumber" class="block text-sm font-medium text-secondary-900">
                  Número de Identificación <span class="text-danger-600">*</span>
                </label>
                <input
                  id="idNumber"
                  v-model="form.personal.id_number"
                  type="text"
                  required
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                  placeholder="12345678"
                />
              </div>
              <div>
                <label for="idType" class="block text-sm font-medium text-secondary-900">
                  Tipo de Identificación <span class="text-danger-600">*</span>
                </label>
                <select
                  id="idType"
                  v-model="form.personal.id_type"
                  required
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                >
                  <option value="">Seleccionar tipo</option>
                  <option value="CC">Cédula de Ciudadanía</option>
                  <option value="TI">Tarjeta de Identidad</option>
                  <option value="CE">Cédula de Extranjería</option>
                  <option value="PA">Pasaporte</option>
                </select>
              </div>
            </div>

            <!-- Date of Birth and Sex Row -->
            <div class="grid gap-5 sm:grid-cols-2">
              <div>
                <label for="dob" class="block text-sm font-medium text-secondary-900">
                  Fecha de Nacimiento
                </label>
                <input
                  id="dob"
                  v-model="form.personal.dob"
                  type="date"
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                />
              </div>
              <div>
                <label for="sex" class="block text-sm font-medium text-secondary-900">
                  Sexo Biológico <span class="text-danger-600">*</span>
                </label>
                <select
                  id="sex"
                  v-model="form.personal.sex_code"
                  required
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                >
                  <option value="">Seleccionar sexo</option>
                  <option value="M">Masculino</option>
                  <option value="F">Femenino</option>
                  <option value="O">Otro</option>
                </select>
              </div>
            </div>

            <!-- Email and Phone Row -->
            <div class="grid gap-5 sm:grid-cols-2">
              <div>
                <label for="email" class="block text-sm font-medium text-secondary-900">
                  Correo Electrónico <span class="text-danger-600">*</span>
                </label>
                <input
                  id="email"
                  v-model="form.personal.email"
                  type="email"
                  required
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                  placeholder="juan@ejemplo.com"
                />
              </div>
              <div>
                <label for="phone" class="block text-sm font-medium text-secondary-900">
                  Teléfono <span class="text-danger-600">*</span>
                </label>
                <input
                  id="phone"
                  v-model="form.personal.phone"
                  type="tel"
                  required
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                  placeholder="+57 300 123 4567"
                />
              </div>
            </div>

            <!-- Place of Birth and Occupation Row -->
            <div class="grid gap-5 sm:grid-cols-2">
              <div>
                <label for="pob" class="block text-sm font-medium text-secondary-900">
                  Lugar de Nacimiento
                </label>
                <input
                  id="pob"
                  v-model="form.personal.pob"
                  type="text"
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                  placeholder="Bogotá, Cundinamarca"
                />
              </div>
              <div>
                <label for="occupation" class="block text-sm font-medium text-secondary-900">
                  Ocupación
                </label>
                <input
                  id="occupation"
                  v-model="form.personal.occupation"
                  type="text"
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                  placeholder="Ingeniería"
                />
              </div>
            </div>

            <!-- Civil Status and Religion Row -->
            <div class="grid gap-5 sm:grid-cols-2">
              <div>
                <label for="civilStatus" class="block text-sm font-medium text-secondary-900">
                  Estado Civil
                </label>
                <select
                  id="civilStatus"
                  v-model="form.personal.civil_status"
                  required
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                >
                  <option value="">Seleccionar tipo</option>
                  <option value="Soltero">Soltero(a)</option>
                  <option value="Casado">Casado(a)</option>
                  <option value="Unión Libre">Unión Libre</option>
                  <option value="Divorciado">Divorciado(a)</option>
                  <option value="Separado">Separado(a)</option>
                  <option value="Viudo">Viudo(a)</option>
                </select>
              </div>
              <div>
                <label for="religion" class="block text-sm font-medium text-secondary-900">
                  Religión
                </label>
                <input
                  id="religion"
                  v-model="form.personal.religion"
                  type="text"
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                  placeholder="Católico(a)"
                />
              </div>
            </div>

            <!-- Address -->
            <div>
              <label for="address" class="block text-sm font-medium text-secondary-900">
                Dirección
              </label>
              <input
                id="address"
                v-model="form.personal.address"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Calle 123 #45-67, Apartamento 8B"
              />
            </div>
          </div>
        </div>

        <!-- Medical Data Section -->
        <div class="rounded-lg bg-white p-8 shadow-sm border border-secondary-200">
          <div class="mb-6 flex items-center gap-3">
            <div class="flex h-10 w-10 items-center justify-center rounded-lg bg-accent-100">
              <svg class="h-6 w-6 text-accent-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <div>
              <h2 class="text-2xl font-bold text-secondary-900">Datos Médicos</h2>
              <p class="text-secondary-600">Antecedentes médicos y hábitos del paciente</p>
            </div>
          </div>

          <div class="space-y-4">
            <!-- Medical Conditions -->
            <div class="grid gap-4 sm:grid-cols-2">
              <label class="flex items-center gap-3 rounded-lg border border-secondary-200 p-4 cursor-pointer hover:bg-secondary-50 transition-colors">
                <input
                  v-model="form.medical.disability"
                  type="checkbox"
                  class="h-4 w-4 rounded border-secondary-300 text-primary-600 focus:ring-2 focus:ring-primary-500"
                />
                <div>
                  <span class="font-medium text-secondary-900">Discapacidad</span>
                  <p class="text-xs text-secondary-600">¿El paciente tiene alguna discapacidad?</p>
                </div>
              </label>

              <label class="flex items-center gap-3 rounded-lg border border-secondary-200 p-4 cursor-pointer hover:bg-secondary-50 transition-colors">
                <input
                  v-model="form.medical.diabetes"
                  type="checkbox"
                  class="h-4 w-4 rounded border-secondary-300 text-primary-600 focus:ring-2 focus:ring-primary-500"
                />
                <div>
                  <span class="font-medium text-secondary-900">Diabetes</span>
                  <p class="text-xs text-secondary-600">¿El paciente tiene diabetes?</p>
                </div>
              </label>

              <label class="flex items-center gap-3 rounded-lg border border-secondary-200 p-4 cursor-pointer hover:bg-secondary-50 transition-colors">
                <input
                  v-model="form.medical.cancer"
                  type="checkbox"
                  class="h-4 w-4 rounded border-secondary-300 text-primary-600 focus:ring-2 focus:ring-primary-500"
                />
                <div>
                  <span class="font-medium text-secondary-900">Cáncer</span>
                  <p class="text-xs text-secondary-600">¿Antecedentes de cáncer?</p>
                </div>
              </label>

              <label class="flex items-center gap-3 rounded-lg border border-secondary-200 p-4 cursor-pointer hover:bg-secondary-50 transition-colors">
                <input
                  v-model="form.medical.alcohol_consumption"
                  type="checkbox"
                  class="h-4 w-4 rounded border-secondary-300 text-primary-600 focus:ring-2 focus:ring-primary-500"
                />
                <div>
                  <span class="font-medium text-secondary-900">Consumo de Alcohol</span>
                  <p class="text-xs text-secondary-600">¿Consume alcohol regularmente?</p>
                </div>
              </label>

              <label class="flex items-center gap-3 rounded-lg border border-secondary-200 p-4 cursor-pointer hover:bg-secondary-50 transition-colors">
                <input
                  v-model="form.medical.smoker"
                  type="checkbox"
                  class="h-4 w-4 rounded border-secondary-300 text-primary-600 focus:ring-2 focus:ring-primary-500"
                />
                <div>
                  <span class="font-medium text-secondary-900">Fumador</span>
                  <p class="text-xs text-secondary-600">¿El paciente fuma o fumó?</p>
                </div>
              </label>

              <label class="flex items-center gap-3 rounded-lg border border-secondary-200 p-4 cursor-pointer hover:bg-secondary-50 transition-colors">
                <input
                  v-model="form.medical.drug_use"
                  type="checkbox"
                  class="h-4 w-4 rounded border-secondary-300 text-primary-600 focus:ring-2 focus:ring-primary-500"
                />
                <div>
                  <span class="font-medium text-secondary-900">Uso de Drogas</span>
                  <p class="text-xs text-secondary-600">¿Historia de consumo de drogas?</p>
                </div>
              </label>
            </div>

            <!-- Occupational Risk -->
            <div>
              <label for="occupationalRisk" class="block text-sm font-medium text-secondary-900">
                Riesgo Ocupacional
              </label>
              <textarea
                id="occupationalRisk"
                v-model="form.medical.occupational_risk"
                rows="4"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Describe cualquier riesgo ocupacional relevante..."
              />
              <p class="mt-1 text-xs text-secondary-600">Información sobre riesgos en su ambiente de trabajo</p>
            </div>
          </div>
        </div>

        <!-- Error Message -->
        <div v-if="errorMessage" class="rounded-lg bg-danger-50 p-4 text-sm text-danger-600 border border-danger-200">
          {{ errorMessage }}
        </div>

        <!-- Success Message -->
        <div v-if="successMessage" class="rounded-lg bg-success-50 p-4 text-sm text-success-600 border border-success-200">
          {{ successMessage }}
        </div>

        <!-- Form Actions -->
        <div class="flex gap-4 sm:justify-end">
          <button
            type="button"
            @click="$router.push('/dashboard')"
            class="rounded-lg border border-secondary-300 px-6 py-3 text-center font-semibold text-secondary-700 transition-colors hover:bg-secondary-50"
          >
            Cancelar
          </button>
          <button
            type="submit"
            :disabled="isLoading"
            class="rounded-lg bg-primary-600 px-6 py-3 text-center font-semibold text-white transition-colors hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <span v-if="!isLoading">Guardar Paciente</span>
            <span v-else class="flex items-center justify-center gap-2">
              <svg class="h-4 w-4 animate-spin" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
              </svg>
              Guardando...
            </span>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { refreshToken } from '../services/authService'
import { user } from '../store/auth'

const router = useRouter()

const form = ref({
  personal: {
    first_name: '',
    last_name: '',
    id_number: '',
    id_type: '',
    phone: '',
    dob: '',
    email: '',
    address: '',
    sex_code: '',
    pob: '',
    occupation: '',
    civil_status: '',
    religion: '',
  },
  medical: {
    disability: false,
    diabetes: false,
    cancer: false,
    alcohol_consumption: false,
    smoker: false,
    drug_use: false,
    occupational_risk: '',
  },
})

const isLoading = ref(false)
const errorMessage = ref('')
const successMessage = ref('')

const handleSubmit = async () => {
  try {
    isLoading.value = true
    errorMessage.value = ''
    successMessage.value = ''

    await refreshToken()

    // API call - user
    const userResponse = await axios.post('http://127.0.0.1:8000/patients/create/', {
      user: {
        user_type: 2,
        username: form.value.personal.id_number,
        first_name: form.value.personal.first_name,
        last_name: form.value.personal.last_name,
        id_number: form.value.personal.id_number,
        id_type: form.value.personal.id_type,
        phone: form.value.personal.phone,
        email: form.value.personal.email,
        password: form.value.personal.id_number,
      },
      patient: {
        address: form.value.personal.address,
        sex_code: form.value.personal.sex_code,
        dob: form.value.personal.dob,
        pob: form.value.personal.pob,
        occupation: form.value.personal.occupation,
      },
      register: {
        disability: form.value.medical.disability,
        diabetes: form.value.medical.diabetes,
        cancer: form.value.medical.cancer,
        alcohol_consumption: form.value.medical.alcohol_consumption,
        smoker: form.value.medical.smoker,
        drug_use: form.value.medical.drug_use,
        occupational_risk: form.value.medical.occupational_risk,
      }
    })

    successMessage.value = '¡Paciente agregado exitosamente!'

    // Redirect to history after a short delay
    setTimeout(() => {
      router.push('/add-history')
    }, 1500)
  } catch (error: any) {
    errorMessage.value = error.response?.data?.message || 'Error al guardar el paciente. Por favor intenta de nuevo.'
  } finally {
    isLoading.value = false
  }
}
</script>
