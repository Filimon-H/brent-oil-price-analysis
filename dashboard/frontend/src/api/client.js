//import axios from "axios";

// 🔧 Create axios instance with base URL
//const api = axios.create({
  //baseURL: "http://localhost:5000/api", // make sure Flask is running
//});

// ✅ Use the same instance for all API calls
//export const fetchSummary = () => api.get("/summary");

//export const fetchPriceTrend = () => api.get("/events/price_trend");

//export const fetchVolatility = () => api.get("/events/volatility");
//


//....................


import axios from "axios";

// 🔧 Create axios instance with base URL
const api = axios.create({
  baseURL: "http://localhost:5000/api", // Ensure Flask backend is running here
});

// ✅ Fetch summary card info
export const fetchSummary = () => api.get("/summary");

// ✅ Enhanced: Add optional filtering AND event toggle
export const fetchPriceTrend = (start = "", end = "", includeEvents = false) => {
  const params = {};
  if (start) params.start_date = start;
  if (end) params.end_date = end;
  if (includeEvents) params.include_events = true;

  return api.get("/events/price_trend", { params });
};


// 📈 Volatility API call (used in VolatilityChart.jsx)
export const fetchVolatility = () => api.get("/events/volatility");

// 🔄 API for average price change around events
export const fetchEventImpacts = () => api.get("/events/price_change_impact");

export const fetchForecast = () => api.get("/events/forecast");
export const fetchBayesianForecast = () => api.get("/events/bayesian_forecast");
