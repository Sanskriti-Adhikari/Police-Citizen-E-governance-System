import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/api"; // Change if your backend URL differs

// Criminal Records APIs
export const getCriminalRecords = async () => {
  const res = await axios.get(`${BASE_URL}/records`);
  return res.data;
};

export const addCriminalRecord = async (data) => {
  const res = await axios.post(`${BASE_URL}/records`, data);
  return res.data;
};

export const updateCriminalRecord = async (id, data) => {
  const res = await axios.put(`${BASE_URL}/records/${id}`, data);
  return res.data;
};

export const deleteCriminalRecord = async (id) => {
  const res = await axios.delete(`${BASE_URL}/records/${id}`);
  return res.data;
};

// Officers APIs
export const getOfficers = async () => {
  const res = await axios.get(`${BASE_URL}/officers`);
  return res.data;
};

export const addOfficer = async (data) => {
  const res = await axios.post(`${BASE_URL}/officers`, data);
  return res.data;
};

export const updateOfficer = async (id, data) => {
  const res = await axios.put(`${BASE_URL}/officers/${id}`, data);
  return res.data;
};

export const deleteOfficer = async (id) => {
  const res = await axios.delete(`${BASE_URL}/officers/${id}`);
  return res.data;
};

// Holidays APIs
export const getHolidays = async () => {
  const res = await axios.get(`${BASE_URL}/holidays`);
  return res.data;
};

export const requestHoliday = async (data) => {
  const res = await axios.post(`${BASE_URL}/holidays/request`, data);
  return res.data;
};

// Allocation API
export const allocateOfficers = async (data) => {
  const res = await axios.post(`${BASE_URL}/allocation/allocate`, data);
  return res.data;
};

// Analytics API
export const getAnalytics = async () => {
  const res = await axios.get(`${BASE_URL}/analytics`);
  return res.data;
};

export const getHeatmap = async () => {
  const res = await axios.get(`${BASE_URL}/analytics/heatmap`);
  return res.data;
};

export const getTrends = async () => {
  const res = await axios.get(`${BASE_URL}/analytics/trends`);
  return res.data;
};
