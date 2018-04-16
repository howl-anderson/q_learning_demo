from collections import defaultdict
import functools
import pickle

import numpy as np

from gym.spaces import discrete


class UnsupportedSpace(Exception):
    pass


def generate_zeros(n):
    return [0] * n


class TabularQAgent(object):
    """
    Agent implementing tabular Q-learning.
    """

    def __init__(self, observation_space, action_space, **userconfig):
        if not isinstance(observation_space, discrete.Discrete):
            raise UnsupportedSpace('Observation space {} incompatible with {}. (Only supports Discrete observation spaces.)'.format(observation_space, self))
        if not isinstance(action_space, discrete.Discrete):
            raise UnsupportedSpace('Action space {} incompatible with {}. (Only supports Discrete action spaces.)'.format(action_space, self))
        self.observation_space = observation_space
        self.action_space = action_space
        self.action_n = action_space.n
        self.config = {
            "init_mean": 0.0,      # Initialize Q values with this mean
            "init_std": 0.0,       # Initialize Q values with this standard deviation
            "learning_rate": 0.5,
            "eps": 0.05,            # Epsilon in epsilon greedy policies
            "discount": 0.99,
            "n_iter": 10000}        # Number of iterations
        self.config.update(userconfig)
        # self.q = defaultdict(lambda: self.config["init_std"] * np.random.randn(self.action_n) + self.config["init_mean"])
        self.q = defaultdict(functools.partial(generate_zeros, n=self.action_n))

    def act(self, observation, eps=None):
        if eps is None:
            eps = self.config["eps"]
        # epsilon greedy.
        action = np.argmax(self.q[observation]) if np.random.random() > eps else self.action_space.sample()
        return action

    def learn(self, env, learning_rate=None, eps=None):
        if learning_rate is None:
            learning_rate = self.config["learning_rate"]

        obs = env.reset()
        # env.render(mode='human')

        rAll = 0
        step_count = 0

        for t in range(self.config["n_iter"]):
            action = self.act(obs, eps)
            obs2, reward, done, _ = env.step(action)
            # env.render(mode='human')

            # Get negative reward every step
            if reward == 0:
                reward = -0.005

            # if agent sucked at same position, punish it
            if obs == obs2:
                reward = -0.01

            # if agent fill to hole then die, punish it
            if done and not reward:
                reward = -1

            future = 0.0
            if not done:
                future = np.max(self.q[obs2])
            self.q[obs][action] = (1 - learning_rate) * self.q[obs][action] + learning_rate * (reward + self.config["discount"] * future)

            obs = obs2

            rAll += reward
            step_count += 1

            if done:
                break

        return rAll, step_count

    def test(self, env):
        obs = env.reset()
        env.render(mode='human')

        for t in range(self.config["n_iter"]):
            env.render(mode='human')

            action = self.act(obs, eps=0)
            obs2, reward, done, _ = env.step(action)
            env.render(mode='human')

            if done:
                break

            obs = obs2

    def export(self, file="./pretrained_model/parameter.pkl"):
        with open(file, 'wb') as fd:
            pickle.dump(self, fd)

    @staticmethod
    def load(file="./pretrained_model/parameter.pkl"):
        with open(file, 'rb') as fd:
            instance = pickle.load(fd)
        return instance
