import React, { useEffect, useState } from "react";
import Table from "../components/Table";
import { getCriminalRecords, deleteCriminalRecord } from "../api/api";

function CriminalRecords() {
  const [records, setRecords] = useState([]);

  useEffect(() => {
    fetchRecords();
  }, []);

  const fetchRecords = async () => {
    const data = await getCriminalRecords();
    setRecords(data);
  };

  const handleDelete = async (id) => {
    if (window.confirm("Are you sure to delete this record?")) {
      await deleteCriminalRecord(id);
      fetchRecords();
    }
  };

  const columns = [
    "id",
    "criminal_name",
    "crime_type",
    "severity",
    "status",
    "location",
    "officer_assigned",
    "priority",
  ];

  return (
    <div>
      <h2 className="text-xl font-bold mb-4">Criminal Records</h2>
      <Table columns={columns} data={records} />
      <div className="mt-4">
        {records.map((r) => (
          <button
            key={r.id}
            onClick={() => handleDelete(r.id)}
            className="bg-red-600 text-white px-2 py-1 rounded mr-2"
          >
            Delete {r.criminal_name}
          </button>
        ))}
      </div>
    </div>
  );
}

export default CriminalRecords;
