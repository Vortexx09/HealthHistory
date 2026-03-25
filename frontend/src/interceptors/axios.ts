import axios from "axios"
import { logout } from "../services/authService"
import { isAuthenticated, user } from "../store/auth"

// Refresh Token
axios.interceptors.response.use(
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
        const res = await axios.post("http://127.0.0.1:8000/auth/refresh/", {
          refresh
        })

        localStorage.setItem("access", res.data.access)

        error.config.headers["Authorization"] =
          "Bearer " + res.data.access

        return axios(error.config)

      } 
      catch {
        logout()
      }
    }

    return Promise.reject(error)
  }
)