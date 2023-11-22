import numpy as np
import matplotlib.pyplot as plt

def glivenko_cantelli_simulation(sample_size, num_samples):
    cumulative_distribution_functions = []

    for _ in range(num_samples):
        # Generate random samples from a uniform distribution
        samples = np.sort(np.random.uniform(0, 1, sample_size))
        
        # Calculate the empirical cumulative distribution function (ECDF)
        ecdf = np.arange(1, sample_size + 1) / sample_size
        cumulative_distribution_functions.append(ecdf)

    return cumulative_distribution_functions

def plot_glivenko_cantelli_simulation(sample_size, num_samples):
    cumulative_distribution_functions = glivenko_cantelli_simulation(sample_size, num_samples)

    # Plot the Glivenko-Cantelli cumulative distribution functions
    for ecdf in cumulative_distribution_functions:
        plt.plot(np.linspace(0, 1, sample_size), ecdf, color='b', alpha=0.1)

    # Plot the true cumulative distribution function (uniform distribution)
    plt.plot(np.linspace(0, 1, sample_size), np.linspace(0, 1, sample_size), color='r', linestyle='--', label='True CDF (Uniform)')
    
    plt.xlabel('Value')
    plt.ylabel('Cumulative Probability')
    plt.title('Glivenko-Cantelli Theorem Simulation')
    plt.legend()
    plt.show()

# Example usage
sample_size = 100
num_samples = 1000
plot_glivenko_cantelli_simulation(sample_size, num_samples)

plt.savefig('img.png')