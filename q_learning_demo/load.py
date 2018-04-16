import gym

from .tabular_q_agent import TabularQAgent


def main():
    env = gym.make('FrozenLake-v0')

    tabular_q_agent = TabularQAgent.load()
    tabular_q_agent.test(env)


if __name__ == "__main__":
    main()
