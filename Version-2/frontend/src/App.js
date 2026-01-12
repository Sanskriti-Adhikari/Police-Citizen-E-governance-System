import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import CriminalRecords from "./pages/CriminalRecords";
import Officers from "./pages/Officers";
import Holidays from "./pages/Holidays";
import Allocation from "./pages/Allocation";
import Header from "./components/Header";
import Sidebar from "./components/Sidebar";

function App() {
  return (
    <Router>
      <div className="flex h-screen">
        <Sidebar />
        <div className="flex-1 flex flex-col">
          <Header />
          <main className="p-4 flex-1 overflow-auto">
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/records" element={<CriminalRecords />} />
              <Route path="/officers" element={<Officers />} />
              <Route path="/holidays" element={<Holidays />} />
              <Route path="/allocation" element={<Allocation />} />
            </Routes>
          </main>
        </div>
      </div>
    </Router>
  );
}

export default App;
