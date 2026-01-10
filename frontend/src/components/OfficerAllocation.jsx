export default function OfficerAllocation() {
  const assignments = [
    { area: 'Thamel', officers: 3 },
    { area: 'Lalitpur', officers: 2 },
  ];

  return (
    <div>
      <h3>Officer Allocation</h3>
      {assignments.map((a, idx) => (
        <div key={idx}>{a.area}: {a.officers} officers</div>
      ))}
    </div>
  );
}