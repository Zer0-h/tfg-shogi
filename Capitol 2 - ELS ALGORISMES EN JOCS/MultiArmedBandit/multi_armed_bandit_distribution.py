import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

fig, axes = plt.subplots(2, 4, figsize=(14, 8))
fig.subplots_adjust(hspace=0.4, wspace=0.3)

action_values = np.array([1, 4, 2, 0, 7, 1, -1, 3])
variance = 2
sigma = math.sqrt(variance)

for idx, val in enumerate(action_values):
    mu = val
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)

    ax = axes[idx // 4, idx % 4]

    ax.plot(x, stats.norm.pdf(x, mu, sigma))
    ax.fill_between(x, stats.norm.pdf(x, mu, sigma), alpha=0.3)

    ax.set_xlabel('Màquina ' + str(idx + 1))

# Save the plot
plt.savefig('figuramaquines.png', dpi=1200)

# Show the plot
plt.show()
