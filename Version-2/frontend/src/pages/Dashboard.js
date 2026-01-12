import React, { useEffect, useState } from "react";
import { getAnalytics } from "../api/api";

function Dashboard() {
  const [analytics, setAnalytics] = useState(null);

  useEffect(() => {
    fetchAnalytics();
  }, []);

  const fetchAnalytics = async () => {
    const data = await getAnalytics();
    setAnalytics(data);
  };

  if (!analytics) return <div>Loading...</div>;

  return (
    <div>
      <h2 className="text-xl font-bold mb-4">Dashboard</h2>
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div className="bg-white p-4 shadow rounded">
          <p className="text-gray-500">Total Crimes</p>
          <p className="text-2xl font-bold">{analytics.total_crimes}</p>
        </div>
        <div className="bg-white p-4 shadow rounded">
          <p className="text-gray-500">Solved Cases</p>
          <p className="text-2xl font-bold">{analytics.solved_cases}</p>
        </div>
        <div className="bg-white p-4 shadow rounded">
          <p className="text-gray-500">Pending Cases</p>
          <p className="text-2xl font-bold">{analytics.pending_cases}</p>
        </div>
        <div className="bg-white p-4 shadow rounded">
          <p className="text-gray-500">Officers Available</p>
          <p className="text-2xl font-bold">{analytics.available_officers}</p>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
