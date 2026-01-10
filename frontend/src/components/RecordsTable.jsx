import React from 'react';

const mockRecords = [
  { id: 1, type: 'Theft', date: '2026-01-01', status: 'Solved' },
  { id: 2, type: 'Assault', date: '2026-01-02', status: 'Unsolved' },
];

export default function RecordsTable() {
  return (
    <table border="1" cellPadding={5}>
      <thead>
        <tr>
          <th>ID</th>
          <th>Type</th>
          <th>Date</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        {mockRecords.map(r => (
          <tr key={r.id} style={{ backgroundColor: r.status === 'Solved' ? 'lightgreen' : 'lightcoral' }}>
            <td>{r.id}</td>
            <td>{r.type}</td>
            <td>{r.date}</td>
            <td>{r.status}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}