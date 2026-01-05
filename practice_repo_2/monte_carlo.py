
import numpy as np
from src.utils.user_input import UserInput

#monte carlo simulation:
#Instead of using a closed-form formula, we simulate many possible future stock price paths, calculate the option payoff in each case and average them out

def monte_carlo_simulation(option_type, S, K, T, r, sigma, q=0, num_simulations=10000, random_numbers=None):

    # check inputs and raise errors
    if S <= 0:
        raise ValueError("Underlying asset price (S) must be greater than zero.")
    if K <= 0:
        raise ValueError("Strike price (K) must be greater than zero.")
    if T <= 0:
        raise ValueError("Time to expiration (T) must be greater than zero.")
    if sigma < 0:
        raise ValueError("Volatility (sigma) must be non-negative.")
    if num_simulations <= 0:
        raise ValueError("Number of simulations must be a positive integer.")
    if option_type not in ["Call", "Put"]:
        raise ValueError("Invalid option type. Use 'Call' or 'Put'.")

    # simulating price paths
    dt = T / 365  # daily time steps
    prices = np.zeros(num_simulations) #to store final stock price at expiry for each simulated world

    # generate or use given random numbers
    if random_numbers is None:
        #acc to the geometric brownian motion stochastic DE, the second term is to include randomness
        random_numbers = np.random.normal(size=(num_simulations, 365))  
    
    # check for random_numbers to have correct shape
    if random_numbers.shape != (num_simulations, 365):
        raise ValueError(f"random_numbers must have shape ({num_simulations}, 365)")

    for i in range(num_simulations):
        #for each of the simulations
        #cumsum - cumulative sum of daily log returns (multiplication of the return percentages) of 365 days in the ith simulation world
        price_path = S * np.exp(np.cumsum(
            (r - q - 0.5 * sigma ** 2) * dt +   #this is the predicted movement -
            sigma * np.sqrt(dt) * random_numbers[i] #randomness                 - this part is a vector of length 365 thats how the cumsum happens
        ))
        prices[i] = price_path[-1]  # last element since it has the final cumulated value

    # calculating option payoffs
    if option_type == "Call":
        payoffs = np.maximum(prices - K, 0)
    else:  # put payoffs
        payoffs = np.maximum(K - prices, 0)

    # the exponential term exists in order to correct the fact that future value is higher than present value 
    # we're calculating the present fair option price by discounting (convertin future money value to present) 
    # and averaging out the payoffs from all different simulations 
    option_price = np.exp(-r * T) * np.mean(payoffs)
    
    return option_price

def calculate_monte_carlo():
    
    # Create an instance of UserInput to gather parameters
    user_input = UserInput()
    user_input.gather_input(prefix="monte_carlo_")
    parameters = user_input.get_parameters()

    # Extract parameters
    underlying_price = parameters['underlying_price']
    strike_price = parameters['strike_price']
    time_to_expiration = parameters['time_to_expiration']  # Already in years
    risk_free_rate = parameters['risk_free_rate']  # As a decimal
    volatility = parameters['volatility']  # As a decimal
    dividend_yield = parameters['dividend_yield']  # As a decimal
    option_type = parameters['option_type']
    num_simulations = parameters['num_simulations']  # Accessing num_simulations from user input

    # Perform Monte Carlo simulation
    option_price = monte_carlo_simulation(option_type, underlying_price, strike_price, time_to_expiration, risk_free_rate, volatility, dividend_yield, num_simulations)
    return option_price 
