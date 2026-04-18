import axios from "axios"
import { logout, expiredToken } from "../services/authService"
import { isAuthenticated, user } from "../store/auth"

axios.interceptors.response.use(
  response => response,
  async error => {

    if (error.response?.status === 401) {

      const refresh = localStorage.getItem("refresh")      

      if (!expiredToken(refresh)) {
        window.location.href = "/login"          
        isAuthenticated.value = false
        user.value = null
        logout()

        return Promise.reject(error)
      }
      try {
        
      } 
      catch {
        logout()
      }
    }

    return Promise.reject(error)
  }
)