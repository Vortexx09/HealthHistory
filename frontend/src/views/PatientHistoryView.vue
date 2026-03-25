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
            <h1 class="text-3xl font-bold text-secondary-900">Historial del Paciente</h1>
            <p class="mt-1 text-secondary-600">Gestionar historial médico y citas</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Success Alert -->
    <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
      <div class="rounded-lg bg-success-50 p-6 border border-success-200">
        <div class="flex items-center gap-4">
          <div class="flex h-12 w-12 items-center justify-center rounded-full bg-success-100">
            <svg class="h-6 w-6 text-success-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <div>
            <h3 class="font-semibold text-success-900">¡Paciente agregado exitosamente!</h3>
            <p class="text-success-700">El paciente ha sido registrado en el sistema</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Content -->
    <div class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
      <div class="grid gap-8 lg:grid-cols-3">
        <!-- Main Content -->
        <div class="lg:col-span-2 space-y-6">
          <!-- Patient Info Card -->
          <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
            <h2 class="mb-4 text-xl font-bold text-secondary-900">Información del Paciente</h2>
            <div class="space-y-4">
              <div class="grid grid-cols-2 gap-4 sm:grid-cols-3">
                <div>
                  <p class="text-xs font-medium text-secondary-600">Nombre Completo</p>
                  <p class="mt-1 font-semibold text-secondary-900">Paciente Nuevo</p>
                </div>
                <div>
                  <p class="text-xs font-medium text-secondary-600">ID</p>
                  <p class="mt-1 font-semibold text-secondary-900">------</p>
                </div>
                <div>
                  <p class="text-xs font-medium text-secondary-600">Edad</p>
                  <p class="mt-1 font-semibold text-secondary-900">--</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Add History Section -->
          <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
            <h2 class="mb-4 text-xl font-bold text-secondary-900">Agregar Historial Médico</h2>
            <div class="rounded-lg bg-secondary-50 p-8 text-center">
              <svg class="mx-auto h-16 w-16 text-secondary-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
              <p class="mt-4 font-semibold text-secondary-900">Formulario de Historial Médico</p>
              <p class="mt-2 text-secondary-600">El formulario para agregar historial será desarrollado en la próxima etapa</p>
              <button
                @click="openHistoryForm"
                class="mt-6 rounded-lg bg-primary-600 px-6 py-2 text-sm font-semibold text-white transition-colors hover:bg-primary-700"
              >
                Próximas características
              </button>
            </div>
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
                  Ir al Panel
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
                  Ver Pacientes
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

const router = useRouter()

const openHistoryForm = () => {
  // Placeholder for future history form
  alert('El formulario de historial será desarrollado en la próxima etapa')
}
</script>
