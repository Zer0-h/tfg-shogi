import math
import numpy as np


class BanditProblem(object):
    def __init__(self, trueActionValues, epsilon, totalSteps, confidence, isUCB):

        # Number of arms
        self.armNumber = np.size(trueActionValues)

        # Probability of ignoring the greedy selection and selecting an arm randomly
        self.epsilon = epsilon

        self.confidence = confidence

        self.isUCB = isUCB

        # Current step
        self.currentStep = 0

        # This variable tracks how many times a particular arm is being selected
        self.timesSelected = np.zeros(self.armNumber)

        # Total steps
        self.totalSteps = totalSteps

        # True action values that are expectations of rewards for arms
        self.trueActionValues = trueActionValues

        # Vector that stores mean rewards of every arm
        self.armMeanRewards = np.zeros(self.armNumber)

        # Variable that stores the current value of reward
        self.currentReward = 0

        # Mean reward
        self.meanReward = np.zeros(totalSteps + 1)

        self.ucb_values = np.zeros(self.armNumber)

        self.sum_rewards = np.zeros(self.armNumber)

    def selectAction(self):
        if not self.isUCB:
            probabilityDraw = np.random.rand()

            if (self.currentStep == 0) or (probabilityDraw <= self.epsilon):
                selectedArmIndex = np.random.choice(self.armNumber)
            else:
                selectedArmIndex = np.argmax(self.armMeanRewards)

            self.currentStep += 1

            self.timesSelected[selectedArmIndex] += 1

            self.currentReward = np.random.normal(self.trueActionValues[selectedArmIndex], 2)

            self.meanReward[self.currentStep] = self.meanReward[self.currentStep - 1] + \
                (1 / self.currentStep) * (self.currentReward - self.meanReward[self.currentStep - 1])

            self.armMeanRewards[selectedArmIndex] += \
                (1 / self.timesSelected[selectedArmIndex]) * \
                (self.currentReward - self.armMeanRewards[selectedArmIndex])

        else:
            selectedArmIndex = self.selectedUCBArm()

            self.currentStep += 1

            self.timesSelected[selectedArmIndex] += 1

            self.currentReward = np.random.normal(self.trueActionValues[selectedArmIndex], 2)

            self.meanReward[self.currentStep] = self.meanReward[self.currentStep - 1] + \
                (1 / self.currentStep) * (self.currentReward - self.meanReward[self.currentStep - 1])

            self.armMeanRewards[selectedArmIndex] += \
                (1 / self.timesSelected[selectedArmIndex]) * \
                (self.currentReward - self.armMeanRewards[selectedArmIndex])

            self.sum_rewards[selectedArmIndex] += self.currentReward

    def playGame(self):
        for _ in range(self.totalSteps):
            self.selectAction()

    def clearAll(self):
        self.currentStep = 0
        self.timesSelected = np.zeros(self.armNumber)
        self.armMeanRewards = np.zeros(self.armNumber)
        self.currentReward = 0
        self.meanReward = np.zeros(self.totalSteps + 1)

    def selectedUCBArm(self):
        for arm in range(self.armNumber):
            if self.timesSelected[arm] == 0:
                return arm
            else:
                mean_reward = self.sum_rewards[arm] / self.timesSelected[arm]
                confidence_bound = self.confidence * math.sqrt(math.log2(self.currentStep) / self.timesSelected[arm])
                self.ucb_values[arm] = mean_reward + confidence_bound

        return np.argmax(self.ucb_values)
