<template>
  <div class="min-h-screen bg-secondary-50">
    <!-- Header Section -->
    <div class="border-b border-secondary-200 bg-white shadow-sm">
      <div class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <div class="flex flex-col justify-between sm:flex-row sm:items-center">
          <div>
            <h1 class="text-3xl font-bold text-secondary-900">Welcome back, Dr. {{ user?.last_name }}</h1>
            <p class="mt-2 text-secondary-600">
              {{ getGreeting() }} - You have {{ totalPatients }} patients in your system
            </p>
          </div>
          <div class="mt-4 text-right sm:mt-0">
            <p class="text-sm text-secondary-500">Last updated: {{ currentDate }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
      <!-- Quick Stats Row -->
      <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-4 mb-8">
        <!-- Total Patients Stat -->
        <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200 hover:shadow-md transition-shadow">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm text-secondary-600 font-medium">Total Patients</p>
              <p class="mt-2 text-3xl font-bold text-secondary-900">{{ totalPatients }}</p>
              <p class="mt-1 text-xs text-success-600">↑ 12% from last month</p>
            </div>
            <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-primary-100">
              <svg class="h-6 w-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.856-1.487M15 10h.01M11 10h.01M7 10h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
            </div>
          </div>
        </div>

        <!-- Appointments This Month Stat -->
        <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200 hover:shadow-md transition-shadow">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm text-secondary-600 font-medium">Appointments</p>
              <p class="mt-2 text-3xl font-bold text-secondary-900">{{ appointmentsThisMonth }}</p>
              <p class="mt-1 text-xs text-secondary-600">This month</p>
            </div>
            <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-blue-100">
              <svg class="h-6 w-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
            </div>
          </div>
        </div>

        <!-- Urgent Cases Stat -->
        <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200 hover:shadow-md transition-shadow">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm text-secondary-600 font-medium">Urgent Cases</p>
              <p class="mt-2 text-3xl font-bold text-danger-600">{{ urgentCases }}</p>
              <p class="mt-1 text-xs text-danger-600">Require attention</p>
            </div>
            <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-danger-100">
              <svg class="h-6 w-6 text-danger-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4v.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
          </div>
        </div>

        <!-- Pending Records Stat -->
        <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200 hover:shadow-md transition-shadow">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm text-secondary-600 font-medium">Pending Records</p>
              <p class="mt-2 text-3xl font-bold text-secondary-900">{{ pendingRecords }}</p>
              <p class="mt-1 text-xs text-secondary-600">To be reviewed</p>
            </div>
            <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-accent-100">
              <svg class="h-6 w-6 text-accent-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
          </div>
        </div>
      </div>

      <!-- Main Features Section -->
      <div class="mb-8">
        <div class="mb-6">
          <h2 class="text-2xl font-bold text-secondary-900">Main Features</h2>
          <p class="mt-2 text-secondary-600">Quick access to the most common operations</p>
        </div>

        <div class="grid gap-6 sm:grid-cols-3">
          <!-- Add Patient Feature -->
          <router-link
            to="/add-patient"
            class="group rounded-lg bg-white p-8 shadow-sm border-2 border-secondary-200 transition-all hover:border-primary-500 hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2"
          >
            <div class="flex flex-col items-center text-center">
              <div class="flex h-16 w-16 items-center justify-center rounded-lg bg-primary-100 group-hover:bg-primary-200 transition-colors">
                <svg class="h-8 w-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                </svg>
              </div>
              <h3 class="mt-4 text-lg font-semibold text-secondary-900">Add Patient</h3>
              <p class="mt-2 text-sm text-secondary-600">Register a new patient to the system</p>
              <div class="mt-4 inline-flex items-center gap-2 text-sm font-medium text-primary-600 group-hover:text-primary-700">
                Get Started
                <svg class="h-4 w-4 transition-transform group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
              </div>
            </div>
          </router-link>

          <!-- Manage Patient Feature -->
          <router-link
            to="/"
            class="group rounded-lg bg-white p-8 shadow-sm border-2 border-secondary-200 transition-all hover:border-blue-500 hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
          >
            <div class="flex flex-col items-center text-center">
              <div class="flex h-16 w-16 items-center justify-center rounded-lg bg-blue-100 group-hover:bg-blue-200 transition-colors">
                <svg class="h-8 w-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                </svg>
              </div>
              <h3 class="mt-4 text-lg font-semibold text-secondary-900">Manage Patient</h3>
              <p class="mt-2 text-sm text-secondary-600">Update patient information and records</p>
              <div class="mt-4 inline-flex items-center gap-2 text-sm font-medium text-blue-600 group-hover:text-blue-700">
                Manage
                <svg class="h-4 w-4 transition-transform group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
              </div>
            </div>
          </router-link>

          <!-- Add History Feature -->
          <router-link
            to="/"
            class="group rounded-lg bg-white p-8 shadow-sm border-2 border-secondary-200 transition-all hover:border-accent-500 hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-accent-400 focus:ring-offset-2"
          >
            <div class="flex flex-col items-center text-center">
              <div class="flex h-16 w-16 items-center justify-center rounded-lg bg-accent-100 group-hover:bg-accent-200 transition-colors">
                <svg class="h-8 w-8 text-accent-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C6.5 6.253 2 10.998 2 17s4.5 10.747 10 10.747c5.5 0 10-4.998 10-10.747S17.5 6.253 12 6.253z" />
                </svg>
              </div>
              <h3 class="mt-4 text-lg font-semibold text-secondary-900">Add History</h3>
              <p class="mt-2 text-sm text-secondary-600">Record medical history and findings</p>
              <div class="mt-4 inline-flex items-center gap-2 text-sm font-medium text-accent-600 group-hover:text-accent-700">
                Add Record
                <svg class="h-4 w-4 transition-transform group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
              </div>
            </div>
          </router-link>
        </div>
      </div>

      <!-- Recent Activity Section -->
      <div class="grid gap-8 lg:grid-cols-3">
        <!-- Upcoming Appointments -->
        <div class="lg:col-span-2 rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
          <h3 class="text-lg font-semibold text-secondary-900 mb-4">Upcoming Appointments</h3>
          <div class="space-y-4">
            <div
              v-for="appointment in upcomingAppointments"
              :key="appointment.id"
              class="flex items-center justify-between border-b border-secondary-100 pb-4 last:border-b-0"
            >
              <div class="flex items-center gap-4">
                <div class="flex h-10 w-10 items-center justify-center rounded-full bg-primary-100">
                  <span class="text-sm font-semibold text-primary-600">{{ appointment.initials }}</span>
                </div>
                <div>
                  <p class="font-medium text-secondary-900">{{ appointment.name }}</p>
                  <p class="text-sm text-secondary-600">{{ appointment.time }}</p>
                </div>
              </div>
              <span class="inline-flex items-center rounded-full bg-blue-100 px-3 py-1 text-xs font-medium text-blue-700">
                {{ appointment.type }}
              </span>
            </div>
          </div>
          <button class="mt-6 w-full rounded-lg border border-primary-600 px-4 py-2 text-sm font-semibold text-primary-600 transition-colors hover:bg-primary-50">
            View All Appointments
          </button>
        </div>

        <!-- Quick Actions -->
        <div class="rounded-lg bg-white p-6 shadow-sm border border-secondary-200">
          <h3 class="text-lg font-semibold text-secondary-900 mb-4">Quick Actions</h3>
          <div class="space-y-3">
            <button class="w-full rounded-lg bg-primary-50 px-4 py-3 text-left text-sm font-medium text-primary-700 transition-colors hover:bg-primary-100">
              <div class="flex items-center gap-3">
                <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                </svg>
                New Patient
              </div>
            </button>
            <button class="w-full rounded-lg bg-blue-50 px-4 py-3 text-left text-sm font-medium text-blue-700 transition-colors hover:bg-blue-100">
              <div class="flex items-center gap-3">
                <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
                Schedule Appointment
              </div>
            </button>
            <button class="w-full rounded-lg bg-accent-50 px-4 py-3 text-left text-sm font-medium text-accent-700 transition-colors hover:bg-accent-100">
              <div class="flex items-center gap-3">
                <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                View Records
              </div>
            </button>
            <button class="w-full rounded-lg bg-success-50 px-4 py-3 text-left text-sm font-medium text-success-700 transition-colors hover:bg-success-100">
              <div class="flex items-center gap-3">
                <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>
                Prescriptions
              </div>
            </button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { isAuthenticated, user, authInitialized }  from "../store/auth.ts"
import axios from 'axios'

// Dashboard Data
const totalPatients = ref(48)
const appointmentsThisMonth = ref(15)
const urgentCases = ref(3)
const pendingRecords = ref(7)

console.log(isAuthenticated.value)

const upcomingAppointments = ref([
  { id: 1, name: 'John Anderson', initials: 'JA', time: 'Today at 2:00 PM', type: 'Follow-up' },
  { id: 2, name: 'Maria Garcia', initials: 'MG', time: 'Tomorrow at 10:30 AM', type: 'Consultation' },
  { id: 3, name: 'Robert Wilson', initials: 'RW', time: 'Dec 15 at 3:00 PM', type: 'Check-up' },
])

const currentDate = computed(() => {
  const today = new Date()
  return today.toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })
})

const getGreeting = () => {
  const hour = new Date().getHours()
  if (hour < 12) return 'Good morning'
  if (hour < 18) return 'Good afternoon'
  return 'Good evening'
}

</script>