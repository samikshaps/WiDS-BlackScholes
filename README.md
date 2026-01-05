# WiDS-BlackScholes
# Practice Repositories

Three repositories were covered by practicing those code files which included the relevant concepts. Files that take user input, use streamlit, code for visualisation with mathplotlib or plotly were ignored for this practice.

---

## repo1 – Basic Black Scholes code

**Overview:**  
This set of codes is mainly for understanding and coding the Black–Scholes model with python notebook. The main idea is to get intuition about how option prices depend on different parameters.

**Files:**
- `BlackScholesImplementation.ipynb`  
  Implements the Black–Scholes formula for European call and put options and walks through the calculations step by step by extracting and using all necessary parameters. Greeks for call and put option were also calculated separately. 
- `examples_usage.ipynb`  
 This file is just to see how the previous code can be used. It uses the implemented functions with different input values to see how option prices change for different values of the parameters.

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
