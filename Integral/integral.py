import numpy as np
from scipy.integrate import quad

# Define the function to integrate
def integrand(x):
    return np.exp(-x**2 / 6)

# Set the limits of integration
lower_limit = 0
upper_limit = (3/2) + np.log(3)

# Perform the integration
result, error = quad(integrand, lower_limit, upper_limit)

print("Integral result:", result)
