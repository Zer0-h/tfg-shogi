import math
import numpy as np
import matplotlib.pyplot as plt
from multi_armed_bandit import MultiArmedBandit

# Means of the action values used to simulate the multi-armed bandit problem
action_values = np.array([1, 4, 2, 0, 7, 1, -1, 3])

# Confidence values to investigate the performance of the method
c1 = 0.5
c2 = 1
c3 = math.sqrt(2)
c4 = 5
c5 = 10

# Total number of simulation steps
total_steps = 100000

# Create different bandit problems and simulate the method performance
bandit1 = MultiArmedBandit(action_values, c1 / 10, total_steps, c1, True)
bandit1.playGame()
epsilon1_mean_reward = bandit1.meanReward

bandit2 = MultiArmedBandit(action_values, c2 / 10, total_steps, c2, True)
bandit2.playGame()
epsilon2_mean_reward = bandit2.meanReward

bandit3 = MultiArmedBandit(action_values, c3 / 10, total_steps, c3, True)
bandit3.playGame()
epsilon3_mean_reward = bandit3.meanReward

bandit4 = MultiArmedBandit(action_values, c4 / 10, total_steps, c4, True)
bandit4.playGame()
epsilon4_mean_reward = bandit4.meanReward

bandit5 = MultiArmedBandit(action_values, c5 / 10, total_steps, c5, True)
bandit5.playGame()
epsilon5_mean_reward = bandit5.meanReward

# Plot the results
plt.plot(np.arange(total_steps + 1), epsilon1_mean_reward, linewidth=2, color='#1f77b4', label='confiança = 0.5')
plt.plot(np.arange(total_steps + 1), epsilon2_mean_reward, linewidth=2, color='#ff7f0e', label='confiança = 1')
plt.plot(np.arange(total_steps + 1), epsilon3_mean_reward, linewidth=2, color='#2ca02c', label='confiança = √2')
plt.plot(np.arange(total_steps + 1), epsilon4_mean_reward, linewidth=2, color='#d62728', label='confiança = 5')
plt.plot(np.arange(total_steps + 1), epsilon5_mean_reward, linewidth=2, color='#9467bd', label='confiança = 10')
plt.xscale("log")
plt.xlabel('Passos')
plt.ylabel('Recompensa mitjana')
plt.legend()
plt.savefig('resultats_ucb.png', dpi=300)
plt.show()
