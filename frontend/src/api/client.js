import axios from "axios";

 
const rawBaseURL = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000/api";
const cleanBaseURL = rawBaseURL.replace(/\/+$/, "");  

const api = axios.create({
  baseURL: cleanBaseURL,
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 60000,  
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("gramsetu_access_token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

api.interceptors.response.use(
  (res) => res,
  (error) => {
    const status = error?.response?.status;
    const url = error?.config?.url;
    const message =
      error?.response?.data?.message ||
      error?.response?.data?.detail ||
      error?.message ||
      "Something went wrong talking to the server.";

    console.error(`[API Error] Status: ${status} | Route: ${url} | Message:`, message);
    
    
    const enhancedError = new Error(message);
    enhancedError.response = error.response;
    enhancedError.status = status;
    return Promise.reject(enhancedError);
  }
);

 
async function postWithFallback(primaryPath, fallbackPath, payload) {
  try {
    const res = await api.post(primaryPath, payload);
    return res.data;
  } catch (err) {
    const is404 = err.status === 404 || err.response?.status === 404 || err.message?.includes("404");
    if (fallbackPath && is404) {
      console.warn(`[API Fallback] ${primaryPath} returned 404. Attempting fallback: ${fallbackPath}...`);
      const res = await api.post(fallbackPath, payload);
      return res.data;
    }
    throw err;
  }
}

 
export const structureLoan = (marginCapital) =>
  postWithFallback("/finance/structure-loan/", "/structure-loan/", { margin_capital: marginCapital });

 
export const competitorsDensity = (payload) =>
  postWithFallback("/competitors/density/", "/competitors-density/", payload);

 
export const generateFeasibility = (payload) =>
  postWithFallback("/feasibility/generate/", "/feasibility/", payload);

 
export const fullFeasibilityEvaluation = (payload) =>
  postWithFallback("/feasibility/evaluate/", "/feasibility-evaluate/", payload);

 
export const otpLogin = (payload) =>
  postWithFallback("/auth/otp-login/", "/otp-login/", payload);

export default api;