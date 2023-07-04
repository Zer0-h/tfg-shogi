import numpy as np
import matplotlib.pyplot as plt
from multi_armed_bandit import BanditProblem

# These are the means of the action values that are used to simulate the multi-armed bandit problem
actionValues = np.array([1, 4, 2, 0, 7, 1, -1, 3])

# Epsilon values to investigate the performance of the method
epsilon_values = [0, 0.1, 0.2, 0.5, 1]

# Total number of simulation steps
totalSteps = 100000

# Create different bandit problems and simulate the method performance
mean_rewards = []
for epsilon in epsilon_values:
    bandit = BanditProblem(actionValues, epsilon, totalSteps, 0, False)
    bandit.playGame()
    mean_rewards.append(bandit.meanReward)

# Plot the results
plt.figure()
labels = ['ε = 0', 'ε = 0.1', 'ε = 0.2', 'ε = 0.5', 'ε = 1.0']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for i in range(len(epsilon_values)):
    plt.plot(np.arange(totalSteps + 1), mean_rewards[i], linewidth=2, color=colors[i], label=labels[i])

plt.xscale("log")
plt.xlabel('Steps')
plt.ylabel('Average Reward')
plt.legend()
plt.savefig('epsilon_greedy_results.png', dpi=300)
plt.show()
