import numpy as np
import matplotlib.pyplot as plt

def donsker_invariance_simulation(num_samples, num_points):
    # Generate random samples from a uniform distribution
    samples = np.random.uniform(size=(num_samples, num_points))
    
    # Calculate the empirical distribution function (ECDF) for each sample
    ecdfs = np.array([np.cumsum(sample) / num_points for sample in samples])
    
    # Plot the ECDFs
    for ecdf in ecdfs:
        plt.plot(np.linspace(0, 1, num_points), ecdf, color='gray', alpha=0.1)
    
    # Plot the average ECDF
    average_ecdf = np.mean(ecdfs, axis=0)
    plt.plot(np.linspace(0, 1, num_points), average_ecdf, color='blue', label='Average ECDF')
    
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.title("Donsker's Invariance Principle Simulation")
    plt.legend()

    # Save the plot as an image
    plt.savefig('donsker_invariance_plot.png')

    # Show the plot (optional, comment out if not needed)
    plt.show()

# Parameters for the simulation
num_samples = 1000
num_points = 100

# Simulate Donsker's Invariance Principle
donsker_invariance_simulation(num_samples, num_points)

plt.savefig('img.png')
