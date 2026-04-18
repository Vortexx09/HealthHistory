import { createRouter, createWebHistory } from 'vue-router'
import LandingView from '../views/LandingView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import DashboardView from '../views/DashboardView.vue'
import AddPatientView from '../views/AddPatientView.vue'
import AddHistoryView from '../views/AddHistoryView.vue'
import ManagementView from '../views/ManagementView.vue'
import PlaceholderView from '../views/PlaceholderView.vue'

import { useAuth, expiredToken, refreshToken } from '../services/authService'


export const router = createRouter({
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
      path: '/add-history',
      name: 'add-history',
      component: AddHistoryView,
    },
    {
      path: '/management',
      name: 'management',
      component: ManagementView,
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
  const access = localStorage.getItem("access")

  const publicRoutes = ['login', 'landing', 'register']
  if (!publicRoutes.includes(to.name as string) && expiredToken(access)) {
    await refreshToken()
  }
  
  if (!authInitialized.value)  {
    await initAuth()
  }

  if (to.meta.requiresAuth && !access) {
    return { 
      name: 'login',
    }
  }

  return true
})

export default router