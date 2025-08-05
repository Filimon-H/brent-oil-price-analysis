import React from "react";

const EventModal = ({ event, onClose }) => {
  if (!event) return null;

  return (
    <div style={{
      position: "fixed",
      top: "0", left: "0", width: "100%", height: "100%",
      backgroundColor: "rgba(0,0,0,0.4)", display: "flex",
      justifyContent: "center", alignItems: "center", zIndex: 1000
    }}>
      <div style={{
        background: "#fff", padding: "20px", borderRadius: "8px",
        width: "400px", boxShadow: "0 2px 10px rgba(0,0,0,0.3)"
      }}>
        <h3>📌 Event Details</h3>
        <p><strong>Date:</strong> {event.date}</p>
        <p><strong>Event:</strong> {event.label}</p>
        <p><strong>Category:</strong> {event.category || "N/A"}</p>

        <button
          onClick={onClose}
          style={{ marginTop: "10px", padding: "8px 16px", background: "#007bff", color: "#fff", border: "none", borderRadius: "4px" }}
        >
          Close
        </button>
      </div>
    </div>
  );
};

export default EventModal;
