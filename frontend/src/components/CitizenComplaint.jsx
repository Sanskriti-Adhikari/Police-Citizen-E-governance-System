import React from 'react';

export default function CitizenComplaint() {
  return (
    <div>
      <h3>File Complaint</h3>
      <input placeholder="Your Name" /><br />
      <input placeholder="Type of Complaint" /><br />
      <textarea placeholder="Details"></textarea><br />
      <button>Submit Complaint</button>
    </div>
  );
}