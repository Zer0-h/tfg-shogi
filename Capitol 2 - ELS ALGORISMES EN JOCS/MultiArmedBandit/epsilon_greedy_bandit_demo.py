import numpy as np
import matplotlib.pyplot as plt
from multi_armed_bandit import MultiArmedBandit

# Mean action values used to simulate the multi-armed bandit problem
action_values = np.array([1, 4, 2, 0, 7, 1, -1, 3])

# Epsilon values to investigate the performance of the method
epsilon1 = 0
epsilon2 = 0.1
epsilon3 = 0.2
epsilon4 = 0.5
epsilon5 = 1

# Total number of simulation steps
total_steps = 100000

# Create different bandit problems and simulate the method performance
bandit1 = MultiArmedBandit(action_values, epsilon1, total_steps, 0, False)
bandit1.play_game()
epsilon1_mean_reward = bandit1.mean_rewards

bandit2 = MultiArmedBandit(action_values, epsilon2, total_steps, 0, False)
bandit2.play_game()
epsilon2_mean_reward = bandit2.mean_rewards

bandit3 = MultiArmedBandit(action_values, epsilon3, total_steps, 0, False)
bandit3.play_game()
epsilon3_mean_reward = bandit3.mean_rewards

bandit4 = MultiArmedBandit(action_values, epsilon4, total_steps, 0, False)
bandit4.play_game()
epsilon4_mean_reward = bandit4.mean_rewards

bandit5 = MultiArmedBandit(action_values, epsilon5, total_steps, 0, False)
bandit5.play_game()
epsilon5_mean_reward = bandit5.mean_rewards

# Plot the results
plt.plot(np.arange(total_steps + 1), epsilon1_mean_reward, linewidth=2, color='#1f77b4', label='Epsilon = 0')
plt.plot(np.arange(total_steps + 1), epsilon2_mean_reward, linewidth=2, color='#ff7f0e', label='Epsilon = 0.1')
plt.plot(np.arange(total_steps + 1), epsilon3_mean_reward, linewidth=2, color='#2ca02c', label='Epsilon = 0.2')
plt.plot(np.arange(total_steps + 1), epsilon4_mean_reward, linewidth=2, color='#d62728', label='Epsilon = 0.5')
plt.plot(np.arange(total_steps + 1), epsilon5_mean_reward, linewidth=2, color='#9467bd', label='Epsilon = 1.0')
plt.xscale("log")
plt.xlabel('Steps')
plt.ylabel('Average Reward')
plt.legend()
plt.savefig('epsilon_results.png', dpi=300)
plt.show()
