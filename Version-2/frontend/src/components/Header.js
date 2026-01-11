import React from "react";

function Header() {
  return (
    <header className="bg-white shadow p-4 flex justify-between items-center">
      <h1 className="text-xl font-bold text-gray-800">Police Admin Dashboard</h1>
      <div>
        <button className="bg-blue-600 text-white px-3 py-1 rounded">Logout</button>
      </div>
    </header>
  );
}

export default Header;
