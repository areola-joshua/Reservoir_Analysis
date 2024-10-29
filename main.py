import numpy as np
import matplotlib.pyplot as plt
from reservoir_calculations import (
    exponential_decline, hyperbolic_decline, harmonic_decline,
    cumulative_exponential, cumulative_hyperbolic, estimated_ultimate_recovery,
    water_cut_analysis
)

# Simulation Parameters
qi = 1000   # Initial production rate in barrels per day (bbl/day)
D = 0.2     # Decline rate
b = 0.5     # Decline exponent (for hyperbolic decline)
time = np.linspace(0, 10, 100)  # Time in years

"""
# Calculate Decline Rates
exp_decline = exponential_decline(qi, D, time)
hyp_decline = hyperbolic_decline(qi, D, b, time)
harm_decline = harmonic_decline(qi, D, time)

# Calculate Cumulative Production
cumulative_exp = cumulative_exponential(qi, D, time)
cumulative_hyp = cumulative_hyperbolic(qi, D, b, time)


# Calculate Estimated Ultimate Recovery (EUR)
EUR_exp = estimated_ultimate_recovery(qi, exp_decline[-1], D)
EUR_hyp = estimated_ultimate_recovery(qi, hyp_decline[-1], D)


# Generate Water Cut Data
oil_rate = exp_decline
water_rate = np.linspace(50, 300, len(time))  # Increasing water rate over time
water_cut = water_cut_analysis(oil_rate, water_rate)

# Plot Production Decline Curves
plt.figure(figsize=(10, 8))
plt.plot(time, exp_decline, label="Exponential Decline", color="blue")
plt.plot(time, hyp_decline, label="Hyperbolic Decline", color="green")
plt.plot(time, harm_decline, label="Harmonic Decline", color="red")
plt.xlabel("Time (years)")
plt.ylabel("Production Rate (bbl/day)")
plt.title("Production Decline Curves")
plt.legend()
plt.grid(True)
plt.show()

# Plot Cumulative Production
plt.figure(figsize=(10, 8))
plt.plot(time, cumulative_exp, label="Cumulative Production (Exponential)", color="blue")
plt.plot(time, cumulative_hyp, label="Cumulative Production (Hyperbolic)", color="green")
plt.xlabel("Time (years)")
plt.ylabel("Cumulative Production (bbl)")
plt.title("Cumulative Production Over Time")
plt.legend()
plt.grid(True)
plt.show()

# Plot Water Cut Analysis
plt.figure(figsize=(10, 8))
plt.plot(time, water_cut, label="Water Cut", color="purple")
plt.xlabel("Time (years)")
plt.ylabel("Water Cut (%)")
plt.title("Water Cut Analysis Over Time")
plt.legend()
plt.grid(True)
plt.show()

# Print EUR Results
print(f"Estimated Ultimate Recovery (Exponential): {EUR_exp:.2f} bbl")
print(f"Estimated Ultimate Recovery (Hyperbolic): {EUR_hyp:.2f} bbl") 
"""

#Assignment: debug this code snippets and make it work okay