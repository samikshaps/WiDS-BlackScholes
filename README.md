# WiDS-Simulation and Quantitative Analysis of the Black Scholes Model Using Python
# Practice Repositories

Three repositories were covered by practicing those code files which included the relevant concepts. Files that take user input, use streamlit, code for visualisation with mathplotlib or plotly were ignored for this practice.

---

## repo1 – Basic Black Scholes code

**Overview:**  
This set of codes is mainly for understanding and coding the Black–Scholes model with python notebook. The aim is to understand the working of the mathematical formulation of the model and study the dependence of option prices and Greeks on key parameters.

**Files:**
- `BlackScholesImplementation.ipynb`  
  Implements the Black–Scholes formula for European call and put options and walks through the calculations step by step by extracting and using all necessary parameters. Greeks for call and put option were also calculated separately. 
- `examples_usage.ipynb`  
 This file is just to see how the previous code can be used. It uses the implemented functions with different input values to see how option prices change for different values of the parameters.

---

## repo2 – Black–Scholes, Greeks and Monte Carlo Simulation

**Overview:**  
This set of codes focuses on implementing the Black–Scholes model in a more structured Python format. It also includes the calculation of option Greeks and option pricing using Monte Carlo simulation.

**Files:**
- `black_scholes.py`  
  Contains functions to compute European call and put option prices using the Black–Scholes formula based on the given input parameters. This is similar to the code from the previous BS model code.
- `calculate_greeks.py`  
  Computes using formulas to calculate option Greeks such as Delta, Gamma, Vega, Theta, and Rho for both call and put options.
- `greeks_analysis.py`  
  Uses the Greek calculation functions to study how option sensitivities change with respect to different parameters like volatility, time, and stock price.
- `monte_carlo.py`  
  Learnt the working of Monte Carlo simulation with the help of the reference code. It implements Monte Carlo simulation to price options by simulating multiple stock price paths (assuming different financial worlds) and estimating the expected payoff by taking into account all such possible paths. 
- `user_input.py`  
  Takes user inputs for option parameters such as stock price, strike price, volatility, risk-free rate and time to maturity.

---

## repo3 – Advanced Option Pricing Models

**Overview:**  
This set of codes has different option pricing models and compares them with the Black–Scholes model framework. It also has the codes stochastic volatility models.

**Files:**
- `black_scholes.py`  
  Implements the standard Black–Scholes formula for pricing European call and put options. This file is mainly used as a reference model to compare results obtained from other pricing methods. Again, this code remains similar to the previous ones. 
- `binomial_tree.py`  
  This implements the binomial tree method for option pricing by modeling the stock price evolution in discrete time steps (this is somewhat similar to black scholes model working but it is its discrete time counterpart) and computing option values by collapsing the binary tree level by level backward. 
- `monte_carlo.py`  
  The option prices were determined using Monte Carlo simulation by generating multiple random price paths and estimating the option value using the average discounted payoff.
- `greeks.py`  
  It computes the option Greeks such as Delta, Gamma, Vega, Theta and Rho that measure the sensitivity of option prices with respect to different parameters.
- `heston.py`  
  It implements Heston stochastic volatility model, where both the stock price and volatility evolve over time (unlike the black scholes model where only the stock price changed with time and volatality was treated as a constant). This allows for more realistic option pricing. 
- `volatality.py`  
  This is to analyze how changes in volatility affect option prices. The file covers both historical volatility and implied volatility and also compares the behaviour of different pricing models with different volatility levels.

---


