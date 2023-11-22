import random
import matplotlib.pyplot as plt

def simulate_coin_tosses(num_tosses):
    results = [random.choice(['Heads', 'Tails']) for _ in range(num_tosses)]
    head_count = results.count('Heads')
    tail_count = num_tosses - head_count
    return head_count / num_tosses

def plot_lln_simulation(num_simulations, max_tosses):
    averages = []

    for tosses in range(1, max_tosses + 1):
        simulation_results = [simulate_coin_tosses(tosses) for _ in range(num_simulations)]
        average = sum(simulation_results) / num_simulations
        averages.append(average)

    plt.plot(range(1, max_tosses + 1), averages, label='Simulation Mean')
    plt.axhline(0.5, color='r', linestyle='--', label='Expected Value (0.5)')
    plt.xlabel('Number of Tosses')
    plt.ylabel('Mean of Heads')
    plt.legend()
    plt.show()

num_simulations = 1000
max_tosses = 1000
plot_lln_simulation(num_simulations, max_tosses)

plt.savefig('lln_simulation_plot.png')
