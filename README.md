
# 📊 Brent Oil Price Change Point Analysis

This project analyzes the historical fluctuations in Brent oil prices using **Bayesian Change Point Modeling** to identify significant shifts in market behavior. The goal is to align these shifts with **major geopolitical or economic events** and provide insight into the underlying structural changes.

---
brent-oil-price-analysis/
│
├── data/ # Raw and processed datasets
├── dashboard/
│ ├── app.py # Flask backend server
│ ├── routes/ # API route logic (change point, trends, events)
│ └── frontend/ # React frontend (UI components and charts)
├── models/ # Bayesian model scripts & traces
├── notebooks/ # EDA and PyMC modeling notebooks
└── README.md # You are here

yaml
Copy
Edit

---

## 🚀 Features

### ✅ Task 1: Exploratory Data Analysis (EDA)
- Summary statistics and trend inspection.
- Price spikes and drops visually explored.
- Missing data handling and transformation.

### ✅ Task 2: Bayesian Change Point Detection
- Used `PyMC` to model oil price returns.
- Identified change points (e.g., 2008–2009 financial crisis).
- Posterior distributions visualized with `arviz`.

### ✅ Task 3: Interactive Dashboard (Flask + React)
#### 📈 Key Functionalities:
- **Historical Price Trends** with toggleable key event highlights.
- **Date Range Filtering** to drill into specific time windows.
- **Volatility Visualization** with moving standard deviation.
- **Event Impact Table** showing avg. price change before/after events.
- **Forecasting Toggle** using Linear Regression and Optional Bayesian Forecast.
- **Change Point Summary Cards** with μ/σ changes before & after.

---

## 🌐 Live Demo (if hosted)
> Not hosted publicly. Run locally using the setup instructions below.

---

## 🧠 Tech Stack

| Layer         | Tools Used                         |
|---------------|-------------------------------------|
| Data Analysis | Python, Pandas, PyMC, ArviZ         |
| API Server    | Flask, Flask-CORS                   |
| Frontend UI   | React, Chart.js, Recharts, CSS      |
| Visualization | Chart.js with annotations, tooltips |
| State Mgmt    | React Hooks (`useState`, `useEffect`) |

---

## 🛠 Setup Instructions

### 1. Clone and install Python backend
```bash
git clone https://github.com/your-username/brent-oil-price-analysis.git
cd brent-oil-price-analysis/dashboard
python -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
pip install -r requirements.txt
2. Run Flask backend
bash
Copy
Edit
cd dashboard
python app.py
3. Install and run React frontend
bash
Copy
Edit
cd frontend
npm install
npm start
The app will be available at: http://localhost:3000

📂 Datasets
BrentOilPrices.csv: Historical daily prices from 2000 onward.

key_events.csv: Manually curated global events with timestamps.

volatility.csv: Rolling standard deviation for each date.

bayesian_trace.nc: PyMC-generated posterior samples.

📊 Sample UI Screenshots
Price Trend + Events	Forecast Toggle	Change Point Summary

📈 Future Directions
Feature	Description
📅 Multi-Change Point	Display and compare several change points.
🧠 Bayesian Forecast	Extend forecasting using posterior sampling.
🔍 Event Filtering	Filter events by category or severity.
🧾 Export Reports	Export event impact summaries to PDF/CSV.

🤝 Contributing
Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.

📄 License
MIT

👨‍💻 Author
Filimon Hailemariam · AI Intern @ 10 Academy · LinkedIn · GitHub

