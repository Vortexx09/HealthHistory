import { ref } from "vue"

export const isAuthenticated = ref(false)
export const user = ref<User | null>(null);
export const authInitialized = ref(false)

interface User {
  id: number;
  email: string;
  first_name: string;
  last_name: string;
  user_type: string;
}