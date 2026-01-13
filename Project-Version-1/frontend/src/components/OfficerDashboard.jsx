import React, { useState } from 'react';
import CrimeHeatmap from './CrimeHeatmap';
import EnterReports from './EnterReports';
import RecordsTable from './RecordsTable';
import OfficerAllocation from './OfficerAllocation';
import CaseTracking from './CaseTracking';
import ComplaintsView from './ComplaintsView';

export default function OfficerDashboard() {
  const [activeSection, setActiveSection] = useState('enterReports');

  return (
    <div style={{ padding: 20 }}>
      <h1>👮 Officer Dashboard</h1>

      {/* Heatmap /}
      <div style={{ height: 400, marginBottom: 20 }}>
        <CrimeHeatmap />
      </div>

      {/ Menu buttons /}
      <div style={{ display: 'flex', gap: 10, marginBottom: 20 }}>
        <button onClick={() => setActiveSection('enterReports')}>Enter Reports</button>
        <button onClick={() => setActiveSection('records')}>View Records</button>
        <button onClick={() => setActiveSection('allocation')}>Officer Allocation</button>
        <button onClick={() => setActiveSection('cases')}>Case Tracking</button>
        <button onClick={() => setActiveSection('complaints')}>Alerts & Complaints</button>
      </div>

      {/ Active section */}
      <div>
        {activeSection === 'enterReports' && <EnterReports />}
        {activeSection === 'records' && <RecordsTable />}
        {activeSection === 'allocation' && <OfficerAllocation />}
        {activeSection === 'cases' && <CaseTracking />}
        {activeSection === 'complaints' && <ComplaintsView />}
      </div>
    </div>
  );
}