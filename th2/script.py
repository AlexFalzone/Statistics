import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def simulate_clt(sample_size, num_samples):
    means = []

    for _ in range(num_samples):
        sample = np.random.uniform(0, 1, sample_size)
        sample_mean = np.mean(sample)
        means.append(sample_mean)

    return means

def plot_clt_simulation(sample_size, num_samples):
    sample_means = simulate_clt(sample_size, num_samples)

    plt.hist(sample_means, bins=30, density=True, alpha=0.6, color='g', label='Sample Means')
    
    # Fit a normal distribution to the data
    mu, std = norm.fit(sample_means)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2, label='Fitted Normal Distribution')

    plt.xlabel('Sample Mean')
    plt.ylabel('Density')
    plt.title('Central Limit Theorem Simulation')
    plt.legend()
    plt.show()

# Example usage
sample_size = 30
num_samples = 1000
plot_clt_simulation(sample_size, num_samples)

plt.savefig('clt_simulation_plot.png')
