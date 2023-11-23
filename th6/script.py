import numpy as np
import matplotlib.pyplot as plt

def inverse_transform_method(num_samples, lam):
    # Generate random samples from a uniform distribution
    u = np.random.uniform(size=num_samples)
    
    # Use the inverse transform method for exponential distribution
    x = -np.log(1 - u) / lam
    return x

# Parameters for the exponential distribution
lam = 2
num_samples = 1000

# Generate random variates using the inverse transform method
data = inverse_transform_method(num_samples, lam)

# Plot the histogram of generated random variates
plt.hist(data, bins=30, density=True, alpha=0.6, color='orange', label='Generated Variates')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Random Variates Generation using Inverse Transform Method')
plt.legend()

# Save the plot as an image
plt.savefig('random_variates_generation_plot.png')

# Show the plot (optional, comment out if not needed)
plt.show()
