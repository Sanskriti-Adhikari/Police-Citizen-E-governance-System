// Users
export const users = [
  { username: 'officer1', password: '123', role: 'officer' },
  { username: 'citizen1', password: '123', role: 'citizen' }
];

// Crimes
export const crimes = [
  { id: 1, type: 'Robbery', lat: 27.7, lng: 85.3, severity: 'High', status: 'Open', description: 'Bank robbed', date: '2026-01-01' },
  { id: 2, type: 'Theft', lat: 27.6, lng: 85.4, severity: 'Medium', status: 'Solved', description: 'Bike stolen', date: '2026-01-02' }
];

// Officers
export const officers = [
  { id: 1, name: 'Officer A', assignedCases: [1] },
  { id: 2, name: 'Officer B', assignedCases: [] }
];

// Complaints
export const complaints = [
  { id: 1, citizen: 'John Doe', description: 'Noise complaint', status: 'Pending' },
  { id: 2, citizen: 'Jane Smith', description: 'Illegal parking', status: 'Resolved' }
];

// mockData.js

export let users = [
  { username: 'officer1', password: '123', role: 'officer' },
  { username: 'citizen1', password: '123', role: 'citizen' }
];

export function addUser(user) {
  users.push(user);
}