import React, { useState } from 'react';
import CitizenComplaint from './CitizenComplaint';
import EmergencyDial from './EmergencyDial';
import Notices from './Notices';

export default function CitizenDashboard() {
  const [activeSection, setActiveSection] = useState('complaint');

  return (
    <div style={{ padding: 20 }}>
      <h1>👤 Citizen Dashboard</h1>

      <div style={{ display: 'flex', gap: 10, marginBottom: 20 }}>
        <button onClick={() => setActiveSection('complaint')}>File Complaint</button>
        <button onClick={() => setActiveSection('emergency')}>Emergency Dial</button>
        <button onClick={() => setActiveSection('notices')}>Notices / Info</button>
      </div>

      <div>
        {activeSection === 'complaint' && <CitizenComplaint />}
        {activeSection === 'emergency' && <EmergencyDial />}
        {activeSection === 'notices' && <Notices />}
      </div>
    </div>
  );
}