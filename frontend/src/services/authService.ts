import { ref } from "vue"
import axios from "axios"
import { isAuthenticated, user, authInitialized }  from "../store/auth.ts"

// Verify login
export const login = async (email:string,password:string) => {
 const response = await axios.post("http://127.0.0.1:8000/auth/login/",{
  email,
  password
 })

 localStorage.setItem("access",response.data.access)
 localStorage.setItem("refresh", response.data.refresh)

 axios.defaults.headers.common["Authorization"] = "Bearer " + localStorage.getItem("access")

 return response.data
}

// Secure logout
export const logout = () => {
  window.location.reload()
  localStorage.removeItem("access")
  localStorage.removeItem("refresh")
  isAuthenticated.value = false
  user.value = null
}

// Verify authentication from login (persistent connection)
export function useAuth() {
  const initAuth = async () => {
    const token = localStorage.getItem("access")

    if (!token) {
      isAuthenticated.value = false
      authInitialized.value = true
      return
    }

    try {
      const response = await axios.get("http://127.0.0.1:8000/users/me", {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })

      user.value = response.data
      isAuthenticated.value = true
    } 
    catch {
      isAuthenticated.value = false
      localStorage.removeItem("access")
    } 
    finally {
      authInitialized.value = true
    }
  }

  return {
    isAuthenticated,
    user,
    initAuth,
    authInitialized
  }
}