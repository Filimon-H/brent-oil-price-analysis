import React, { useEffect, useState } from "react";
import { fetchSummary } from "./api/client";
import SummaryCard from "./components/SummaryCard";
import HistoricalChart from "./components/HistoricalChart";
import VolatilityChart from "./components/VolatilityChart";
import EventImpactTable from "./components/EventImpactTable";

function App() {
  const [summary, setSummary] = useState(null);

  useEffect(() => {
    fetchSummary()
      .then((res) => setSummary(res.data))
      .catch((err) => console.error("Failed to fetch summary", err));
  }, []);

  return (
    <div className="App">
      <h1 style={{ textAlign: "center", paddingTop: "20px" }}>
        🛢 Brent Oil Change Point Dashboard
      </h1>

      {/* Summary card */}
      {summary ? <SummaryCard summary={summary} /> : <p>Loading summary...</p>}

      {/* Historical price chart with filters and event toggle */}
      <HistoricalChart />

      {/* Volatility visualization */}
      <VolatilityChart />

      {/* 📊 Average price change around events */}
      <EventImpactTable />
    </div>
  );
}

export default App;
