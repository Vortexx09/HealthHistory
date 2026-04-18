<template>
  <div class="min-h-screen bg-secondary-50">
    <!-- Header -->
    <div class="border-b border-secondary-200 bg-white shadow-sm">
      <div class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
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
            <h1 class="text-3xl font-bold text-secondary-900">Administrar Pacientes</h1>
            <p class="mt-1 text-secondary-600">Gestionar historial médico y citas</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Content -->
    <div class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
      <div class="grid gap-8 lg:grid-cols-3">
        <!-- Main Content -->
        <div class="lg:col-span-2 space-y-6">
          
          <!-- Patient Selection Section -->
          <div class="mb-8 rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
            <h2 class="mb-4 text-xl font-bold text-secondary-900">Seleccionar Paciente</h2>
            <div class="grid gap-4 sm:grid-cols-2">
              <div class="relative">
                <label for="patient" class="block text-sm font-medium text-secondary-900">
                  Paciente <span class="text-danger-600">*</span>
                </label>
                <input
                  v-model="searchQuery"
                  v-on:keyup="handleInput"
                  v-on:blur="closeList"
                  placeholder="Buscar..."
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                  required
                >
                <ul v-if="patients.length > 0" class="absolute z-10 mt-1 w-full bg-white border border-secondary-300 rounded-lg shadow-lg max-h-60 overflow-auto">
                    <li 
                    v-for="item in patients" 
                    v-bind="item.patient.patient_id"
                    v-on:mousedown="selectPatient(item)"
                    class="px-4 py-2 hover:bg-primary-50 cursor-pointer border-b last:border-none"
                    >
                    <div class="font-medium text-secondary-900">
                        {{ item.patient.user.first_name }} {{ item.patient.user.last_name }}
                    </div>
                    <div class="text-xs text-secondary-500">
                        ID: {{ item.patient.user.id_number }} | {{ item.patient.occupation }}
                    </div>
                    </li>
                </ul>
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900 invisible">Doctor</label>
                <div class="mt-2 flex items-center gap-2 rounded-lg bg-primary-50 px-4 py-2.5 border border-primary-200">
                  <svg class="h-5 w-5 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                  </svg>
                  <span class="font-medium text-primary-900">Dr. {{ user?.last_name }} (Current User)</span>
                </div>
              </div>
            </div>
          </div>
          <!-- Patient Info Card -->
          <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
            <h2 class="mb-4 text-xl font-bold text-secondary-900">Información del Paciente</h2>
            <div class="space-y-4">
              <div v-if="selectedPatient" class="grid grid-cols-2 gap-4 sm:grid-cols-3">
                <div>
                  <p class="text-xs font-medium text-secondary-600">Nombre Completo</p>
                  <p class="mt-1 font-semibold text-secondary-900">{{ selectedPatient?.patient.user.first_name }} {{ selectedPatient?.patient.user.last_name }}</p>
                </div>
                <div>
                  <p class="text-xs font-medium text-secondary-600">ID</p>
                  <p class="mt-1 font-semibold text-secondary-900">{{ selectedPatient?.patient.user.id_number }}</p>
                </div>
                <div>
                  <p class="text-xs font-medium text-secondary-600">Edad</p>
                  <p class="mt-1 font-semibold text-secondary-900">{{ selectedPatient?.patient.age }}</p>
                </div>
              </div>
              <div v-else class="grid grid-cols-2 gap-4 sm:grid-cols-3">
                <div>
                  <p class="text-xs font-medium text-secondary-600">Nombre Completo</p>
                  <p class="mt-1 font-semibold text-secondary-900"> ---------- </p>
                </div>
                <div>
                  <p class="text-xs font-medium text-secondary-600">ID</p>
                  <p class="mt-1 font-semibold text-secondary-900"> ---------- </p>
                </div>
                <div>
                  <p class="text-xs font-medium text-secondary-600">Edad</p>
                  <p class="mt-1 font-semibold text-secondary-900"> ---------- </p>
                </div>
              </div>
            </div>
          </div>

          <!-- Add History Section -->
          <div v-if="histories.length == 0"  class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
            <h2 class="mb-4 text-xl font-bold text-secondary-900">Agregar Historial Médico</h2>
            <div class="rounded-lg bg-secondary-50 p-8 text-center">
              <svg class="mx-auto h-16 w-16 text-secondary-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
              <p class="mt-4 font-semibold text-secondary-900">Formulario de Historial Médico</p>
              <button
                class="mt-6 rounded-lg bg-primary-600 px-6 py-2 text-sm font-semibold text-white transition-colors hover:bg-primary-700"
              >
                Próximas características
              </button>
            </div>
          </div>
          <div v-else class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
            <table class="min-w-full border border-secondary-200 rounded-lg overflow-hidden">
              <thead class="bg-secondary-100">
                <tr>
                  <th class="px-4 py-2 text-left text-sm font-semibold">ID</th>
                  <th class="px-4 py-2 text-left text-sm font-semibold">Paciente</th>
                  <th class="px-4 py-2 text-left text-sm font-semibold">Fecha</th>
                  <th class="px-4 py-2"></th>
                </tr>
              </thead>

              <tbody>
                <template v-for="history in histories" :key="history.history_id">
                  
                  <!-- Fila principal -->
                  <tr class="border-t hover:bg-secondary-50">
                    <td class="px-4 py-2">{{ history.history_id }}</td>

                    <td class="px-4 py-2">
                      {{ selectedPatient.patient.user.first_name }}
                      {{ selectedPatient.patient.user.last_name }}
                    </td>

                    <td class="px-4 py-2">
                      {{ formatDate(history.issue_date) }}
                    </td>

                    <td class="px-4 py-2 text-right">
                      <button
                        @click="toggleHistory(history.history_id)"
                        class="bg-primary-600 text-white px-3 py-1 rounded"
                      >
                        {{ expandedHistoryId === history.history_id ? 'Ocultar' : 'Ver' }}
                      </button>
                    </td>
                  </tr>

                  <!-- Fila expandida -->
                  <tr v-if="expandedHistoryId === history.history_id">
                    <td colspan="4" class="bg-secondary-50 px-4 py-4 border-t">
                      
                      <!-- Contenido expandido -->
                      <div class="grid grid-cols-1 gap-4 text-sm">
                        <div>
                          <p class="font-semibold text-secondary-700">Motivo de consulta</p>
                          <p class="text-secondary-900">{{ history.consultation_reason }}</p>
                        </div>
                        <div>
                          <p class="font-semibold text-secondary-700">Enfermedad</p>
                          <p class="text-secondary-900">{{ history.current_illness }}</p>
                        </div>
                        <div>
                          <p class="font-semibold text-secondary-700">Diagnóstico</p>
                          <p>{{ history.diagnosis }}</p>
                        </div>
                        <div>
                          <p class="font-semibold text-secondary-700">Evolución</p>
                          <p>{{ history.patient_progress }}</p>
                        </div>
                      </div>
                      
                    </td>
                  </tr>

                </template>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Sidebar -->
        <div class="space-y-6">
          <!-- Quick Actions -->
          <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
            <h3 class="mb-4 text-lg font-semibold text-secondary-900">Acciones Rápidas</h3>
            <div class="space-y-3">
              <button
                @click="$router.push('/add-patient')"
                class="w-full rounded-lg bg-primary-50 px-4 py-3 text-left text-sm font-medium text-primary-700 transition-colors hover:bg-primary-100"
              >
                <div class="flex items-center gap-3">
                  <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                  </svg>
                  Nuevo Paciente
                </div>
              </button>
              <button
                @click="$router.push('/dashboard')"
                class="w-full rounded-lg bg-blue-50 px-4 py-3 text-left text-sm font-medium text-blue-700 transition-colors hover:bg-blue-100"
              >
                <div class="flex items-center gap-3">
                  <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-3m0 0l7-4 7 4M5 7v10a1 1 0 001 1h12a1 1 0 001-1V7m0 0l-4 2.25M9 21h6m-6 0v-4m0 4H3m18 0h3" />
                  </svg>
                  Nueva Historia
                </div>
              </button>
              <button
                @click="$router.push('/dashboard')"
                class="w-full rounded-lg bg-secondary-50 px-4 py-3 text-left text-sm font-medium text-secondary-700 transition-colors hover:bg-secondary-100"
              >
                <div class="flex items-center gap-3">
                  <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.856-1.487M15 10h.01M11 10h.01M7 10h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                  Ir al Panel
                </div>
              </button>
            </div>
          </div>

          <!-- Info Card -->
          <div class="rounded-lg bg-primary-50 p-6 border border-primary-200">
            <h3 class="font-semibold text-primary-900">Próximos Pasos</h3>
            <p class="mt-2 text-sm text-primary-700">
              Puedes agregar más datos al paciente, incluyendo:
            </p>
            <ul class="mt-3 space-y-2 text-sm text-primary-700">
              <li>✓ Historial médico detallado</li>
              <li>✓ Consultas y citas</li>
              <li>✓ Prescripciones</li>
              <li>✓ Pruebas y diagnósticos</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { ref, computed, watch } from 'vue'
import { user } from '../store/auth'
import axios from 'axios'

const router = useRouter()
const isLoading = ref(false)
let debounceTimer: ReturnType<typeof setTimeout> | null = null;

const patients = ref<any[]>([]);
const selectedPatient = ref<any>(null);
const histories = ref<any[]>([]);
const selectedHistory = ref<any>(null);

const isSelecting = ref(false)
const searchQuery = ref('')
const expandedHistoryId = ref(null)

const errorMessage = ref('')
const successMessage = ref('')

console.log(histories)

const searchPatient = async () => {
  if (isSelecting.value || !searchQuery.value.trim()) {
    patients.value = [];
    return;
  }
          
  if (searchQuery.value.length > 2){
    const response = await axios.get(`http://127.0.0.1:8000/registers/`, {
      params: { search: searchQuery.value}
    });
    patients.value = response.data;
  }
  else {
    return;
  }
}

const selectPatient = async (item: any) => {
  isSelecting.value = true; // Bloqueamos la búsqueda

  selectedPatient.value = item
  searchQuery.value = `${item.patient.user.first_name} ${item.patient.user.last_name}`;
  patients.value = []; // Limpia la lista

  const responseHistories = await axios.get(`http://127.0.0.1:8000/histories/get_all`, {
    params: { patient_id: selectedPatient.value.patient.patient_id }
  });
  histories.value = responseHistories.data;

  setTimeout(() => {
    isSelecting.value = false;
  }, 100);
}

const handleInput = () => {
  // Si ya hay un temporizador corriendo, lo cancelamos
  if (debounceTimer) clearTimeout(debounceTimer);
  // Creamos un nuevo temporizador de 400ms
  debounceTimer = setTimeout(() => {
    searchPatient();
  }, 400);
};

const formatDate = (date:any) => {
  return new Date(date).toLocaleDateString()
}

const toggleHistory = (id:any) => {
  expandedHistoryId.value =
    expandedHistoryId.value === id ? null : id
}

const closeList = () => {
  setTimeout(() => {
    patients.value = [];
  }, 200); // Pequeño retraso para permitir que el mousedown se procese
};

watch(searchQuery, (newVal) => {
    if (newVal === '') {
        patients.value = [];
        selectedPatient.value = "";
        histories.value =[];
        console.log(histories.value)
    }
})
</script>
