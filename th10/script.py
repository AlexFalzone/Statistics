import numpy as np
import matplotlib.pyplot as plt

def simulate_wiener_process(num_steps, dt):
    # Generate increments from a normal distribution
    increments = np.random.normal(0, np.sqrt(dt), size=num_steps)
    
    # Cumulatively sum the increments to get the Wiener process path
    wiener_process = np.cumsum(increments)
    
    # Create time points
    time_points = np.linspace(0, (num_steps - 1) * dt, num_steps)
    
    return time_points, wiener_process

def simulate_gbm(num_steps, dt, mu, sigma, initial_value):
    # Simulate the Wiener process
    time_points, wiener_process = simulate_wiener_process(num_steps, dt)
    
    # Calculate the GBM path
    gbm_path = initial_value * np.exp((mu - 0.5 * sigma**2) * time_points + sigma * wiener_process)
    
    return time_points, gbm_path

# Parameters for the simulation
num_steps = 1000
dt = 0.01
mu = 0.1
sigma = 0.2
initial_value = 1.0

# Simulate the Wiener process
wiener_time_points, wiener_process = simulate_wiener_process(num_steps, dt)

# Simulate the GBM
gbm_time_points, gbm_path = simulate_gbm(num_steps, dt, mu, sigma, initial_value)

# Plot the Wiener process and GBM
plt.plot(wiener_time_points, wiener_process, label='Wiener Process')
plt.plot(gbm_time_points, gbm_path, label='Geometric Brownian Motion (GBM)')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Simulation of Wiener Process and GBM')
plt.legend()

# Save the plot as an image
plt.savefig('wiener_gbm_simulation_plot.png')

# Show the plot (optional, comment out if not needed)
plt.show()
