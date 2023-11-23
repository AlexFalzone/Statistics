import numpy as np
import matplotlib.pyplot as plt

def simulate_poisson_process(rate, time_horizon):
    # Generate random inter-arrival times from exponential distribution
    inter_arrival_times = np.random.exponential(1/rate, int(rate * time_horizon * 2))
    
    # Calculate arrival times
    arrival_times = np.cumsum(inter_arrival_times)
    
    # Extract events within the time horizon
    arrival_times = arrival_times[arrival_times <= time_horizon]
    
    return arrival_times

# Parameters for the Poisson Process
arrival_rate = 0.5
simulation_time = 10

# Simulate the Poisson Process
poisson_process_events = simulate_poisson_process(arrival_rate, simulation_time)

# Plot the Poisson Process events
plt.eventplot(poisson_process_events, lineoffsets=1, color='blue', label='Poisson Process Events')
plt.xlabel('Time')
plt.ylabel('Event')
plt.title('Simulation of Poisson Process')
plt.legend()

# Save the plot as an image
plt.savefig('poisson_process_plot.png')

# Show the plot (optional, comment out if not needed)
plt.show()
