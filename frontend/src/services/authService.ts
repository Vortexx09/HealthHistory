import { isRef, ref } from "vue"
import axios from "axios"
import { router } from '../router/index.ts' // importa la instancia del router
import { user, isAuthenticated, authInitialized, }  from "../store/auth.ts"

export const login = async (username:string,password:string) => {
  // API call
  const response = await axios.post('http://127.0.0.1:8000/auth/login/', {
    username,
    password,
  }) 

  // Store token
  localStorage.setItem("access", response.data.access)
  localStorage.setItem("refresh", response.data.refresh)

  // Update state
  isAuthenticated.value = true

  // Pass access token
  axios.defaults.headers.common["Authorization"] = "Bearer " + localStorage.getItem("access")
  
  return response.data
}

// Secure logout
export const logout = async () => {
  // Redirect to login
  await router.push({ name: 'login' }) // espera que la navegación termine

  // Remove tokens
  localStorage.removeItem("access")
  localStorage.removeItem("refresh")

  // Update state
  isAuthenticated.value = false
  user.value = null
}

// Fetch the user data
export const fetchUser = async () => {
  try {
    // API call
    const response = await axios.get("http://127.0.0.1:8000/users/me/")
    user.value = response.data
  } catch {
    // Clean state
    user.value = null
  }
}

// Initialize authorization, save user data.
export const initAuth = async () => {
  // Obtain access token
  const access = localStorage.getItem("access")

  if (!expiredToken(access)) {
    // Send the bearer and update state
    axios.defaults.headers.common["Authorization"] = `Bearer ${access}`
    isAuthenticated.value = true

    try {
      // Get user data
      await fetchUser()
    } 
    catch {
      // Clean user data
      logout()
    }
  } 
  else {
      isAuthenticated.value = false
  }

  // Ensures the executation once per reload
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

// Refresh token, 
export const refreshToken = async () => {
  // Get refresh token
  const refresh = localStorage.getItem("refresh")
  
  if (!expiredToken(refresh)){
    // API call
    const response = await axios.post("http://127.0.0.1:8000/auth/refresh/", {
      refresh
    })

    // Set new access token
    localStorage.setItem("access", response.data.access)
    axios.defaults.headers.common["Authorization"] =
      "Bearer " + response.data.access
  }
  else {
    // Clean user data
    logout()
  }
}

// Checks token expiration
export const expiredToken = (token: string | null) => {
  if (!token) {
    // If token is null the token is expired
    return true
  }

  // Calculates the token expiration
  const payload = JSON.parse(atob(token.split('.')[1]))
  return payload.exp * 1000 < Date.now()
}