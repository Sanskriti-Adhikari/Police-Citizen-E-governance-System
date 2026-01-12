import React, { useEffect, useState } from "react";
import { getHolidays, requestHoliday } from "../api/api";

function Holidays() {
  const [holidays, setHolidays] = useState([]);
  const [form, setForm] = useState({ officer_id: "", start_date: "", end_date: "", reason: "" });

  useEffect(() => {
    fetchHolidays();
  }, []);

  const fetchHolidays = async () => {
    const data = await getHolidays();
    setHolidays(data);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await requestHoliday({
      officer_id: parseInt(form.officer_id),
      start_date: form.start_date,
      end_date: form.end_date,
      reason: form.reason,
    });
    fetchHolidays();
  };

  return (
    <div>
      <h2 className="text-xl font-bold mb-4">Holiday Requests</h2>
      <form onSubmit={handleSubmit} className="mb-4 bg-white p-4 shadow rounded grid grid-cols-1 md:grid-cols-2 gap-4">
        <input
          type="number"
          placeholder="Officer ID"
          value={form.officer_id}
          onChange={(e) => setForm({ ...form, officer_id: e.target.value })}
          className="p-2 border rounded"
        />
        <input
          type="date"
          placeholder="Start Date"
          value={form.start_date}
          onChange={(e) => setForm({ ...form, start_date: e.target.value })}
          className="p-2 border rounded"
        />
        <input
          type="date"
          placeholder="End Date"
          value={form.end_date}
          onChange={(e) => setForm({ ...form, end_date: e.target.value })}
          className="p-2 border rounded"
        />
        <input
          type="text"
          placeholder="Reason"
          value={form.reason}
          onChange={(e) => setForm({ ...form, reason: e.target.value })}
          className="p-2 border rounded"
        />
        <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded col-span-full">
          Request Holiday
        </button>
      </form>

      <div className="bg-white p-4 shadow rounded">
        <table className="min-w-full border border-gray-200">
          <thead className="bg-gray-100">
            <tr>
              <th className="p-2 border-b">ID</th>
              <th className="p-2 border-b">Officer</th>
              <th className="p-2 border-b">Start</th>
              <th className="p-2 border-b">End</th>
              <th className="p-2 border-b">Reason</th>
              <th className="p-2 border-b">Status</th>
            </tr>
          </thead>
          <tbody>
            {holidays.map((h) => (
              <tr key={h.id} className="hover:bg-gray-50">
                <td className="p-2 border-b">{h.id}</td>
                <td className="p-2 border-b">{h.officer_name}</td>
                <td className="p-2 border-b">{h.start_date.split("T")[0]}</td>
                <td className="p-2 border-b">{h.end_date.split("T")[0]}</td>
                <td className="p-2 border-b">{h.reason}</td>
                <td className="p-2 border-b">{h.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Holidays;
