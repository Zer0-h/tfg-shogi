import math
import numpy as np

class MultiArmedBandit:
    def __init__(self, true_action_values, epsilon, total_steps, confidence, is_ucb):
        self.arm_number = np.size(true_action_values)
        self.epsilon = epsilon
        self.confidence = confidence
        self.is_ucb = is_ucb
        self.current_step = 0
        self.times_selected_arm = np.zeros(self.arm_number)
        self.total_steps = total_steps
        self.true_action_values = true_action_values
        self.mean_rewards = np.zeros(total_steps + 1)
        self.ucb_values = np.zeros(self.arm_number)
        self.sum_rewards = np.zeros(self.arm_number)

    def select_action(self):
        if not self.is_ucb:
            probability_draw = np.random.rand()
            if (self.current_step == 0) or (probability_draw <= self.epsilon):
                selected_arm_index = np.random.choice(self.arm_number)
            else:
                selected_arm_index = np.argmax(self.mean_rewards)

        else:
            selected_arm_index = self.selected_ucb_arm()

        self.current_step += 1
        self.times_selected_arm[selected_arm_index] += 1
        self.current_reward = np.random.normal(self.true_action_values[selected_arm_index], 2)
        self.mean_rewards[self.current_step] = self.mean_rewards[self.current_step - 1] + (1 / self.current_step) * (self.current_reward - self.mean_rewards[self.current_step - 1])
        self.armMeanRewards[selected_arm_index] += (1 / self.times_selected_arm[selected_arm_index]) * (self.current_reward - self.armMeanRewards[selected_arm_index])
        self.sum_rewards[selected_arm_index] += self.current_reward

    def play_game(self):
        for _ in range(self.total_steps):
            self.select_action()

    def clear_all(self):
        self.current_step = 0
        self.times_selected_arm = np.zeros(self.arm_number)
        self.armMeanRewards = np.zeros(self.arm_number)
        self.current_reward = 0
        self.mean_rewards = np.zeros(self.total_steps + 1)

    def selected_ucb_arm(self):
        for arm in range(self.arm_number):
            if self.times_selected_arm[arm] == 0:
                return arm
            else:
                mean_reward = self.sum_rewards[arm] / self.times_selected_arm[arm]
                confidence_bound = self.confidence * math.sqrt(math.log2(self.current_step) / self.times_selected_arm[arm])
                self.ucb_values[arm] = mean_reward + confidence_bound

        return np.argmax(self.ucb_values)
