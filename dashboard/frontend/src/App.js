import React, { useEffect, useState } from "react";
import { fetchSummary } from "./api/client";
import SummaryCard from "./components/SummaryCard";

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
      {summary ? <SummaryCard summary={summary} /> : <p>Loading...</p>}
    </div>
  );
}

export default App;
