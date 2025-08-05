import React, { useEffect, useState } from "react";
import { fetchEventImpacts } from "../api/client";

const EventImpactTable = () => {
  const [impacts, setImpacts] = useState([]);

  useEffect(() => {
    fetchEventImpacts()
      .then((res) => setImpacts(res.data))
      .catch((err) => console.error("Error fetching impact data:", err));
  }, []);

  return (
    <div style={{ width: "95%", margin: "20px auto" }}>
      <h2 style={{ textAlign: "center" }}>
        📊 Average Price Change Around Key Events
      </h2>
      <table style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr>
            <th>Date</th>
            <th>Event</th>
            <th>Category</th>
            <th>Avg Before</th>
            <th>Avg After</th>
            <th>Change (%)</th>
          </tr>
        </thead>
        <tbody>
          {impacts.map((row, idx) => (
            <tr key={idx}>
              <td>{row.date}</td>
              <td>{row.event}</td>
              <td>{row.category}</td>
              <td>${row.avg_before}</td>
              <td>${row.avg_after}</td>
              <td
                style={{
                  color: row.pct_change > 0 ? "green" : "red",
                  fontWeight: "bold",
                }}
              >
                {row.pct_change}%
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default EventImpactTable;
