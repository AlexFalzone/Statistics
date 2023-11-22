import numpy as np
import matplotlib.pyplot as plt

# Parameters for the Gaussian Distribution
mean = 0
std_dev = 1
num_samples = 1000

# Generate random samples from the Gaussian Distribution
data = np.random.normal(mean, std_dev, num_samples)

# Plot the Gaussian Distribution
plt.hist(data, bins=30, density=True, alpha=0.6, color='b', label='Gaussian Distribution')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Gaussian Distribution Plot')
plt.legend()

# Save the plot as an image
plt.savefig('gaussian_distribution_plot.png')

# Show the plot (optional, comment out if not needed)
plt.show()
