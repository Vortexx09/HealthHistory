<template>
  <div class="min-h-screen bg-secondary-50">
    <!-- Header -->
    <div class="border-b border-secondary-200 bg-white shadow-sm">
      <div class="mx-auto max-w-6xl px-4 py-6 sm:px-6 lg:px-8">
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
            <h1 class="text-3xl font-bold text-secondary-900">Agregar Historia Médica</h1>
            <p class="mt-1 text-secondary-600">Registra el historial clínico del paciente</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="mx-auto max-w-6xl px-4 py-8 sm:px-6 lg:px-8">
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

      <!-- Patient Info Display Section -->
      <div v-if="selectedPatient && searchQuery" class="mb-8">
        <!-- Personal Data Display -->
        <div class="mb-6 rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
          <h3 class="mb-4 flex items-center gap-2 text-lg font-semibold text-secondary-900">
            <svg class="h-5 w-5 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            Datos Personales del Paciente
          </h3>
          <div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-5">
            <div class="rounded-lg bg-secondary-50 p-3">
              <p class="text-xs font-medium text-secondary-600">Nombre Completo</p>
              <p class="mt-1 font-semibold text-secondary-900">{{ selectedPatient.patient.user.first_name }} {{ selectedPatient.patient.user.last_name }}</p>
            </div>
            <div class="rounded-lg bg-secondary-50 p-3">
              <p class="text-xs font-medium text-secondary-600">ID</p>
              <p class="mt-1 font-semibold text-secondary-900">{{ selectedPatient.patient.user.id_number }}</p>
            </div>
            <div class="rounded-lg bg-secondary-50 p-3">
              <p class="text-xs font-medium text-secondary-600">Correo</p>
              <p class="mt-1 font-semibold text-secondary-900 text-sm">{{ selectedPatient.patient.user.email }}</p>
            </div>
            <div class="rounded-lg bg-secondary-50 p-3">
              <p class="text-xs font-medium text-secondary-600">Teléfono</p>
              <p class="mt-1 font-semibold text-secondary-900">{{ selectedPatient.patient.user.phone }}</p>
            </div>
            <div class="rounded-lg bg-secondary-50 p-3">
              <p class="text-xs font-medium text-secondary-600">Fecha de Nacimiento</p>
              <p class="mt-1 font-semibold text-secondary-900">{{ selectedPatient.patient.dob || 'N/A' }}</p>
            </div>
            <div class="rounded-lg bg-secondary-50 p-3">
              <p class="text-xs font-medium text-secondary-600">Sexo</p>
              <p class="mt-1 font-semibold text-secondary-900">{{ getSexLabel(selectedPatient.patient.sex_code) }}</p>
            </div>
            <div class="rounded-lg bg-secondary-50 p-3">
              <p class="text-xs font-medium text-secondary-600">Ocupación</p>
              <p class="mt-1 font-semibold text-secondary-900 text-sm">{{ selectedPatient.patient.occupation || 'N/A' }}</p>
            </div>
            <div class="rounded-lg bg-secondary-50 p-3">
              <p class="text-xs font-medium text-secondary-600">Dirección</p>
              <p class="mt-1 font-semibold text-secondary-900 text-sm">{{ selectedPatient.patient.address || 'N/A' }}</p>
            </div>
            <div class="rounded-lg bg-secondary-50 p-3">
              <p class="text-xs font-medium text-secondary-600">Estado Civil</p>
              <p class="mt-1 font-semibold text-secondary-900 text-sm">{{ selectedPatient.patient.civil_status || 'N/A' }}</p>
            </div>
            <div class="rounded-lg bg-secondary-50 p-3">
              <p class="text-xs font-medium text-secondary-600">Religión</p>
              <p class="mt-1 font-semibold text-secondary-900 text-sm">{{ selectedPatient.patient.religion || 'N/A' }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- History Form -->
      <form v-if="selectedPatient && searchQuery" @submit.prevent="handleSubmit" class="space-y-6">
        <!-- Consultation Information Section -->
        <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
          <h3 class="mb-4 flex items-center gap-2 text-lg font-semibold text-secondary-900">
            <svg class="h-5 w-5 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            Información de la Consulta
          </h3>
          <div class="space-y-4">
            <div>
              <label for="consultationReason" class="block text-sm font-medium text-secondary-900">
                Motivo de la Consulta <span class="text-danger-600">*</span>
              </label>
              <textarea
                id="consultationReason"
                v-model="form.consultation_reason"
                rows="3"
                required
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Describe el motivo principal de la consulta"
              />
            </div>
            <div>
              <label for="actualDisease" class="block text-sm font-medium text-secondary-900">
                Enfermedad Actual <span class="text-danger-600">*</span>
              </label>
              <textarea
                id="actualDisease"
                v-model="form.current_illness"
                rows="3"
                required
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Describe la enfermedad o condición actual del paciente"
              />
            </div>
          </div>
        </div>

        <!-- Medical Data Display -->
        <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200 space-y-4">
          <h3 class="mb-4 flex items-center gap-2 text-lg font-semibold text-secondary-900">
            <svg class="h-5 w-5 text-accent-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            Antecedentes Médicos
          </h3>
          <div class="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
            <div class="flex items-center gap-2 rounded-lg bg-secondary-50 p-3">
              <svg class="h-4 w-4" :class="selectedPatient.disability ? 'text-danger-600' : 'text-success-600'" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
              <span class="text-sm font-medium">Discapacidad: {{ selectedPatient.disability ? 'Sí' : 'No' }}</span>
            </div>
            <div class="flex items-center gap-2 rounded-lg bg-secondary-50 p-3">
              <svg class="h-4 w-4" :class="selectedPatient.diabetes ? 'text-danger-600' : 'text-success-600'" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
              <span class="text-sm font-medium">Diabetes: {{ selectedPatient.diabetes ? 'Sí' : 'No' }}</span>
            </div>
            <div class="flex items-center gap-2 rounded-lg bg-secondary-50 p-3">
              <svg class="h-4 w-4" :class="selectedPatient.cancer ? 'text-danger-600' : 'text-success-600'" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
              <span class="text-sm font-medium">Cáncer: {{ selectedPatient.cancer ? 'Sí' : 'No' }}</span>
            </div>
            <div class="flex items-center gap-2 rounded-lg bg-secondary-50 p-3">
              <svg class="h-4 w-4" :class="selectedPatient.alcohol_consumption ? 'text-danger-600' : 'text-success-600'" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
              <span class="text-sm font-medium">Alcohol: {{ selectedPatient.alcohol_consumption ? 'Sí' : 'No' }}</span>
            </div>
            <div class="flex items-center gap-2 rounded-lg bg-secondary-50 p-3">
              <svg class="h-4 w-4" :class="selectedPatient.smoker ? 'text-danger-600' : 'text-success-600'" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
              <span class="text-sm font-medium">Fumador: {{ selectedPatient.smoker ? 'Sí' : 'No' }}</span>
            </div>
            <div class="flex items-center gap-2 rounded-lg bg-secondary-50 p-3">
              <svg class="h-4 w-4" :class="selectedPatient.drug_use ? 'text-danger-600' : 'text-success-600'" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
              <span class="text-sm font-medium">Drogas: {{ selectedPatient.drug_use ? 'Sí' : 'No' }}</span>
            </div>
          </div>
          <!-- Family History -->
            <div>
              <label for="familyHistory" class="block text-sm font-medium text-secondary-900">
                Antecedentes Familiares
              </label>
              <textarea
                id="familyHistory"
                v-model="form.family_history"
                rows="4"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Describe cualquier antecedente familiar relevante..."
              />
              <p class="mt-1 text-xs text-secondary-600">Información sobre enfermedades hereditarias en su ambiente familiar</p>
            </div>
            
            <!-- Personal History -->
            <div>
              <label for="personalHistory" class="block text-sm font-medium text-secondary-900">
                Antecedentes Personales
              </label>
              <textarea
                id="personalHistory"
                v-model="form.personal_history"
                rows="4"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Describe cualquier antecedente personal relevante..."
              />
              <p class="mt-1 text-xs text-secondary-600">Información sobre enfermedades padecidas o propensas a contraer</p>
            </div>
        </div>

        <!-- System Check Section -->
        <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
          <h3 class="mb-4 flex items-center gap-2 text-lg font-semibold text-secondary-900">
            <svg class="h-5 w-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            Revisión por Sistemas
          </h3>
          <div class="grid gap-3 sm:grid-cols-2">
            <div>
              <label for="headSystem" class="block text-sm font-medium text-secondary-900">Cabeza</label>
              <input
                id="headSystem"
                v-model="form.head_system"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="eyesSystem" class="block text-sm font-medium text-secondary-900">Ojos</label>
              <input
                id="eyesSystem"
                v-model="form.eyes_system"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="otolaryngologySystem" class="block text-sm font-medium text-secondary-900">ORL</label>
              <input
                id="otolaryngologySystem"
                v-model="form.otolaryngology_system"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="neckSystem" class="block text-sm font-medium text-secondary-900">Cuello</label>
              <input
                id="neckSystem"
                v-model="form.neck_system"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="chestSystem" class="block text-sm font-medium text-secondary-900">Tórax</label>
              <input
                id="chestSystem"
                v-model="form.chest_system"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="cardiacSystem" class="block text-sm font-medium text-secondary-900">Cardíaco</label>
              <input
                id="cardiacSystem"
                v-model="form.cardiac_system"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="pulmonarySystem" class="block text-sm font-medium text-secondary-900">Pulmonar</label>
              <input
                id="pulmonarySystem"
                v-model="form.pulmonary_system"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="digestiveSystem" class="block text-sm font-medium text-secondary-900">Digestivo</label>
              <input
                id="digestiveSystem"
                v-model="form.digestive_system"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="genitourinarySystem" class="block text-sm font-medium text-secondary-900">Genitourinario</label>
              <input
                id="genitourinarySystem"
                v-model="form.genitourinary_system"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="centralNervousSystem" class="block text-sm font-medium text-secondary-900">SNC</label>
              <input
                id="centralNervousSystem"
                v-model="form.central_nervous_system"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="skinSystem" class="block text-sm font-medium text-secondary-900">Piel</label>
              <input
                id="skinSystem"
                v-model="form.skin_system"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="extremitiesSystem" class="block text-sm font-medium text-secondary-900">Extremidades</label>
              <input
                id="extremitiesSystem"
                v-model="form.extremities_system"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div class="sm:col-span-2">
              <label for="otherSystem" class="block text-sm font-medium text-secondary-900">Observaciones Generales</label>
              <textarea
                id="otherSystem"
                v-model="form.other_system"
                type="text"
                rows="3"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
          </div>
        </div>

        <!-- Vital Signs Section -->
        <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
          <h3 class="mb-4 flex items-center gap-2 text-lg font-semibold text-secondary-900">
            <svg class="h-5 w-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
            Signos Vitales
          </h3>
          <div class="space-y-4">
            <div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              <div>
                <label for="temperature" class="block text-sm font-medium text-secondary-900">
                  Temperatura (°C) <span class="text-danger-600">*</span>
                </label>
                <input
                  id="temperature"
                  v-model.number="form.temperature"
                  type="number"
                  step="0.1"
                  min="0"
                  max="100"
                  required
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                  placeholder="37.0"
                />
              </div>
              <div>
                <label for="heartRate" class="block text-sm font-medium text-secondary-900">
                  Frecuencia Cardíaca (lpm) <span class="text-danger-600">*</span>
                </label>
                <input
                  id="heartRate"
                  v-model.number="form.heart_rate"
                  type="number"
                  min="20"
                  max="220"
                  required
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                  placeholder="75"
                />
              </div>
              <div>
                <label for="respiratoryRate" class="block text-sm font-medium text-secondary-900">
                  Frecuencia Respiratoria <span class="text-danger-600">*</span>
                </label>
                <input
                  id="respiratoryRate"
                  v-model.number="form.respiratory_rate"
                  type="number"
                  min="12"
                  max="25"
                  required
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                  placeholder="16"
                />
              </div>
            </div>
            <div class="grid gap-4 sm:grid-cols-2">
              <div>
                <label for="systolicPressure" class="block text-sm font-medium text-secondary-900">
                  Presión Sistólica (mmHg)
                </label>
                <input
                  id="systolicPressure"
                  v-model.number="form.systolic_pressure"
                  type="number"
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                  placeholder="120"
                />
              </div>
              <div>
                <label for="diastolicPressure" class="block text-sm font-medium text-secondary-900">
                  Presión Diastólica (mmHg)
                </label>
                <input
                  id="diastolicPressure"
                  v-model.number="form.diastolic_pressure"
                  type="number"
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                  placeholder="80"
                />
              </div>
            </div>
            <div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
              <div>
                <label for="weight" class="block text-sm font-medium text-secondary-900">
                  Peso (kg) <span class="text-danger-600">*</span>
                </label>
                <input
                  id="weight"
                  v-model.number="form.weight"
                  type="number"
                  step="0.1"
                  min="0"
                  max="200"
                  required
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                  placeholder="70"
                />
              </div>
              <div>
                <label for="height" class="block text-sm font-medium text-secondary-900">
                  Altura (m) <span class="text-danger-600">*</span>
                </label>
                <input
                  id="height"
                  v-model.number="form.height"
                  type="number"
                  step="0.01"
                  min="0"
                  max="3"
                  required
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                  placeholder="1.75"
                />
              </div>
              <div>
                <label for="imc" class="block text-sm font-medium text-secondary-900">
                  IMC (kg/m²) <span class="text-danger-600">*</span>
                </label>
                <input
                  id="imc"
                  v-model.number="form.imc"
                  type="number"
                  step="0.1"
                  min="0"
                  max="200"
                  required
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                  placeholder="22.8"
                />
              </div>
              <div>
                <label for="abdominalPerimeter" class="block text-sm font-medium text-secondary-900">
                  Perímetro Abdominal (cm) <span class="text-danger-600">*</span>
                </label>
                <input
                  id="abdominalPerimeter"
                  v-model.number="form.abdominal_perimeter"
                  type="number"
                  step="0.1"
                  min="0"
                  max="200"
                  required
                  class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                  placeholder="85"
                />
              </div>
            </div>
            <div>
              <label for="headPerimeter" class="block text-sm font-medium text-secondary-900">
                Perímetro Cefálico (cm)
              </label>
              <input
                id="headPerimeter"
                v-model.number="form.head_perimeter"
                type="number"
                step="0.1"
                min="0"
                max="200"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="57"
              />
            </div>
          </div>
        </div>

        <!-- Physical Examination Section -->
        <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
          <h3 class="mb-4 flex items-center gap-2 text-lg font-semibold text-secondary-900">
            <svg class="h-5 w-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
            Examen Físico General
          </h3>
          <div class="grid gap-4 sm:grid-cols-2">
            <div>
              <label for="consciousnessStatus" class="block text-sm font-medium text-secondary-900">
                Estado de Conciencia
              </label>
              <input
                id="consciousnessState"
                v-model="form.consciousness_status"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="respiratoryStatus" class="block text-sm font-medium text-secondary-900">
                Estado Respiratorio
              </label>
              <input
                id="respiratoryStatus"
                v-model="form.respiratory_status"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="hydrationStatus" class="block text-sm font-medium text-secondary-900">
                Estado de Hidratación
              </label>
              <input
                id="hydrationStatus"
                v-model="form.hydration_status"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="generalStatus" class="block text-sm font-medium text-secondary-900">
                Estado General
              </label>
              <input
                id="generalStatus"
                v-model="form.general_status"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div class="sm:col-span-2">
              <label for="physicalExamination" class="block text-sm font-medium text-secondary-900">
                Observaciones Generales
              </label>
              <textarea
                id="physicalExamination"
                v-model="form.physical_examination"
                rows="3"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
          </div>
        </div>

        <!-- Key Findings Section -->
        <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
          <h3 class="mb-4 flex items-center gap-2 text-lg font-semibold text-secondary-900">
            <svg class="h-5 w-5 text-accent-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            Hallazgos Relevantes
          </h3>
          <div class="grid gap-3 sm:grid-cols-2">
            <div>
              <label for="headFindings" class="block text-sm font-medium text-secondary-900">Cabeza</label>
              <input
                id="headFindings"
                v-model="form.head_findings"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="eyesFindings" class="block text-sm font-medium text-secondary-900">Ojos</label>
              <input
                id="eyesFindings"
                v-model="form.eyes_findings"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="otolaryngologyFindings" class="block text-sm font-medium text-secondary-900">ORL</label>
              <input
                id="otolaryngologyFindings"
                v-model="form.otolaryngology_findings"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="mouthFindings" class="block text-sm font-medium text-secondary-900">Boca</label>
              <input
                id="mouthFindings"
                v-model="form.mouth_findings"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="neckFindings" class="block text-sm font-medium text-secondary-900">Cuello</label>
              <input
                id="neckFindings"
                v-model="form.neck_findings"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="chestFindings" class="block text-sm font-medium text-secondary-900">Tórax</label>
              <input
                id="chestFindings"
                v-model="form.chest_findings"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="abdominalFindings" class="block text-sm font-medium text-secondary-900">Abdomen</label>
              <input
                id="abdominalFindings"
                v-model="form.abdominal_findings"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="genitourinaryFindings" class="block text-sm font-medium text-secondary-900">Genitourinario</label>
              <input
                id="genitourinaryFindings"
                v-model="form.genitourinary_findings"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="centralNervousFindings" class="block text-sm font-medium text-secondary-900">SNC</label>
              <input
                id="centralNervousFindings"
                v-model="form.central_nervous_findings"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="skinFindings" class="block text-sm font-medium text-secondary-900">Piel</label>
              <input
                id="skinFindings"
                v-model="form.skin_findings"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="extremitiesFindings" class="block text-sm font-medium text-secondary-900">Extremidades</label>
              <input
                id="extremitiesFindings"
                v-model="form.extremities_findings"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div>
              <label for="mentalFindings" class="block text-sm font-medium text-secondary-900">Mental</label>
              <input
                id="mentalFindings"
                v-model="form.mental_findings"
                type="text"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
            <div class="sm:col-span-2">
              <label for="otherFindings" class="block text-sm font-medium text-secondary-900">Observaciones Generales</label>
              <textarea
                id="otherFindings"
                v-model="form.other_findings"
                type="text"
                rows="3"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Sin alteraciones"
              />
            </div>
          </div>
        </div>

        <!-- Analysis and Conduct Section -->
        <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
          <h3 class="mb-4 flex items-center gap-2 text-lg font-semibold text-secondary-900">
            <svg class="h-5 w-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
            Análisis y Conducta
          </h3>
          <div class="space-y-4">
            <div>
              <label for="diagnosis" class="block text-sm font-medium text-secondary-900">
                Diagnóstico <span class="text-danger-600">*</span>
              </label>
              <textarea
                id="diagnosis"
                v-model="form.diagnosis"
                rows="3"
                required
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Diagnóstico médico"
              />
            </div>
            <div>
              <label for="analysis" class="block text-sm font-medium text-secondary-900">
                Análisis <span class="text-danger-600">*</span>
              </label>
              <textarea
                id="analysis"
                v-model="form.analysis"
                rows="3"
                required
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Análisis clínico del paciente"
              />
            </div>
            <div>
              <label for="followUpPlan" class="block text-sm font-medium text-secondary-900">
                Plan de Seguimiento <span class="text-danger-600">*</span>
              </label>
              <textarea
                id="followUpPlan"
                v-model="form.follow_up_plan"
                rows="3"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Plan de seguimiento del paciente"
              />
            </div>
            <div>
              <label for="clinicalOrders" class="block text-sm font-medium text-secondary-900">
                Órdenes Clínicas
              </label>
              <textarea
                id="clinicalOrders"
                v-model="form.clinical_orders"
                rows="3"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Órdenes clínicas específicas"
              />
            </div>
            <div>
              <label for="clinicalOrders" class="block text-sm font-medium text-secondary-900">
                Evolución del Paciente <span class="text-danger-600">*</span>
              </label>
              <textarea
                id="patientProgress"
                v-model="form.patient_progress"
                rows="3"
                class="mt-2 w-full rounded-lg border border-secondary-300 bg-white px-4 py-2.5 text-secondary-900 placeholder-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors"
                placeholder="Evolución del paciente en las consultas"
              />
            </div>
          </div>
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
            <span v-if="!isLoading">Guardar Historial</span>
            <span v-else class="flex items-center justify-center gap-2">
              <svg class="h-4 w-4 animate-spin" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
              </svg>
              Guardando...
            </span>
          </button>
        </div>

        <!-- Error Message -->
        <div v-if="errorMessage" class="rounded-lg bg-danger-50 p-4 text-sm text-danger-600 border border-danger-200">
          {{ errorMessage }}
        </div>

        <!-- Success Message -->
        <div v-if="successMessage" class="rounded-lg bg-success-50 p-4 text-sm text-success-600 border border-success-200">
          {{ successMessage }}
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { useRouter } from 'vue-router'
import { user } from '../store/auth'
import axios from 'axios'

const router = useRouter()
const isLoading = ref(false)
let debounceTimer: ReturnType<typeof setTimeout> | null = null;

const patients = ref<any[]>([]);
const selectedPatient = ref<any>(null); 
const isSelecting = ref(false)
const searchQuery = ref('')

const errorMessage = ref('')
const successMessage = ref('')

const form = ref({
  consultation_reason: '',
  current_illness: '',
  temperature: null,
  systolic_pressure: null,
  diastolic_pressure: null,
  heart_rate: null,
  respiratory_rate: null,
  weight: null,
  height: null,
  imc: null,
  abdominal_perimeter: null,
  head_perimeter: null,
  consciousness_status: '',
  respiratory_status: '',
  hydration_status: '',
  general_status: '',
  physical_examination: '',
  head_system: '',
  eyes_system: '',
  otolaryngology_system: '',
  neck_system: '',
  chest_system: '',
  cardiac_system: '',
  pulmonary_system: '',
  digestive_system: '',
  genitourinary_system: '',
  central_nervous_system: '',
  skin_system: '',
  extremities_system: '',
  other_system: '',
  head_findings: '',
  eyes_findings: '',
  otolaryngology_findings: '',
  mouth_findings: '',
  neck_findings: '',
  chest_findings: '',
  abdominal_findings: '',
  genitourinary_findings: '',
  central_nervous_findings: '',
  skin_findings: '',
  extremities_findings: '',
  mental_findings: '',
  other_findings: '',
  analysis: '',
  diagnosis: '',
  follow_up_plan: '',
  clinical_orders: '',
  family_history: '',
  personal_history: '',
  patient_progress: '',
})

const searchPatient = async () => {
    if (isSelecting.value || !searchQuery.value.trim()) {
        patients.value = [];
        return;
    }

    if (searchQuery.value.length > 2){
        const response = await axios.get(`http://127.0.0.1:8000/registers/`, {
            params: { search: searchQuery.value}
        })
        patients.value = response.data
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

    setTimeout(() => {
        isSelecting.value = false;
    }, 100);
}

const handleInput = () => {
  // 1. Si ya hay un temporizador corriendo, lo cancelamos
  if (debounceTimer) clearTimeout(debounceTimer);
  // 2. Creamos un nuevo temporizador de 400ms
  debounceTimer = setTimeout(() => {
    searchPatient();
  }, 400); // 400ms es el "punto dulce" entre rapidez y ahorro de recursos
};

const handleSubmit = async () => {
  try {
    isLoading.value = true
    errorMessage.value = ''
    successMessage.value = ''

    // API call
    const response = await axios.post('http://127.0.0.1:8000/histories/', {
      register: selectedPatient.value.register_id,
      ...form.value,
    })

    successMessage.value = '¡Historial guardado exitosamente!'

    // Redirect after a short delay
    setTimeout(() => {
      router.push('/dashboard')
    }, 1500)
  } catch (error: any) {
    errorMessage.value = error.response?.data?.message || 'Error al guardar el historial. Por favor intenta de nuevo.'
  } finally {
    isLoading.value = false
  }
}

const getSexLabel = (code: string) => {
  const labels: any = {
    M: 'Masculino',
    F: 'Femenino',
    O: 'Otro',
  }
  return labels[code] || code
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
    }
})
</script>
