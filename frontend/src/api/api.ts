import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000',
})

// Set token on every request if it exists
api.interceptors.request.use(config => {
  const token = localStorage.getItem('access')
  if (token) {
    config.headers['Authorization'] = `Bearer ${token}`
  }
  return config
})

export default api