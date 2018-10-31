#!/usr/bin/env python
""" test_hri_airsim.py:
Tests AirSim environment following OpenAI template.
"""

__author__ = "Vinicius Guimaraes Goecks"
__version__ = "0.0.0"
__status__ = "Prototype"
__date__ = "March 3, 2018"


# import
import sys
sys.path.append('../')
import gym
import hri_airsim
import time
import numpy as np
import argparse

class RandomAgent(object):
    """ Performs random actions.
    Used to test environment action space.
    """
    def __init__(self, action_space):
        self.name = 'RandomAgent'
        print('\n*** AGENT: {} ***\n'.format(self.name))
        self.action_space = action_space

    def act(self, observation, reward, done):
        # take a random action
        return self.action_space.sample()

    def close(self):
        """ Stop any thread (if any) or save additional data (if any)"""
        pass

# set random seed.
np.random.seed(1234)

# pseudorandomized starting locations to make comparisons between different
# conditions/runs more fair and even since all runs will now use the same
# starting locations.
initial_y =[
3.851863845972779643e+00,
7.315313326359103030e-01,
-1.592320246707973119e+00,
-3.325366060609192154e+00,
-3.691736009695765652e+00,
3.096417643265097830e+00,
1.448944818145720959e-01,
-3.426283247314604985e+00,
-2.935075205028058853e+00,
-7.676791489005614366e-01,
9.434738875769195232e-01,
-1.399760914587099947e+00,
-1.047589761607853553e+00,
-2.401530045369543842e+00,
3.918044941240500734e+00,
3.356195150793229942e+00,
-1.312118710761853713e+00,
-8.713667529078970020e-01,
3.465162565469892542e-02,
-7.845481638100588739e-01]

initial_x = [
1.349015511269798129e+00,
-8.059045546729562970e-01,
2.456155729665019383e-01,
-4.005863604281448831e-01,
-1.073913348375217236e+00,
2.524124103539480135e-01,
-3.042971979491014833e-01,
2.824285713820617882e-02,
1.364903140506922741e+00,
-6.696202346962570884e-01,
6.975745159647920302e-01,
2.211874700905559488e-01,
-3.725979267282220064e-02,
2.612153184780535708e-01,
-5.273856207414873154e-01,
2.880338834221423117e-01,
-1.031310336137476469e+00,
5.718374171563622710e-02,
1.175336573511485128e-01,
-2.504171148884938303e-01]


def main(imitation_model, n_episodes, idx, human_log):
    ## ENVS
    # start env and test agent
    # env = gym.make('HRI_AirSim-v0')
    env = gym.make('HRI_AirSim_Landing-v0')
    if (idx != 0) and (human_log is not None):
        env._preload_csv(
            initial_human_addr='./data/' + human_log,
            initial_human_epi=idx)

    # if desired, can override number of episodes using argparse
    if n_episodes is not None:
        env.n_episodes = n_episodes

    ## AGENTS
    agent = RandomAgent(env.action_space)
    
    reward = 0
    done = False

    # test basic functions
    try:
        for i_episode in range(idx, env.n_episodes):
            print('*** EPISODE {}/{} ***'.format(i_episode+1, env.n_episodes))
            # feed episode number to agent
            if agent.name == 'InterventionAgent':
                agent.epi_number = i_episode

            x = None
            y = None
            if i_episode < len(initial_x):
                x = initial_x[i_episode]/10 # added /10 for testing only
                y = initial_y[i_episode]/10 # (vehicle starts close to center of road)
            obs = env.reset(initial_x = x, initial_y = y)
            total_rew = 0
            t = 0
            log_time = []
            start_time = time.time()
            while True:
                action = agent.act(obs, reward, done)
                obs, reward, done, info = env.step(action)
                total_rew += reward
                t += 1
                total_time = time.time() - start_time
                log_time.append(total_time)
                start_time = time.time()
                if done:
                    print("Episode finished after {} timesteps".format(t+1))
                    print("Total reward = %.2f" %total_rew)
                    print('Total episode time (sec): ', np.sum(log_time))
                    print('Average time per timestep (sec): ', np.sum(log_time)/(t+1))
                    break

        # close everything
        env.close()
        agent.close()

    except KeyboardInterrupt:
        print('*** KEYBOARD INTERRUPT ***')
        # closes everything after a ctrl+c
        env.close()
        agent.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=('Testing different agents for'
                                                  'the HRI_AirSim_Landing env.'))
    parser.add_argument('--imitation_model', type=str, help='Model to load',
                        default=None)
    parser.add_argument('--n_episodes', type=int, help='Number of episodes to run',
                        default=None)
    parser.add_argument('--idx', type=int, help='Starting idx for human log',
                        default=0)
    parser.add_argument('--human_log', type=str, help='Human log to load',
                        default=None)
    args = parser.parse_args()
    main(**vars(args))
