<template>
  <div class="bg-white">
    <!-- Sección Hero -->
    <section class="relative overflow-hidden px-4 py-20 sm:px-6 sm:py-24 lg:px-8 lg:py-32">
      <div class="mx-auto max-w-5xl">
        <div class="grid gap-12 lg:grid-cols-2 lg:gap-8 lg:items-center">
          <!-- Contenido Hero -->
          <div class="flex flex-col justify-center">
            <h1 class="text-4xl font-bold tracking-tight text-secondary-900 sm:text-5xl">
              Tus registros de salud,
              <span class="block text-primary-600">siempre a tu alcance</span>
            </h1>
            <p class="mt-6 text-lg text-secondary-600">
              Gestiona tu historial médico de forma segura en un solo lugar. Accede a tus registros de salud en cualquier momento, compártelos con profesionales médicos y toma el control de tu bienestar.
            </p>
            <div class="mt-8 flex flex-col gap-4 sm:flex-row sm:gap-4">
              <router-link
                v-if="!isAuthenticated"
                to="/register"
                class="inline-flex items-center justify-center rounded-lg bg-primary-600 px-6 py-3 text-base font-semibold text-white transition-colors hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2"
              >
                Comenzar gratis
              </router-link>
              
              <button
                @click="scrollToFeatures"
                class="inline-flex items-center justify-center rounded-lg border border-secondary-300 px-6 py-3 text-base font-semibold text-secondary-700 transition-colors hover:border-secondary-400 hover:bg-secondary-50"
              >
                Más información
              </button>
            </div>
            <div class="mt-8 flex items-center gap-8">
              <div>
                <div class="text-2xl font-bold text-secondary-900">10.000+</div>
                <div class="text-sm text-secondary-600">Usuarios activos</div>
              </div>
              <div>
                <div class="text-2xl font-bold text-secondary-900">99.9%</div>
                <div class="text-sm text-secondary-600">Tiempo activo</div>
              </div>
              <div>
                <div class="text-2xl font-bold text-secondary-900">100%</div>
                <div class="text-sm text-secondary-600">Cifrado</div>
              </div>
            </div>
          </div>

          <!-- Imagen Hero -->
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
                  <p class="mt-4 text-lg font-semibold text-primary-900">Registros médicos</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Sección de características -->
    <section ref="featuresRef" class="bg-secondary-50 px-4 py-20 sm:px-6 sm:py-24 lg:px-8">
      <div class="mx-auto max-w-5xl">
        <div class="text-center">
          <h2 class="text-3xl font-bold tracking-tight text-secondary-900 sm:text-4xl">
            Funcionalidades pensadas para tu salud
          </h2>
          <p class="mt-4 text-lg text-secondary-600">
            Todo lo que necesitas para gestionar tus registros médicos de manera eficiente
          </p>
        </div>

        <div class="mt-16 grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
          <!-- Característica 1 -->
          <div class="rounded-lg bg-white p-8 shadow-sm border border-secondary-200">
            <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-primary-100">
              <svg class="h-6 w-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
              </svg>
            </div>
            <h3 class="mt-4 text-lg font-semibold text-secondary-900">Gestión sencilla</h3>
            <p class="mt-2 text-secondary-600">
              Organiza y gestiona todos tus registros médicos en un lugar seguro
            </p>
          </div>

          <!-- Característica 2 -->
          <div class="rounded-lg bg-white p-8 shadow-sm border border-secondary-200">
            <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-primary-100">
              <svg class="h-6 w-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
              </svg>
            </div>
            <h3 class="mt-4 text-lg font-semibold text-secondary-900">Seguridad bancaria</h3>
            <p class="mt-2 text-secondary-600">
              Tus datos están cifrados con los más altos estándares de seguridad
            </p>
          </div>

          <!-- Característica 3 -->
          <div class="rounded-lg bg-white p-8 shadow-sm border border-secondary-200">
            <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-primary-100">
              <svg class="h-6 w-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m7 0a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <h3 class="mt-4 text-lg font-semibold text-secondary-900">Comparte de forma segura</h3>
            <p class="mt-2 text-secondary-600">
              Concede acceso a profesionales de la salud cuando lo necesites
            </p>
          </div>

          <!-- Característica 4 -->
          <div class="rounded-lg bg-white p-8 shadow-sm border border-secondary-200">
            <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-primary-100">
              <svg class="h-6 w-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <h3 class="mt-4 text-lg font-semibold text-secondary-900">Acceso rápido</h3>
            <p class="mt-2 text-secondary-600">
              Obtén acceso instantáneo a tus registros en cualquier momento y lugar
            </p>
          </div>

          <!-- Característica 5 -->
          <div class="rounded-lg bg-white p-8 shadow-sm border border-secondary-200">
            <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-primary-100">
              <svg class="h-6 w-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
            </div>
            <h3 class="mt-4 text-lg font-semibold text-secondary-900">Perspectivas de salud</h3>
            <p class="mt-2 text-secondary-600">
              Sigue tendencias y obtén información sobre tu salud a lo largo del tiempo
            </p>
          </div>

          <!-- Característica 6 -->
          <div class="rounded-lg bg-white p-8 shadow-sm border border-secondary-200">
            <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-primary-100">
              <svg class="h-6 w-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 5.636l-3.536 3.536m0 5.656l3.536 3.536M9.172 9.172L5.636 5.636m3.536 9.192l-3.536 3.536M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-5 0a4 4 0 11-8 0 4 4 0 018 0z" />
              </svg>
            </div>
            <h3 class="mt-4 text-lg font-semibold text-secondary-900">Soporte 24/7</h3>
            <p class="mt-2 text-secondary-600">
              Nuestro equipo está siempre disponible para ayudarte
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Sección CTA -->
    <section class="px-4 py-20 sm:px-6 sm:py-24 lg:px-8">
      <div class="mx-auto max-w-2xl text-center">
        <h2 class="text-3xl font-bold tracking-tight text-secondary-900 sm:text-4xl">
          Toma el control de tu salud hoy mismo
        </h2>
        <p class="mt-4 text-lg text-secondary-600">
          Únete a miles de usuarios que confían en HealthHistory para gestionar sus registros médicos
        </p>
        <div class="mt-8">
          <router-link
            to="/register"
            class="inline-flex items-center justify-center rounded-lg bg-primary-600 px-8 py-3 text-lg font-semibold text-white transition-colors hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2"
          >
            Crear tu cuenta
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { isAuthenticated, user } from '../store/auth.ts'


const featuresRef = ref<HTMLElement | null>(null)

const scrollToFeatures = () => {
  if (featuresRef.value) {
    featuresRef.value.scrollIntoView({ behavior: 'smooth' })
  }
}

</script>
