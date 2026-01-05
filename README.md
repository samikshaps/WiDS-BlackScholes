# WiDS-BlackScholes
# Practice Repositories

This repository contains practice implementations of option pricing models written while learning the Black–Scholes framework and related numerical methods. Each sub-repository represents a different stage of learning, starting from basic formula implementation to more advanced models.

---

## repo1 – Black–Scholes Basics (Notebooks)

**Overview:**  
This repository focuses on understanding the Black–Scholes model through Jupyter notebooks. The goal is to build intuition about how option prices depend on different parameters.

**Files:**
- `BlackScholesImplementation.ipynb`  
  Implements the Black–Scholes formula for European call and put options and walks through the calculations step by step.
- `examples_usage.ipynb`  
  Uses the implemented functions with different input values to observe how option prices change.

---

## repo2 – Black–Scholes, Greeks, and Monte Carlo

**Overview:**  
This repository moves from notebooks to modular Python scripts. It includes pricing, Greek calculations, and a Monte Carlo approach for comparison.

**Files:**
- `black_scholes.py`  
  Contains functions to compute European call and put prices using the Black–Scholes formula.
- `calculate_greeks.py`  
  Computes option Greeks such as Delta, Gamma, Vega, Theta, and Rho.
- `greeks_analysis.py`  
  Uses the Greek functions to study how sensitivities change with different parameters.
- `monte_carlo.py`  
  Implements Monte Carlo simulation to price options by simulating stock price paths.
- `user_input.py`  
  Handles user inputs for parameters like stock price, strike price, volatility, and maturity.

---

## repo3 – Advanced Option Pricing Models

**Overview:**  
This repository explores multiple option pricing methods and compares them with Black–Scholes. It also introduces stochastic volatility.

**Files:**
- `black_scholes.py`  
  Standard Black–Scholes implementation used as a reference model.
- `binomial_tree.py`  
  Prices options using the binomial tree method.
- `monte_carlo.py`  
  Monte Carlo simulation for option pricing.
- `greeks.py`  
  Calculates Greeks for the implemented pricing models.
- `heston.py`  
  Implements the Heston model with stochastic volatility.
- `volatality.py`  
  Studies the effect of volatility on option prices.

---

This repository was created as part of practice and learning in quantitative finance and derivative pricing.
