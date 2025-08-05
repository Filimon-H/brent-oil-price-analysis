import React from "react";

export default function SummaryCard({ summary }) {
  return (
    <div style={styles.card}>
      <h2>🧠 Change Point Summary</h2>
      <p><strong>📅 Change Date:</strong> {summary.change_point_date}</p>
      <p><strong>📈 Mu Before:</strong> {summary.mu_before.toFixed(5)}</p>
      <p><strong>📉 Mu After:</strong> {summary.mu_after.toFixed(5)}</p>
      <p><strong>🔻 ΔMu:</strong> {(summary.delta_mu).toFixed(5)}</p>
      <p><strong>σ Before:</strong> {summary.sigma_before.toFixed(5)}</p>
      <p><strong>σ After:</strong> {summary.sigma_after.toFixed(5)}</p>
      <p><strong>ΔSigma:</strong> {(summary.delta_sigma).toFixed(5)}</p>
    </div>
  );
}

const styles = {
  card: {
    border: "1px solid #ccc",
    borderRadius: "10px",
    padding: "20px",
    margin: "20px auto",
    maxWidth: "600px",
    backgroundColor: "#f9f9f9",
  },
};
