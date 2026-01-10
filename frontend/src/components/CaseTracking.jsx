export default function CaseTracking() {
  const cases = [
    { id: 1, case: 'Theft', officer: 'Officer A', status: 'In Progress' },
    { id: 2, case: 'Assault', officer: 'Officer B', status: 'Solved' },
  ];

  return (
    <table border="1" cellPadding={5}>
      <thead>
        <tr>
          <th>Case ID</th>
          <th>Case Type</th>
          <th>Officer</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        {cases.map(c => (
          <tr key={c.id}>
            <td>{c.id}</td>
            <td>{c.case}</td>
            <td>{c.officer}</td>
            <td>{c.status}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}