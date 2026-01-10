import 'leaflet/dist/leaflet.css';
import React, { useState } from 'react';
import Login from './components/Login';
import Signup from './components/Signup';
import OfficerDashboard from './components/OfficerDashboard';
import CitizenDashboard from './components/CitizenDashboard';

export default function App() {
  const [user, setUser] = useState(null);
  const [mode, setMode] = useState('login');

  if (!user) {
    return mode === 'login' ? (
      <Login onLogin={setUser} switchToSignup={() => setMode('signup')} />
    ) : (
      <Signup onSignup={setUser} switchToLogin={() => setMode('login')} />
    );
  }

  switch (user.role) {
    case 'officer':
      return <OfficerDashboard />;
    case 'citizen':
      return <CitizenDashboard />;
    default:
      return <h2 style={{ padding: 30 }}>❗ Unknown role: {user.role}</h2>;
  }
}