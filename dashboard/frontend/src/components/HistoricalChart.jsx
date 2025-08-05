import React, { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";
import { fetchPriceTrend } from "../api/client";
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement, Tooltip, Legend);

const HistoricalChart = () => {
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    fetchPriceTrend()
      .then((res) => {
        const { dates, prices } = res.data;

        const data = {
          labels: dates,
          datasets: [
            {
              label: "Brent Oil Price",
              data: prices,
              fill: false,
              borderColor: "#007bff",
              tension: 0.1,
            },
          ],
        };

        setChartData(data);
      })
      .catch((err) => {
        console.error("Error fetching price trend:", err);
      });
  }, []);

  if (!chartData) return <p>Loading price trend...</p>;

  return (
    <div style={{ width: "95%", maxWidth: "1000px", margin: "30px auto" }}>
      <h2 style={{ textAlign: "center" }}>📈 Brent Oil Historical Price Trend</h2>
      <Line data={chartData} />
    </div>
  );
};

export default HistoricalChart;
