import numpy as np
import matplotlib.pyplot as plt

class OnlineMeanEstimator:
    def __init__(self):
        self.mean = 0
        self.num_samples = 0

    def update(self, new_value):
        self.num_samples += 1
        self.mean = self.mean + (new_value - self.mean) / self.num_samples

# Parameters for the data stream
num_data_points = 1000
stream = np.random.normal(0, 1, num_data_points)

# Initialize the online mean estimator
mean_estimator = OnlineMeanEstimator()

# Update the estimator with the data stream
for data_point in stream:
    mean_estimator.update(data_point)

# Plot the mean estimates over time
mean_estimates = [mean_estimator.mean for _ in range(num_data_points)]
plt.plot(range(num_data_points), mean_estimates, label='Online Mean Estimate')
plt.axhline(0, color='r', linestyle='--', label='True Mean')
plt.xlabel('Data Points')
plt.ylabel('Mean Estimate')
plt.title('Online Mean Estimation from Data Stream')
plt.legend()

# Save the plot as an image
plt.savefig('online_algorithm_plot.png')

# Show the plot (optional, comment out if not needed)
plt.show()
