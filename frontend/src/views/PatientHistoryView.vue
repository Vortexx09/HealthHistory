<template>
  <div class="min-h-screen bg-secondary-50">
    <!-- Header -->
    <div class="border-b border-secondary-200 bg-white shadow-sm">
      <div class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <div class="flex items-center gap-4">
          <button @click="$router.back()" class="rounded-lg p-2 hover:bg-secondary-100 transition-colors">
            <svg class="h-6 w-6 text-secondary-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
            </svg>
          </button>
          <div>
            <h1 class="text-3xl font-bold text-secondary-900">Historial del Paciente</h1>
            <p class="mt-1 text-secondary-600">Buscar paciente por número de identificación</p>
          </div>
        </div>
      </div>
    </div>

    <div class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8 space-y-6">

      <!-- Search Bar -->
      <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
        <h2 class="mb-4 text-lg font-semibold text-secondary-900">Buscar Paciente</h2>
        <div class="flex gap-3">
          <input
            v-model="searchId"
            type="text"
            placeholder="Número de identificación..."
            class="flex-1 rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 transition-colors"
            @keyup.enter="searchPatient"
          />
          <button
            @click="searchPatient"
            :disabled="isSearching || !searchId"
            class="rounded-lg bg-primary-600 px-6 py-2.5 font-semibold text-white transition-colors hover:bg-primary-700 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <span v-if="!isSearching">Buscar</span>
            <span v-else>Buscando...</span>
          </button>
        </div>
        <p v-if="searchError" class="mt-3 text-sm text-danger-600">{{ searchError }}</p>
      </div>

      <!-- Results (only shown after search) -->
      <div v-if="patient" class="grid gap-8 lg:grid-cols-3">

        <!-- Main Content -->
        <div class="lg:col-span-2 space-y-6">

          <!-- Patient Info Card -->
          <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
            <h2 class="mb-4 text-xl font-bold text-secondary-900">Información del Paciente</h2>
            <div class="grid grid-cols-2 gap-4 sm:grid-cols-3">
              <div>
                <p class="text-xs font-medium text-secondary-600">Nombre Completo</p>
                <p class="mt-1 font-semibold text-secondary-900">
                  {{ patient.user.first_name }} {{ patient.user.last_name }}
                </p>
              </div>
              <div>
                <p class="text-xs font-medium text-secondary-600">Número de ID</p>
                <p class="mt-1 font-semibold text-secondary-900">{{ patient.user.id_number }}</p>
              </div>
              <div>
                <p class="text-xs font-medium text-secondary-600">Tipo de ID</p>
                <p class="mt-1 font-semibold text-secondary-900">{{ patient.user.id_type }}</p>
              </div>
              <div>
                <p class="text-xs font-medium text-secondary-600">Email</p>
                <p class="mt-1 font-semibold text-secondary-900">{{ patient.user.email }}</p>
              </div>
              <div>
                <p class="text-xs font-medium text-secondary-600">Teléfono</p>
                <p class="mt-1 font-semibold text-secondary-900">{{ patient.user.phone }}</p>
              </div>
              <div>
                <p class="text-xs font-medium text-secondary-600">Sexo</p>
                <p class="mt-1 font-semibold text-secondary-900">{{ patient.sex_code }}</p>
              </div>
              <div>
                <p class="text-xs font-medium text-secondary-600">Dirección</p>
                <p class="mt-1 font-semibold text-secondary-900">{{ patient.address }}</p>
              </div>
              <div>
                <p class="text-xs font-medium text-secondary-600">Fecha de Nacimiento</p>
                <p class="mt-1 font-semibold text-secondary-900">{{ patient.user.dob || '--' }}</p>
              </div>
            </div>
          </div>

          <!-- Register Details Toggle -->
          <div v-if="register" class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
            <div class="flex items-center justify-between mb-4">
              <h2 class="text-xl font-bold text-secondary-900">Datos del Registro</h2>
              <button
                @click="showRegisterDetails = !showRegisterDetails"
                class="rounded-lg border border-secondary-300 px-4 py-2 text-sm font-medium text-secondary-700 transition-colors hover:bg-secondary-50"
              >
                {{ showRegisterDetails ? 'Ocultar' : 'Ver detalles' }}
              </button>
            </div>
            <div v-if="showRegisterDetails" class="grid grid-cols-2 gap-4 sm:grid-cols-3">
              <div>
                <p class="text-xs font-medium text-secondary-600">Ocupación</p>
                <p class="mt-1 font-semibold text-secondary-900">{{ register.occupation || '--' }}</p>
              </div>
              <div>
                <p class="text-xs font-medium text-secondary-600">Estado Civil</p>
                <p class="mt-1 font-semibold text-secondary-900">{{ register.civil_status || '--' }}</p>
              </div>
              <div>
                <p class="text-xs font-medium text-secondary-600">Discapacidad</p>
                <p class="mt-1 font-semibold text-secondary-900">{{ register.disability || '--' }}</p>
              </div>
              <div>
                <p class="text-xs font-medium text-secondary-600">Diabetes</p>
                <p class="mt-1 font-semibold text-secondary-900">{{ register.diabetes ? 'Sí' : 'No' }}</p>
              </div>
              <div>
                <p class="text-xs font-medium text-secondary-600">Cáncer</p>
                <p class="mt-1 font-semibold text-secondary-900">{{ register.cancer ? 'Sí' : 'No' }}</p>
              </div>
              <div>
                <p class="text-xs font-medium text-secondary-600">Fumador</p>
                <p class="mt-1 font-semibold text-secondary-900">{{ register.smoker ? 'Sí' : 'No' }}</p>
              </div>
              <div>
                <p class="text-xs font-medium text-secondary-600">Consumo de Alcohol</p>
                <p class="mt-1 font-semibold text-secondary-900">{{ register.alcohol_consumption ? 'Sí' : 'No' }}</p>
              </div>
              <div>
                <p class="text-xs font-medium text-secondary-600">Uso de Drogas</p>
                <p class="mt-1 font-semibold text-secondary-900">{{ register.drug_use ? 'Sí' : 'No' }}</p>
              </div>
              <div>
                <p class="text-xs font-medium text-secondary-600">Riesgo Ocupacional</p>
                <p class="mt-1 font-semibold text-secondary-900">{{ register.occupational_risk || '--' }}</p>
              </div>
            </div>
          </div>

          <!-- History Section -->
          <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
            <div class="flex items-center justify-between mb-4">
              <h2 class="text-xl font-bold text-secondary-900">Agregar Historial Médico</h2>
              <button
                @click="showHistoryForm = !showHistoryForm"
                class="rounded-lg bg-primary-600 px-6 py-2 text-sm font-semibold text-white transition-colors hover:bg-primary-700"
              >
                {{ showHistoryForm ? 'Cancelar' : 'Nueva Consulta' }}
              </button>
            </div>
            
            <!-- Success/Error messages -->
            <div v-if="historySuccess" class="mb-4 rounded-lg bg-success-50 p-4 text-sm text-success-600 border border-success-200">
              {{ historySuccess }}
            </div>
            <div v-if="historyError" class="mb-4 rounded-lg bg-danger-50 p-4 text-sm text-danger-600 border border-danger-200">
              {{ historyError }}
            </div>

            <form v-if="showHistoryForm" @submit.prevent="submitHistory" class="space-y-8">
              <!-- Consultation -->
             <div>
              <h3 class="text-lg font-semibold text-secondary-900 mb-4 pb-2 border-b border-secondary-200">Motivo de Consulta</h3>
              <div class="space-y-4">
                <div class="grid gap-4 sm:grid-cols-2">
                <div>
                  <label class="block text-sm font-medium text-secondary-900">Causa de Consulta</label>
                  <input v-model="historyForm.cause_consultation" type="text" maxlength="2"
                    class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
                </div>
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Motivo de Consulta <span class="text-danger-600">*</span></label>
                <textarea v-model="historyForm.reason_consultation" rows="3" required
                class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Enfermedad Actual</label>
                <textarea v-model="historyForm.actual_disease" rows="3"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
            </div>
          </div>

          <!-- Vital Signs -->
          <div>
            <h3 class="text-lg font-semibold text-secondary-900 mb-4 pb-2 border-b border-secondary-200">Signos Vitales</h3>
            <div class="grid gap-4 sm:grid-cols-3">
              <div>
                <label class="block text-sm font-medium text-secondary-900">Edad <span class="text-danger-600">*</span></label>
                <input v-model="historyForm.age" type="number" min="0" max="100" required
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Peso (kg) <span class="text-danger-600">*</span></label>
                <input v-model="historyForm.weight" type="number" step="0.1" min="0.1" max="200" required
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Altura (m) <span class="text-danger-600">*</span></label>
                <input v-model="historyForm.height" type="number" step="0.01" min="0.5" max="3" required
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Frecuencia Cardíaca <span class="text-danger-600">*</span></label>
                <input v-model="historyForm.heart_rate" type="number" min="20" max="220" required
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Frecuencia Respiratoria <span class="text-danger-600">*</span></label>
                <input v-model="historyForm.respiratory_rate" type="number" min="12" max="25" required
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
            </div>
          </div>

          <!-- Clinical Findings -->
          <div>
            <h3 class="text-lg font-semibold text-secondary-900 mb-4 pb-2 border-b border-secondary-200">Hallazgos Clínicos</h3>
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-secondary-900">Examen Físico</label>
                <textarea v-model="historyForm.physical_examination" rows="3"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Hallazgos Clave</label>
                <textarea v-model="historyForm.key_findings" rows="3"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
            </div>
          </div>
          
          <!-- Diagnostics -->
          <div>
            <h3 class="text-lg font-semibold text-secondary-900 mb-4 pb-2 border-b border-secondary-200">Diagnósticos</h3>
            <div class="space-y-4">
              <div class="grid gap-4 sm:grid-cols-2">
                <div>
                  <label class="block text-sm font-medium text-secondary-900">Diagnóstico Principal</label>
                  <input v-model="historyForm.main_diagnostic" type="text"
                    class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
                </div>
                <div>
                  <label class="block text-sm font-medium text-secondary-900">Código Diagnóstico Principal</label>
                  <input v-model="historyForm.main_diagnostic_code" type="text" maxlength="25"
                    class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
                </div>
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Diagnóstico Diferencial</label>
                <textarea v-model="historyForm.differential_diagnostic" rows="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div class="grid gap-4 sm:grid-cols-3">
                <div>
                  <label class="block text-sm font-medium text-secondary-900">Código Dx Secundario</label>
                  <input v-model="historyForm.secondary_diagnostic_code" type="text" maxlength="25"
                    class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
                </div>
                <div>
                  <label class="block text-sm font-medium text-secondary-900">Código Dx Tercero</label>
                  <input v-model="historyForm.third_diagnostic_code" type="text" maxlength="25"
                    class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
                </div>
                <div>
                  <label class="block text-sm font-medium text-secondary-900">Código Dx Cuarto</label>
                  <input v-model="historyForm.fourth_diagnostic_code" type="text" maxlength="25"
                    class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
                </div>
              </div>
            </div>
          </div>

          <!-- Medical Background -->
          <div>
            <h3 class="text-lg font-semibold text-secondary-900 mb-4 pb-2 border-b border-secondary-200">Antecedentes Médicos</h3>
            <div class="grid gap-4 sm:grid-cols-2">
              <div>
                <label class="block text-sm font-medium text-secondary-900">Enfermedades Previas</label>
                <textarea v-model="historyForm.previous_diseases" rows="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Cirugías Previas</label>
                <textarea v-model="historyForm.previous_surgeries" rows="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Hospitalizaciones</label>
                <textarea v-model="historyForm.hospitalization" rows="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Alergias</label>
                <textarea v-model="historyForm.allergies" rows="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Medicamentos</label>
                <textarea v-model="historyForm.medicines" rows="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Inmunización</label>
                <textarea v-model="historyForm.immunization" rows="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
            </div>
          </div>

          <!-- Specific Background -->
          <div>
            <h3 class="text-lg font-semibold text-secondary-900 mb-4 pb-2 border-b border-secondary-200">Antecedentes Específicos</h3>
            <div class="grid gap-4 sm:grid-cols-2">
              <div>
                <label class="block text-sm font-medium text-secondary-900">Condiciones Ginecológicas</label>
                <textarea v-model="historyForm.gynecologic_conditions" rows="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Condiciones Obstétricas</label>
                <textarea v-model="historyForm.obstetric_conditions" rows="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Condiciones Psiquiátricas</label>
                <textarea v-model="historyForm.psychiatric_conditions" rows="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Enfermedades Genéticas</label>
                <textarea v-model="historyForm.genetic_diseases" rows="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Enfermedades Vasculares</label>
                <textarea v-model="historyForm.vascular_diseases" rows="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
            </div>
          </div>

          <!-- Follow Up -->
          <div>
            <h3 class="text-lg font-semibold text-secondary-900 mb-4 pb-2 border-b border-secondary-200">Seguimiento</h3>
            <div class="grid gap-4 sm:grid-cols-2">
              <div>
                <label class="block text-sm font-medium text-secondary-900">Exámenes Solicitados</label>
                <textarea v-model="historyForm.requested_exams" rows="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Procedimientos Programados</label>
                <textarea v-model="historyForm.programmed_procedures" rows="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Interconsulta</label>
                <textarea v-model="historyForm.interconsultation" rows="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Recomendaciones de Seguimiento</label>
                <textarea v-model="historyForm.follow_up_recommendations" rows="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Plan de Seguimiento</label>
                <textarea v-model="historyForm.follow_up_plan" rows="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Detalles de Prescripción</label>
                <textarea v-model="historyForm.prescription_details" rows="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
            </div>
          </div>

          <!-- Administrative -->
          <div>
            <h3 class="text-lg font-semibold text-secondary-900 mb-4 pb-2 border-b border-secondary-200">Información Administrativa</h3>
            <div class="grid gap-4 sm:grid-cols-3">
              <div>
                <label class="block text-sm font-medium text-secondary-900">Costo del Servicio</label>
                <input v-model="historyForm.service_cost" type="number" step="0.01"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Concepto de Ingreso</label>
                <input v-model="historyForm.income_concept" type="text" maxlength="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Valor de Pago</label>
                <input v-model="historyForm.payment_value" type="number" step="0.01"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Número FEV</label>
                <input v-model="historyForm.fev_number" type="text" maxlength="2"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div>
                <label class="block text-sm font-medium text-secondary-900">Discapacidad</label>
                <input v-model="historyForm.disability" type="text"
                  class="mt-1 w-full rounded-lg border border-secondary-300 px-4 py-2.5 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
              </div>
              <div class="flex items-center gap-3 mt-6">
                <input v-model="historyForm.send_email" type="checkbox"
                  class="h-4 w-4 rounded border-secondary-300 text-primary-600 focus:ring-2 focus:ring-primary-500" />
                <label class="text-sm font-medium text-secondary-900">Enviar resumen por email</label>
              </div>
            </div>
          </div>

          <!-- Submit -->
          <div class="flex justify-end gap-4 pt-4 border-t border-secondary-200">
            <button
              type="button"
              @click="showHistoryForm = false"
              class="rounded-lg border border-secondary-300 px-6 py-3 font-semibold text-secondary-700 transition-colors hover:bg-secondary-50"
            >
              Cancelar
            </button>
            <button
              type="submit"
              :disabled="isSubmittingHistory"
              class="rounded-lg bg-primary-600 px-6 py-3 font-semibold text-white transition-colors hover:bg-primary-700 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <span v-if="!isSubmittingHistory">Guardar Historial</span>
              <span v-else>Guardando...</span>
            </button>
          </div>
            
            </form>

          </div>
        </div>

      <!-- Past History Records -->
      <div v-if="histories.length > 0" class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
        <h2 class="mb-4 text-xl font-bold text-secondary-900">Historial de Consultas</h2>
        <div class="space-y-4">
          <div
            v-for="record in histories"
            :key="record.history_id"
            class="rounded-lg border border-secondary-200 p-4"
          >
            <!-- Summary Row -->
            <div class="flex items-center justify-between">
              <div>
                <p class="text-xs text-secondary-500">
                  {{ new Date(record.created_at).toLocaleDateString('es-CO', { 
                    year: 'numeric', month: 'long', day: 'numeric' 
                  }) }}
                </p>
                <p class="font-semibold text-secondary-900">{{ record.reason_consultation }}</p>
                <p class="text-sm text-secondary-600">{{ record.main_diagnostic || 'Sin diagnóstico registrado' }}</p>
              </div>
              <button
                @click="record._expanded = !record._expanded"
                class="rounded-lg border border-secondary-300 px-3 py-1 text-sm font-medium text-secondary-700 transition-colors hover:bg-secondary-50"
              >
                {{ record._expanded ? 'Ocultar' : 'Ver detalles' }}
              </button>
            </div>

      <!-- Expanded Details -->
      <div v-if="record._expanded" class="mt-4 grid gap-4 sm:grid-cols-2 border-t border-secondary-100 pt-4">
        <div>
          <p class="text-xs font-medium text-secondary-600">Enfermedad Actual</p>
          <p class="mt-1 text-secondary-900">{{ record.actual_disease || '--' }}</p>
        </div>
        <div>
          <p class="text-xs font-medium text-secondary-600">Hallazgos Clave</p>
          <p class="mt-1 text-secondary-900">{{ record.key_findings || '--' }}</p>
        </div>
        <div>
          <p class="text-xs font-medium text-secondary-600">Edad</p>
          <p class="mt-1 text-secondary-900">{{ record.age }}</p>
        </div>
        <div>
          <p class="text-xs font-medium text-secondary-600">Peso / Altura</p>
          <p class="mt-1 text-secondary-900">{{ record.weight }}kg / {{ record.height }}m</p>
        </div>
        <div>
          <p class="text-xs font-medium text-secondary-600">Frecuencia Cardíaca</p>
          <p class="mt-1 text-secondary-900">{{ record.heart_rate }} bpm</p>
        </div>
        <div>
          <p class="text-xs font-medium text-secondary-600">Frecuencia Respiratoria</p>
          <p class="mt-1 text-secondary-900">{{ record.respiratory_rate }} rpm</p>
        </div>
        <div>
          <p class="text-xs font-medium text-secondary-600">Diagnóstico Principal</p>
          <p class="mt-1 text-secondary-900">{{ record.main_diagnostic || '--' }}</p>
        </div>
        <div>
          <p class="text-xs font-medium text-secondary-600">Código Diagnóstico</p>
          <p class="mt-1 text-secondary-900">{{ record.main_diagnostic_code || '--' }}</p>
        </div>
        <div>
          <p class="text-xs font-medium text-secondary-600">Prescripción</p>
          <p class="mt-1 text-secondary-900">{{ record.prescription_details || '--' }}</p>
        </div>
        <div>
          <p class="text-xs font-medium text-secondary-600">Plan de Seguimiento</p>
          <p class="mt-1 text-secondary-900">{{ record.follow_up_plan || '--' }}</p>
        </div>
      </div>
    </div>
  </div>
</div>

<div v-else-if="patient && !isSearching" class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
  <p class="text-center text-secondary-600">No hay consultas previas registradas para este paciente.</p>
</div>

        <!-- Sidebar -->
        <div class="space-y-6">
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
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-3m0 0l7-4 7 4M5 7v10a1 1 0 001 1h12a1 1 0 001-1V7" />
                  </svg>
                  Ir al Panel
                </div>
              </button>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { user } from '../store/auth'
import api from '../api'

const router = useRouter()

// Search
const searchId = ref('')
const isSearching = ref(false)
const searchError = ref('')

// Patient data
const patient = ref<any>(null)
const register = ref<any>(null)
const showRegisterDetails = ref(false)
const histories = ref<any[]>([])

// History form
const isSubmittingHistory = ref(false)
const historySuccess = ref('')
const historyError = ref('')
const showHistoryForm = ref(false)

const historyForm = ref({
  reason_consultation: '',
  cause_consultation: '',
  actual_disease: '',
  age: '',
  weight: '',
  height: '',
  heart_rate: '',
  respiratory_rate: '',
  physical_examination: '',
  key_findings: '',
  main_diagnostic: '',
  main_diagnostic_code: '',
  differential_diagnostic: '',
  secondary_diagnostic_code: '',
  third_diagnostic_code: '',
  fourth_diagnostic_code: '',
  previous_diseases: '',
  previous_surgeries: '',
  hospitalization: '',
  allergies: '',
  medicines: '',
  immunization: '',
  gynecologic_conditions: '',
  obstetric_conditions: '',
  psychiatric_conditions: '',
  genetic_diseases: '',
  vascular_diseases: '',
  requested_exams: '',
  programmed_procedures: '',
  interconsultation: '',
  follow_up_recommendations: '',
  follow_up_plan: '',
  prescription_details: '',
  service_cost: '',
  income_concept: '',
  payment_value: '',
  fev_number: '',
  disability: '',
  send_email: false,
})

const searchPatient = async () => {
  try {
    isSearching.value = true
    searchError.value = ''
    patient.value = null
    register.value = null
    histories.value = []
    showHistoryForm.value = false
    historySuccess.value = ''

    const patientRes = await api.get(`/patients/?id_number=${searchId.value}`)

    if (patientRes.data.length === 0) {
      searchError.value = 'No se encontró ningún paciente con ese número de identificación.'
      return
    }

    patient.value = patientRes.data[0]

    try {
      const registerRes = await api.get(`/registers/${patient.value.patient_id}/`)
      register.value = registerRes.data

      const historiesRes = await api.get(`/histories/?register=${register.value.register_id}`)
      histories.value = historiesRes.data.sort((a: any, b: any) =>
        new Date(b.created_at).getTime() - new Date(a.created_at).getTime()
      )
    } catch {
      register.value = null
      histories.value = []
    }

  } catch (error: any) {
    searchError.value = 'Error al buscar el paciente. Por favor intenta de nuevo.'
  } finally {
    isSearching.value = false
  }
}

const submitHistory = async () => {
  try {
    isSubmittingHistory.value = true
    historyError.value = ''
    historySuccess.value = ''

    // Get the doctor_id for the logged-in user
    const doctorRes = await api.get(`/doctors/?user_id=${user.value?.id}`)

    if (doctorRes.data.length === 0) {
      historyError.value = 'No se encontró un perfil de doctor para este usuario.'
      return
    }

    const doctorId = doctorRes.data[0].doctor_id
    const registerId = register.value.register_id

    await api.post('/histories/', {
      doctor: doctorId,
      register: registerId,
      ...historyForm.value,
      age: Number(historyForm.value.age),
      weight: Number(historyForm.value.weight),
      height: Number(historyForm.value.height),
      heart_rate: Number(historyForm.value.heart_rate),
      respiratory_rate: Number(historyForm.value.respiratory_rate),
      service_cost: historyForm.value.service_cost || null,
      payment_value: historyForm.value.payment_value || null,
    })

    historySuccess.value = '¡Historial médico guardado exitosamente!'
    showHistoryForm.value = false

  } catch (error: any) {
    historyError.value = error.response?.data?.detail || 'Error al guardar el historial.'
  } finally {
    isSubmittingHistory.value = false
  }
}


</script>