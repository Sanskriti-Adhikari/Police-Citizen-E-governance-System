import React, { useEffect, useState } from "react";
import Table from "../components/Table";
import { getOfficers, deleteOfficer } from "../api/api";

function Officers() {
  const [officers, setOfficers] = useState([]);

  useEffect(() => {
    fetchOfficers();
  }, []);

  const fetchOfficers = async () => {
    const data = await getOfficers();
    setOfficers(data);
  };

  const handleDelete = async (id) => {
    if (window.confirm("Are you sure to delete this officer?")) {
      await deleteOfficer(id);
      fetchOfficers();
    }
  };

  const columns = ["id", "name", "badge_id", "status", "area", "contact"];

  return (
    <div>
      <h2 className="text-xl font-bold mb-4">Officers</h2>
      <Table columns={columns} data={officers} />
      <div className="mt-4">
        {officers.map((o) => (
          <button
            key={o.id}
            onClick={() => handleDelete(o.id)}
            className="bg-red-600 text-white px-2 py-1 rounded mr-2"
          >
            Delete {o.name}
          </button>
        ))}
      </div>
    </div>
  );
}

export default Officers;
