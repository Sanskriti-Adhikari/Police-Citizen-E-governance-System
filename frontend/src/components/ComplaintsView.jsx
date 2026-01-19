export default function ComplaintsView() {
  const complaints = [
    { id: 1, citizen: 'Alice', type: 'Noise', status: 'Pending' },
    { id: 2, citizen: 'Bob', type: 'Theft', status: 'Resolved' },
  ];

  return (
    <div>
      <h3>Citizen Complaints</h3>
      {complaints.map(c => (
        <div key={c.id}>{c.citizen} - {c.type} [{c.status}]</div>
      ))}
    </div>
  );
}