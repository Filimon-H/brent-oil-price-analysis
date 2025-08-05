import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000/api", // make sure Flask is running!
});

export const fetchSummary = () => api.get("/summary");
