import React, { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";
import { fetchVolatility } from "../api/client";

function VolatilityChart() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetchVolatility()
      .then((res) => setData(res.data))
      .catch((err) => console.error("Failed to fetch volatility", err));
  }, []);

  if (!data) return <p>Loading Volatility Chart...</p>;

  const chartData = {
    labels: data.dates,
    datasets: [
      {
        label: "30-Day Rolling Volatility",
        data: data.volatility,
        borderColor: "orange",
        fill: false,
        tension: 0.1,
        pointRadius: 0,
      },
    ],
  };

  return (
    <div style={{ width: "90%", margin: "auto", paddingTop: "40px" }}>
      <h2 style={{ textAlign: "center" }}>📊 Brent Oil Volatility (σ) Over Time</h2>
      <Line data={chartData} />
    </div>
  );
}

export default VolatilityChart;
