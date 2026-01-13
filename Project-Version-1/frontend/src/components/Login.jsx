import React, { useState } from 'react';

export default function Login({ onLogin, switchToSignup }) {
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
    onLogin({ name: formData.username, role: formData.role });
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>🔐 Login</h2>
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

        <button type="submit">Login</button>
      </form>
      <p>
        Don't have an account?{' '}
        <button onClick={switchToSignup}>Signup</button>
      </p>
    </div>
  );
}