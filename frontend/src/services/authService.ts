import { ref } from "vue"
import api from '../api'
import { isAuthenticated, user, authInitialized }  from "../store/auth.ts"

export const login = async (username:string,password:string) => {
  // API call
  const response = await api.post('/auth/login/', {
    id_number: username,
    password,
  }) 

  // Store token
  localStorage.setItem("access", response.data.access)
  localStorage.setItem("refresh", response.data.refresh)

  // Update state
  isAuthenticated.value = true

  // Pass access token
  api.defaults.headers.common["Authorization"] = "Bearer " + localStorage.getItem("access")
  
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

// Fetch the user data
export const fetchUser = async () => {
  try {
    const response = await api.get('/users/me/')
    user.value = response.data
  } catch {
    user.value = null
  }
}

// Initialize authorization, save user data.
export const initAuth = async () => {
  const token = localStorage.getItem("access")

  if (token) {
    api.defaults.headers.common["Authorization"] = `Bearer ${token}`
    isAuthenticated.value = true

    try {
      await fetchUser()
    } catch {
      logout()
    }

  } else {
    isAuthenticated.value = false
  }

  authInitialized.value = true
}

// Global method to use initAuth
export function useAuth() {
  return {
    isAuthenticated,
    user,
    initAuth,
    authInitialized
  }
}

// Remove token when needed
export const removeToken = async () => {
  const access = localStorage.getItem("access")

  if (expiredToken(access)){
    localStorage.removeItem("access")
  }
}

// Refresh token, 
export const refreshToken = async () => {
  const refresh = localStorage.getItem("refresh")

  const response = await api.post('/auth/refresh/', {
    refresh
  })

  localStorage.setItem("access", response.data.access)

  api.defaults.headers.common["Authorization"] =
    "Bearer " + response.data.access
}

// Checks token expiration
export const expiredToken = (token: string | null) => {
  if (!token) {
    return
  }

  const payload = JSON.parse(atob(token.split('.')[1]))
  return payload.exp * 1000 < Date.now()
}