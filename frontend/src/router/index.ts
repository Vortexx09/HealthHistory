import { createRouter, createWebHistory } from 'vue-router'
import LandingView from '../views/LandingView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import DashboardView from '../views/DashboardView.vue'
import AddPatientView from '../views/AddPatientView.vue'
import PatientHistoryView from '../views/PatientHistoryView.vue'
import PlaceholderView from '../views/PlaceholderView.vue'

import { user } from '../store/auth'
import { useAuth, fetchUser, logout, expiredToken, removeToken, refreshToken } from '../services/authService'


const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'landing',
      component: LandingView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView,
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView,
    },
    {
      path: '/add-patient',
      name: 'add-patient',
      component: AddPatientView,
    },
    {
      path: '/history',
      name: 'history',
      component: PatientHistoryView,
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'placeholder',
      component: PlaceholderView,
    },
  ],
})

// Router Guard
router.beforeEach(async (to, from) => {
  const { initAuth, isAuthenticated, authInitialized } = useAuth()
  const token = localStorage.getItem("access")

  if (expiredToken(token)){
    await refreshToken()
  }
  
  if (!authInitialized.value) {
    await initAuth()
  }

  if (to.meta.requiresAuth && !token) {
    return { 
      name: 'login',
    }
  }

  return true
})

export default router