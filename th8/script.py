import numpy as np
import matplotlib.pyplot as plt

def geometric_brownian_motion(num_steps, dt, mu, sigma, initial_value):
    time_points = np.arange(0, num_steps * dt, dt)
    increments = np.random.normal(mu * dt, sigma * np.sqrt(dt), size=num_steps)
    path = initial_value * np.exp(np.cumsum(increments))
    return time_points, path

# Parameters for the geometric Brownian motion
num_steps = 1000
dt = 0.01
mu = 0.1
sigma = 0.2
initial_value = 1.0

# Simulate the geometric Brownian motion
time_points, path = geometric_brownian_motion(num_steps, dt, mu, sigma, initial_value)

# Plot the trajectory of the geometric Brownian motion
plt.plot(time_points, path, label='Geometric Brownian Motion')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Simulation of Geometric Brownian Motion')
plt.legend()

# Save the plot as an image
plt.savefig('stochastic_processes_plot.png')

# Show the plot (optional, comment out if not needed)
plt.show()
