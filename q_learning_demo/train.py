import math

import gym
from tqdm import tqdm
from terminaltables import AsciiTable

from .tabular_q_agent import TabularQAgent


def exponential_decay(starter_learning_rate, global_step, decay_step,
                      decay_rate, mini_value=0.0):
    decayed_learning_rate = starter_learning_rate * math.pow(decay_rate,
                                                             math.floor(
                                                                 global_step / decay_step))
    return decayed_learning_rate if decayed_learning_rate > mini_value else mini_value


def train(tabular_q_agent, env, train_episodes=100000):
    table_header = ['Episode', 'learning_rate', 'eps_rate', 'reward', 'step']

    table_data = [table_header]

    for episode in tqdm(range(train_episodes)):
        learning_rate = exponential_decay(0.9, episode, 1000, 0.99)
        eps_rate = exponential_decay(1.0, episode, 1000, 0.97, 0.001)

        all_reward, step_count = tabular_q_agent.learn(env, learning_rate,
                                                       eps_rate)

        if not episode % 1000:
            table_data.append([episode, learning_rate, eps_rate, all_reward, step_count])
            table = AsciiTable(table_data)
            tqdm.write(table.table)
            # print(DataFrame(tabular_q_agent.q))


def main():
    env = gym.make('FrozenLake-v0')
    env.seed(0)  # make sure result is reproducible

    tabular_q_agent = TabularQAgent(env.observation_space, env.action_space, n_iter=100, discount=1)

    train(tabular_q_agent, env)

    tabular_q_agent.test(env)
    tabular_q_agent.export()


if __name__ == "__main__":
    main()