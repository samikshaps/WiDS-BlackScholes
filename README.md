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

# 🚀 Final Project: Option Pricing using Black–Scholes and Monte Carlo Simulation (CEV Model)

## Overview

The final project integrates analytical Black–Scholes pricing with Monte Carlo simulation under a Constant Elasticity of Variance (CEV) framework to study European call options under different volatility regimes. In addition to pricing, the project implements implied volatility estimation and statistical confidence intervals, allowing direct comparison between closed-form theory and stochastic simulation.

The complete pipeline was implemented in Python using NumPy, SciPy, Matplotlib, and Pandas.

Baseline parameters:

- Initial stock price: S0 = 100  
- Risk-free rate: r = 0.02  
- Volatility: σ = 0.2  
- Time to maturity: T = 1 year  
- Monte Carlo paths: 50,000  
- Time steps: 252 (daily)

---

## Methodology

### 1. Analytical Black–Scholes Pricing

A custom `bs_call()` function computes European call prices using the standard Black–Scholes closed-form formula. This serves as a benchmark for validating Monte Carlo results.

The quantities d1 and d2 are evaluated using logarithmic returns and volatility-scaled time, and cumulative normal distributions are obtained from SciPy.

---

### 2. CEV Stock Price Simulation

Stock dynamics are modeled using the Constant Elasticity of Variance (CEV) stochastic differential equation:

dS = rS dt + σ S^γ dW

where γ controls how volatility depends on the stock price.

The equation is discretized using the Euler–Maruyama method. Random Gaussian shocks drive the stochastic component, and a small numerical floor is applied to prevent negative stock prices.

---

### 3. Monte Carlo Option Pricing

European call option prices are estimated via Monte Carlo by:

1. Simulating stock paths  
2. Computing terminal payoff: max(ST − K, 0)  
3. Discounting using exp(-rT)  
4. Taking the mean over all paths  

Standard error and 95% confidence intervals are computed to quantify statistical uncertainty.

---

### 4. Implied Volatility Estimation

Given simulated option prices, implied volatility is recovered using Brent’s root-finding algorithm from SciPy. The solver iteratively finds the volatility that reproduces the observed price under Black–Scholes.

Safeguards are included to handle deep ITM/OTM cases and unreasonable inputs.

---

## Key Quantitative Results

Monte Carlo pricing was performed using 50,000 paths and 252 time steps for an at-the-money call (K = 100):

- γ = 0.5 → Call price ≈ 2.14 (tight CI ≈ 0.03)  
- γ = 1.0 → Call price ≈ 8.91, closely matching analytical BS value (8.916)  
- γ = 1.5 → Call price ≈ 8.33 with large variance  

For γ = 1.0, Monte Carlo differed from Black–Scholes by only 0.07%, validating the simulator.

Path statistics:

- γ = 0.5: Std ≈ 2.02 (tight clustering)  
- γ = 1.0: Std ≈ 20.56 (standard GBM behavior)  
- γ = 1.5: Extreme variance and explosive paths  

These results show how γ fundamentally controls volatility structure and tail behavior.

---

## Volatility Smile and Leverage Effect

Implied volatility was computed across multiple strikes using γ = 0.8:

- K = 85 → IV ≈ 6.6%  
- K = 100 → IV ≈ 7.9%  
- K = 115 → IV ≈ 7.8%  

A clear negative skew was observed, with the put wing steeper than the call wing.

This arises from the leverage effect embedded in CEV when γ < 1: volatility increases as price decreases. Consequently, downside options become more expensive, producing realistic volatility skew, something Black–Scholes cannot capture due to its constant-volatility assumption.

---

## Implementation Challenges

- Low γ instability:  
  For γ = 0.5, stock dispersion became very small, causing intrinsic-value saturation and implied volatility failures.

- High γ variance:  
  For γ = 1.5, extreme outliers produced massive variance and wide confidence intervals.

- Implied volatility convergence:  
  Brent’s method occasionally failed for deep ITM/OTM strikes, requiring bounds checking.

- Model tradeoff:  
  Lower γ gives stronger skew but poorer numerical stability. A compromise value of γ = 0.8 was selected.

These challenges reflect real-world quantitative modeling tradeoffs between realism and robustness.

---

## Practical Significance

This project demonstrates that volatility smiles are not arbitrary artifacts but emerge naturally from state-dependent volatility dynamics. While Black–Scholes predicts a flat implied volatility surface, the CEV model reproduces market-observed skew.

From a trading perspective, this explains why downside protection is expensive. From a modeling perspective, it highlights the necessity of moving beyond constant-volatility assumptions for realistic derivative pricing.

---

## Summary

This final project bridges theory and computation by combining:

- Black–Scholes analytical pricing  
- Monte Carlo simulation  
- CEV stochastic dynamics  
- Implied volatility extraction  

It provides a complete quantitative finance workflow, demonstrating how classical models can be extended using numerical methods to capture real market behavior.



