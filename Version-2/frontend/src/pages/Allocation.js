import React, { useState } from "react";
import { allocateOfficers } from "../api/api";

function Allocation() {
  const [totalOfficers, setTotalOfficers] = useState(1);
  const [result, setResult] = useState(null);

  const handleAllocate = async () => {
    const data = await allocateOfficers({ total_officers: totalOfficers });
    setResult(data);
  };

  return (
    <div>
      <h2 className="text-xl font-bold mb-4">Officer Allocation</h2>
      <div className="mb-4 flex items-center gap-2">
        <input
          type="number"
          value={totalOfficers}
          onChange={(e) => setTotalOfficers(parseInt(e.target.value))}
          className="p-2 border rounded"
          min={1}
        />
        <button onClick={handleAllocate} className="bg-blue-600 text-white px-4 py-2 rounded">
          Allocate
        </button>
      </div>

      {result && (
        <div className="bg-white p-4 shadow rounded">
          <h3 className="font-bold mb-2">Allocation Result</h3>
          <table className="min-w-full border border-gray-200">
            <thead className="bg-gray-100">
              <tr>
                <th className="p-2 border-b">Area</th>
                <th className="p-2 border-b">Officers</th>
                <th className="p-2 border-b">Crime Rate</th>
              </tr>
            </thead>
            <tbody>
              {result.allocation.map((a, idx) => (
                <tr key={idx} className="hover:bg-gray-50">
                  <td className="p-2 border-b">{a.area}</td>
                  <td className="p-2 border-b">{a.officers}</td>
                  <td className="p-2 border-b">{a.crime_rate}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <p className="mt-2 font-bold">{result.recommendation}</p>
        </div>
      )}
    </div>
  );
}

export default Allocation;
