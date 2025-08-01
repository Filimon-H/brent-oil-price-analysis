# src/change_point_model.py

import pymc as pm
import numpy as np
import pandas as pd
import arviz as az

def run_bayesian_change_point_model(data: pd.Series, draws=1000, tune=1000, seed=42):
    """
    Build and sample a Bayesian change point model on time series data.

    Args:
        data (pd.Series): Stationary 1D time series (e.g., log returns)
        draws (int): Number of samples to draw from posterior
        tune (int): Tuning steps
        seed (int): Random seed for reproducibility

    Returns:
        model (pm.Model): PyMC model object
        trace (arviz.InferenceData): Posterior samples
    """
    data = data.dropna().values
    n = len(data)

    with pm.Model() as model:
        # 🔁 Prior for changepoint (discrete day index)
        tau = pm.DiscreteUniform("tau", lower=0, upper=n)

        # 📊 Priors for mean and std before and after the change
        mu1 = pm.Normal("mu1", mu=0, sigma=1)
        mu2 = pm.Normal("mu2", mu=0, sigma=1)

        sigma1 = pm.HalfNormal("sigma1", sigma=1)
        sigma2 = pm.HalfNormal("sigma2", sigma=1)

        # ⛓ Switch between pre- and post-changepoint parameters
        mu = pm.math.switch(tau >= np.arange(n), mu1, mu2)
        sigma = pm.math.switch(tau >= np.arange(n), sigma1, sigma2)

        # 📈 Likelihood
        obs = pm.Normal("obs", mu=mu, sigma=sigma, observed=data)

        # 🧠 Run MCMC
        trace = pm.sample(draws=draws, tune=tune, random_seed=seed, return_inferencedata=True)

    return model, trace
