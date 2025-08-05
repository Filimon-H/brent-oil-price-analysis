import axios from "axios";

// 🔧 Create axios instance with base URL
const api = axios.create({
  baseURL: "http://localhost:5000/api", // make sure Flask is running
});

// ✅ Use the same instance for all API calls
export const fetchSummary = () => api.get("/summary");

export const fetchPriceTrend = () => api.get("/events/price_trend");

export const fetchVolatility = () => api.get("/events/volatility");
