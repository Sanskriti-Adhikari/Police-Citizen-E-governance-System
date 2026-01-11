import React from "react";

function Notification({ message }) {
  return (
    <div className="bg-green-100 border border-green-400 text-green-700 p-2 rounded mb-2">
      {message}
    </div>
  );
}

export default Notification;
