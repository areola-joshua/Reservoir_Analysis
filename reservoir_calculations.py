import numpy as np

# Decline Curve Analysis (DCA) Functions
def exponential_decline(qi, D, t):
    """ Simulation Parameters
    Args:
        qi (float): # Initial production rate in barrels per day (bbl/day)
        D (float): # Decline rate
        t (float): # Decline exponent (for hyperbolic decline)

    Returns:
        [type]: [description]
    """     
    return qi * np.exp(-D * t)

def hyperbolic_decline(qi, D, b, t):
    """AI is creating summary for hyperbolic_decline

    Args:
        qi ([type]): [description]
        D ([type]): [description]
        b ([type]): [description]
        t ([type]): [description]

    Returns:
        [type]: [description]
    """
    return qi / ((1 + b * D * t) ** (1 / b))

def harmonic_decline(qi, D, t):
    return qi / (1 + D * t)

# Cumulative Production Calculations
def cumulative_exponential(qi, D, t):
    return (qi / D) * (1 - np.exp(-D * t))

def cumulative_hyperbolic(qi, D, b, t):
    return (qi / (D * (1 - b))) * (1 - (1 + b * D * t) ** ((1 - b) / b))

# Estimated Ultimate Recovery (EUR)
#def estimated_ultimate_recovery(qi, q_t, D, t):
 #   return cumulative_exponential(qi, D, t) + (q_t / D)

# Water Cut Analysis
def water_cut_analysis(oil_rate, water_rate):
    return water_rate / (oil_rate + water_rate)