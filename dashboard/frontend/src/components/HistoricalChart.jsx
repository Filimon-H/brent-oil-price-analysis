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
import annotationPlugin from "chartjs-plugin-annotation";

// 📌 Register chart elements and plugin
ChartJS.register(
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Tooltip,
  Legend,
  annotationPlugin
);

const HistoricalChart = () => {
  const [chartData, setChartData] = useState(null);
  const [startDate, setStartDate] = useState("2000-01-01");
  const [endDate, setEndDate] = useState("2022-12-31");
  const [showEvents, setShowEvents] = useState(true);

  const fetchData = () => {
    fetchPriceTrend(startDate, endDate, showEvents)
      .then((res) => {
        const { dates, prices, events = [] } = res.data;

        const mainDataset = {
          label: "Brent Oil Price",
          data: prices,
          fill: false,
          borderColor: "#007bff",
          tension: 0.1,
          pointRadius: 1,
        };

        // 🔴 Red lines for visual annotation
        const annotations = {};
        const eventPoints = [];

        if (showEvents && events.length) {
          events.forEach((e, idx) => {
            annotations[`event-${idx}`] = {
              type: "line",
              xMin: e.date,
              xMax: e.date,
              borderColor: "red",
              borderWidth: 1.2,
              label: { enabled: false },
            };

            // ⛳ Invisible points for tooltip
            eventPoints.push({
              x: e.date,
              y: e.y !== null ? e.y : null,
              eventLabel: e.label,
            });
          });
        }

        // ➕ Dataset for tooltip interaction
        const eventDataset = {
          label: "Event",
          data: eventPoints,
          pointRadius: 6,
          backgroundColor: "rgba(255,0,0,0.5)",
          borderWidth: 0,
          showLine: false,
          parsing: {
            xAxisKey: "x",
            yAxisKey: "y",
          },
          pointHoverRadius: 8,
          pointHitRadius: 20,
        };

        const data = {
          labels: dates,
          datasets: [mainDataset, ...(showEvents ? [eventDataset] : [])],
        };

        const options = {
          responsive: true,
          plugins: {
            legend: { display: true },
            annotation: { annotations },
            tooltip: {
              callbacks: {
                label: function (context) {
                  const point = context.raw;
                  if (point?.eventLabel) {
                    return `📌 ${point.eventLabel}`;
                  }
                  return `💰 $${context.parsed.y}`;
                },
              },
            },
          },
          scales: {
            x: { ticks: { maxTicksLimit: 15 } },
            y: { beginAtZero: false },
          },
        };

        setChartData({ data, options });
      })
      .catch((err) => {
        console.error("Error fetching price trend:", err);
      });
  };

  useEffect(() => {
    fetchData();
  }, [startDate, endDate, showEvents]);

  if (!chartData) return <p>Loading chart...</p>;

  return (
    <div style={{ width: "95%", maxWidth: "1000px", margin: "30px auto" }}>
      <h2 style={{ textAlign: "center" }}>
        📈 Brent Oil Historical Price Trend
      </h2>

      <div style={{ textAlign: "center", marginBottom: "15px" }}>
        <label>
          Start Date:{" "}
          <input
            type="date"
            value={startDate}
            onChange={(e) => setStartDate(e.target.value)}
            style={{ marginRight: "20px" }}
          />
        </label>
        <label>
          End Date:{" "}
          <input
            type="date"
            value={endDate}
            onChange={(e) => setEndDate(e.target.value)}
            style={{ marginRight: "20px" }}
          />
        </label>
        <label>
          <input
            type="checkbox"
            checked={showEvents}
            onChange={() => setShowEvents(!showEvents)}
          />
          {"  "}Show Events
        </label>
      </div>

      <Line data={chartData.data} options={chartData.options} />
    </div>
  );
};

export default HistoricalChart;
