import api from '../api'
import { logout } from "../services/authService"
import { isAuthenticated, user } from "../store/auth"

// Refresh Token
api.interceptors.response.use(
  response => response,
  async error => {

    if (error.response?.status === 401) {

      const refresh = localStorage.getItem("refresh")      

      if (!refresh) {
        window.location.href = "/login"          
        isAuthenticated.value = false
        user.value = null
        logout()

        return Promise.reject(error)

      }
      try {
        const res = await api.post('/auth/refresh/', {
          refresh
        })

        localStorage.setItem("access", res.data.access)

        error.config.headers["Authorization"] =
          "Bearer " + res.data.access

        return api(error.config)

      } 
      catch {
        logout()
      }
    }

    return Promise.reject(error)
  }
)