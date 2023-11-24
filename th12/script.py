import numpy as np
import matplotlib.pyplot as plt

def simulate_ito_integral(num_steps, dt):
    # Generate increments from a normal distribution
    increments = np.random.normal(0, np.sqrt(dt), size=num_steps)
    
    # Calculate the cumulative sum to obtain the Itô integral
    ito_integral = np.cumsum(increments)
    
    # Create time points
    time_points = np.linspace(0, (num_steps - 1) * dt, num_steps)
    
    return time_points, ito_integral

# Parameters for the simulation
num_steps = 1000
dt = 0.01

# Simulate the Itô integral
ito_time_points, ito_integral = simulate_ito_integral(num_steps, dt)

# Plot the Itô integral
plt.plot(ito_time_points, ito_integral, label="Itô Integral")
plt.xlabel('Time')
plt.ylabel('Value')
plt.title("Simulation of Itô Integration")
plt.legend()

# Save the plot as an image
plt.savefig('ito_integration_plot.png')

