Interim Report – Task 1: Laying the Foundation for Analysis
Project: Change Point Analysis of Brent Oil Prices
Date: August 1, 2025
Prepared by: Filimon HAILEMARIAM

1.  Data Analysis Workflow
 Defined Phases and Rationale:
Phase 1: Data Loading and Cleaning
•	Load daily Brent oil price data (1987–2022) from CSV.
•	Convert Date to datetime format and sort chronologically.
Phase 2: Event Research and Compilation
•	Curated key_events.csv with 20+ global events relevant to oil prices.
•	Each event includes event, start, end, category, clearly describing geopolitical, economic, or OPEC-based events.
Phase 3: Exploratory Data Analysis (EDA)
•	Visualized raw price trends and volatility patterns.
•	Identified historical outliers and spikes.
Phase 4: Log Return Transformation & Stationarity
•	Transformed prices into log returns: log(price_t / price_{t-1}).
•	Conducted Augmented Dickey-Fuller (ADF) test to verify stationarity.
•	Outcome: log returns are stationary → suitable for modeling.
Phase 5: Event Alignment Preparation
•	Overlaid events on price timeline.
•	Created modular plotting utilities to visually match changepoints with key historical events.
Phase 6: Modeling Preparation
•	Designed a PyMC-based Bayesian model to detect a single changepoint.
•	Defined priors and switch logic for behavior shift in mean/volatility.
Phase 7: Communication Strategy
•	Final insights will be delivered via:
o	Medium-style blog post
o	Flask + React dashboard
o	GitHub repo for reproducibility

2.  Event Dataset Quality
•	The dataset includes 20 well-documented events.
•	Columns: event, start, end, category
•	Events include:
o	1990 Gulf War
o	2008 Global Financial Crisis
o	2020 COVID-19 lockdowns
o	2022 Russia-Ukraine conflict
•	Events were plotted on the Brent oil timeline for interpretability.
•	Dataset was cleaned, validated, and date parsed.
3.  Time Series Properties
•	Brent price series: non-stationary, long-term trend observed.
•	Log return series: stationary → verified by ADF test (p-value < 0.05).
•	Log returns used for modeling to satisfy statistical assumptions.
•	Volatility clustering observed, supporting segmentation by regime.
 
 
 
4. Assumptions and Limitations
•	Correlation ≠ Causation: Statistical changepoints are matched to real events, but no causal inference is claimed.
•	Subjective Event Selection: Manual curation may bias interpretation.
•	Single Changepoint Model: Initial model detects only one shift; future work may extend to multiple or hierarchical models.
•	Exogenous Variables Ignored: External macroeconomic data (GDP, inflation) not yet included.
5.  Purpose of Change Point Models
Change point models help detect structural breaks in the statistical behavior of time series.
•	In Brent oil prices, these reflect policy shocks, wars, or demand collapses.
•	The Bayesian approach allows:
o	Probabilistic reasoning about when a change occurred.
o	Modeling uncertainty in the shift.
o	Interpreting how mean and volatility changed post-event.
This enables investors and policymakers to better understand the impact of real-world disruptions on market regimes.
6. Deliverables So Far
•	EDA.ipynb: Time series EDA, log returns, ADF test
•	key_events.csv: Cleaned, structured geopolitical event dataset
•	src/: Modular functions for loading, preprocessing, and plotting
•	modeling.ipynb: Bayesian change point model
•	Visualizations: raw prices, log returns, and event overlays

7.  Next Steps
•	Finalize changepoint interpretation and event alignment
•	Build interactive dashboard



