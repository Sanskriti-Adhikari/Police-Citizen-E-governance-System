import React, { useState } from 'react';

export default function EnterReports() {
  const [formData, setFormData] = useState({
    type: '',
    severity: 'Low',
    description: ''
  });

  const handleChange = (e) => {
    setFormData(prev => ({
      ...prev,
      [e.target.name]: e.target.value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(Crime Report Submitted!\n${JSON.stringify(formData, null, 2)});
  };

  return (
    <div className="card" style={{ marginTop: 20, padding: 10 }}>
      <h2>📝 Enter Crime Report</h2>
      <form onSubmit={handleSubmit}>
        <label>Crime Type</label>
        <input name="type" value={formData.type} onChange={handleChange} />

        <label>Severity</label>
        <select name="severity" value={formData.severity} onChange={handleChange}>
          <option>Low</option>
          <option>Medium</option>
          <option>High</option>
        </select>

        <label>Description</label>
        <textarea name="description" rows="4" value={formData.description} onChange={handleChange} />

        <button type="submit">Submit Report</button>
      </form>
    </div>
  );
}