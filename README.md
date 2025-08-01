
# 📊 Brent Oil Price Change Point Analysis

This project analyzes the historical fluctuations in Brent oil prices using **Bayesian Change Point Modeling** to identify significant shifts in market behavior. The goal is to align these shifts with **major geopolitical or economic events** and provide insight into the underlying structural changes.

---

## 🚀 Project Overview

**Challenge**: Week 10 - 10 Academy AI Mastery Program
**Client**: Birhan Energies (Energy Sector Consultancy)
**Date Range**: July 30 – August 5, 2025

We use probabilistic modeling (via PyMC) to:

* Detect when structural breaks occur in oil prices
* Quantify the magnitude of change in return and volatility
* Compare model-detected change points with historical real-world events

---

## 📅 Data Sources

### 1. **Brent Oil Price Dataset**

* Source: Provided CSV (`BrentOilPrices.csv`)
* Frequency: Daily
* Range: May 20, 1987 – September 30, 2022
* Columns: `Date`, `Price`

### 2. **Key Global Events**

* Source: Manually compiled
* File: `key_events.csv`
* Columns: `event`, `start`, `end`, `category`
* Examples: Gulf War, COVID-19, OPEC cuts, financial crises

---

## 🧱 Tools and Technologies

* **Python 3.10+**
* **PyMC** (v4+) for Bayesian modeling
* **ArviZ** for posterior analysis
* **Matplotlib/Seaborn** for visualization
* **Pandas/Numpy** for data wrangling
---

## 🔄 Project Structure

```bash
brent-oil-price-analysis/
├── data/
│   ├── BrentOilPrices.csv
│   └── key_events.csv
├── notebooks/
│   ├── EDA.ipynb
│   └── modeling.ipynb
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── event_utils.py
│   └── change_point_model.py
├── README.md
└── requirements.txt
```

---

## 🥇 Key Features

* **Bayesian Change Point Detection** using log returns
* **Posterior inference** for tau (change date), mean, and volatility
* **Visual alignment** of detected changepoint with real-world events
* **Clear storytelling** in reports and future blog post
* **Interactive Dashboard** (under development)

---

## 🔍 How to Run

### 1. Install dependencies:

```bash
pip install -r requirements.txt
```

### 2. Run Jupyter notebooks:

```bash
jupyter notebook notebooks/EDA.ipynb
jupyter notebook notebooks/modeling.ipynb
```

## 📊 Example Insights

* Model detected a changepoint in March 2020 aligned with COVID-19 lockdowns.
* Post-change: mean returns dropped, volatility doubled.
* Likely market regime shift due to global demand collapse.


---

## 📄 License

MIT License — free for reuse with attribution.

---

## 🔗 References

* PyMC documentation: [https://www.pymc.io](https://www.pymc.io)
* ADF Test (statsmodels): [https://www.statsmodels.org](https://www.statsmodels.org)
* Oil Market Timeline: [https://en.wikipedia.org/wiki/Oil\_crisis](https://en.wikipedia.org/wiki/Oil_crisis)
