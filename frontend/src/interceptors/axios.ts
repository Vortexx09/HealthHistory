import axios from "axios"
import { logout } from "../services/authService"

// Refresh Token
axios.interceptors.response.use(
  response => response,
  async error => {

    if (error.response?.status === 401) {

      const refresh = localStorage.getItem("refresh")

      if (!refresh) {
        logout()
        return Promise.reject(error)
      }

      try {
        const res = await axios.post("/auth/refresh/", {
          refresh
        })

        localStorage.setItem("access", res.data.access)

        error.config.headers["Authorization"] =
          "Bearer " + res.data.access

        return axios(error.config)

      } catch {
        logout()
      }
    }

    return Promise.reject(error)
  }
)