import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, poisson

def simulate_continuous_distribution():
    # Simulate a continuous distribution (normal distribution)
    data = np.random.normal(0, 1, 1000)

    # Plot the histogram
    plt.hist(data, bins=30, density=True, alpha=0.6, color='b', label='Continuous Distribution (Normal)')

def simulate_discrete_distribution():
    # Simulate a discrete distribution (Poisson distribution)
    data = np.random.poisson(3, 1000)

    # Plot the histogram
    plt.hist(data, bins=np.arange(0, max(data) + 1.5) - 0.5, density=True, alpha=0.6, color='g', label='Discrete Distribution (Poisson)')

def plot_properties():
    # Plot distribution properties (mean, variance, skewness)
    x = np.linspace(-5, 5, 100)
    plt.plot(x, norm.pdf(x, 0, 1), 'r', label='Normal Distribution (N(0,1))')
    plt.title('Distribution Properties')
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.legend()

# Example usage
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
simulate_continuous_distribution()
plt.title('Continuous Distribution Simulation')

plt.subplot(2, 2, 2)
simulate_discrete_distribution()
plt.title('Discrete Distribution Simulation')

plt.subplot(2, 2, 3)
plot_properties()

plt.tight_layout()
plt.show()

plt.savefig('img.png')
