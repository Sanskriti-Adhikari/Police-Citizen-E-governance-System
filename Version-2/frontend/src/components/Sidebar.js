import React from "react";
import { NavLink } from "react-router-dom";

const links = [
  { name: "Dashboard", path: "/" },
  { name: "Criminal Records", path: "/records" },
  { name: "Officers", path: "/officers" },
  { name: "Holidays", path: "/holidays" },
  { name: "Allocation", path: "/allocation" }
];

function Sidebar() {
  return (
    <aside className="w-60 bg-gray-800 text-white flex flex-col">
      <div className="p-4 text-2xl font-bold">Police Admin</div>
      <nav className="flex-1 flex flex-col">
        {links.map(link => (
          <NavLink
            key={link.name}
            to={link.path}
            className={({ isActive }) => `p-3 hover:bg-gray-700 ${isActive ? "bg-gray-700" : ""}`}
          >
            {link.name}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}

export default Sidebar;
