import React, { useState } from 'react';

export default function Signup({ onSignup, switchToLogin }) {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    role: 'citizen'
  });

  const handleChange = (e) => {
    setFormData(prev => ({
      ...prev,
      [e.target.name]: e.target.value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSignup({ name: formData.username, role: formData.role });
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>📝 Signup</h2>
      <form onSubmit={handleSubmit}>
        <label>Username</label>
        <input name="username" value={formData.username} onChange={handleChange} />

        <label>Password</label>
        <input type="password" name="password" value={formData.password} onChange={handleChange} />

        <label>Role</label>
        <select name="role" value={formData.role} onChange={handleChange}>
          <option value="citizen">Citizen</option>
          <option value="officer">Officer</option>
        </select>

        <button type="submit">Signup</button>
      </form>
      <p>
        Already have an account?{' '}
        <button onClick={switchToLogin}>Login</button>
      </p>
    </div>
  );
}