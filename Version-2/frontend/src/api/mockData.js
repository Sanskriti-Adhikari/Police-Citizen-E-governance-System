export const mockData = {
  records: [
    {
      id: 1,
      criminal_name: "John Doe",
      crime_type: "Theft",
      severity: "Medium",
      status: "Under Investigation",
      location: "Downtown",
      description: "Shoplifting incident at local store",
      created_at: "2025-01-01T10:00:00",
      priority: 2,
      officer_assigned: "Officer Smith"
    },
    {
      id: 2,
      criminal_name: "Jane Smith",
      crime_type: "Assault",
      severity: "High",
      status: "Pending",
      location: "Northside",
      description: "Physical altercation reported",
      created_at: "2025-01-02T14:30:00",
      priority: 1,
      officer_assigned: "Officer Johnson"
    }
  ],
  officers: [
    { id: 1, name: "Officer Smith", badge_id: "B001", status: "Available", area: "Downtown", contact: "555-0101" },
    { id: 2, name: "Officer Johnson", badge_id: "B002", status: "On Duty", area: "Northside", contact: "555-0102" }
  ],
  analytics: {
    total_crimes: 145,
    solved_cases: 89,
    pending_cases: 42,
    under_investigation: 14,
    total_officers: 24,
    available_officers: 18
  },
  heatmapData: [
    { area: "Downtown", crimes: 45 },
    { area: "Northside", crimes: 32 }
  ]
};
