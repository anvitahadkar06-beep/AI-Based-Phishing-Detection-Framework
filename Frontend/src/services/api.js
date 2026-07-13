import axios from "axios";

const API = axios.create({
  baseURL: "https://ai-based-phishing-detection-framework.onrender.com",
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 30000,
});

export const scanURL = async (url) => {
  const response = await API.post("/predict", {
    url: url,
  });

  return response.data;
};

export default API;