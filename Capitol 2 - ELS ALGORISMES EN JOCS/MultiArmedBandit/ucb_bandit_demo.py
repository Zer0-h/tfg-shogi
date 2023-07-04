import math
import numpy as np
import matplotlib.pyplot as plt
from multi_armed_bandit import BanditProblem

# These are the means of the action values that are used to simulate the multi-armed bandit problem
actionValues = np.array([1, 4, 2, 0, 7, 1, -1, 3])

# Confidence values to investigate the performance of the method
c_values = [0.5, 1, math.sqrt(2), 5, 10]

# Total number of simulation steps
totalSteps = 100000

# Create different bandit problems and simulate the method performance
mean_rewards = []
for c in c_values:
    confidence = c / 10
    bandit = BanditProblem(actionValues, confidence, totalSteps, c, True)
    bandit.playGame()
    mean_rewards.append(bandit.meanReward)

# Plot the results
plt.figure()
labels = ['confidence = 0.5', 'confidence = 1', 'confidence = √2', 'confidence = 5', 'confidence = 10']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for i in range(len(c_values)):
    plt.plot(np.arange(totalSteps + 1), mean_rewards[i], linewidth=2, color=colors[i], label=labels[i])

plt.xscale("log")
plt.xlabel('Steps')
plt.ylabel('Average Reward')
plt.legend()
plt.savefig('ucb_results.png', dpi=300)
plt.show()
