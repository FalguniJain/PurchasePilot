import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
  withCredentials: true,
});

// add request interceptor to include auth token
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Add this function to your api.ts
export const fetchSimilarProducts = async (productName: string) => {
  try {
    const response = await api.get(`/similar_products/${encodeURIComponent(productName)}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching similar products:', error);
    // Return empty results instead of throwing
    return { similar_products: [] };
  }
};

// Add response interceptor to handle auth errors
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response.status === 401) {
      localStorage.removeItem("token");
      if (typeof window !== "undefined") {
        // Add a small delay to prevent event conflicts
        setTimeout(() => {
          window.dispatchEvent(new CustomEvent("auth:failed"));
        }, 0);
      }
    }
    return Promise.reject(error);
  },
);
        

export default api;
