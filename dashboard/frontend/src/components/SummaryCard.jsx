import React from "react";
import { FaCalendarAlt, FaChartLine, FaArrowDown } from "react-icons/fa";
import { GiBrain } from "react-icons/gi";
import { BiScatterChart } from "react-icons/bi";

const SummaryCard = ({ summary }) => {
  if (!summary) return null;

  return (
    <div
      style={{
        maxWidth: "600px",
        margin: "30px auto",
        padding: "25px 30px",
        borderRadius: "16px",
        backgroundColor: "#ffffff",
        boxShadow: "0 8px 20px rgba(0, 0, 0, 0.08)",
        border: "1px solid #eaeaea",
      }}
    >
      <h2 style={{ fontSize: "1.5rem", marginBottom: "20px", textAlign: "center" }}>
        <GiBrain style={{ verticalAlign: "middle", marginRight: "10px", color: "#9333ea" }} />
        <span>Change Point Summary</span>
      </h2>

      <ul style={{ listStyle: "none", paddingLeft: 0, lineHeight: "2rem" }}>
        <li>
          <FaCalendarAlt style={{ color: "#0ea5e9", marginRight: "8px" }} />
          <strong>Change Date:</strong> {summary.change_date}
        </li>
        <li>
          <FaChartLine style={{ color: "#6366f1", marginRight: "8px" }} />
          <strong>Mu Before:</strong> {summary.mu_before}
        </li>
        <li>
          <FaChartLine style={{ color: "#ef4444", marginRight: "8px" }} />
          <strong>Mu After:</strong> {summary.mu_after}
        </li>
        <li>
          <FaArrowDown style={{ color: "#dc2626", marginRight: "8px" }} />
          <strong>ΔMu:</strong> {summary.delta_mu}
        </li>
        <li>
          <BiScatterChart style={{ color: "#16a34a", marginRight: "8px" }} />
          <strong>σ Before:</strong> {summary.sigma_before}
        </li>
        <li>
          <BiScatterChart style={{ color: "#f97316", marginRight: "8px" }} />
          <strong>σ After:</strong> {summary.sigma_after}
        </li>
        <li>
          <BiScatterChart style={{ color: "#a855f7", marginRight: "8px" }} />
          <strong>ΔSigma:</strong> {summary.delta_sigma}
        </li>
      </ul>
    </div>
  );
};

export default SummaryCard;
