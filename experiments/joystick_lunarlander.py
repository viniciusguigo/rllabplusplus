#!/usr/bin/env python
""" joystick_lunarlander.py:
Uses joystick to control LunarLanderContinuous-v2.
"""

__author__ = "Vinicius Guimaraes Goecks"
__version__ = "0.0.0"
__date__ = "November 25, 2018"

import numpy as np
import gym
import time
import pygame

class JoystickAgent(object):
    """ Reads an Xbox joystick to control OpenAI Gym envs.

    Nov 25, 2018: 2 continuous actions using left and right stick.
    """
    def __init__(self, env):
        # env information
        self.env = env

        # setup xbox joystick using pygame
        pygame.init()

        # Initialize the connected joysticks
        pygame.joystick.init()
        joystick_count = pygame.joystick.get_count()
        print('Joysticks connected: {}'.format(joystick_count))

        # only use first connected
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        print('Using joystick: {}'.format(self.joystick.get_name()))

       

    def act(self, ob):
        """ Reads and return left and right sticks."""
        pygame.event.pump()
        # read left stick (vertical)
        left_stick_vert = self.joystick.get_axis(1)

        # read right stick (horizontal)
        right_stick_horz = self.joystick.get_axis(3)

        # concatenate joystick values
        action = np.array([-left_stick_vert, right_stick_horz])

        return action

    def close(self):
        """ Stop any thread (if any) or save additional data (if any)"""
        pygame.quit()
        print('Joystick connection closed.')

if __name__ == "__main__":
    try:
        ## setup human subject
        n_epi = 50
        exp_name = 'test'
        # save rewards and time steps
        human_data = np.zeros((n_epi, 2))

        # setup env and agent
        env = gym.make('LunarLanderContinuous-v2')
        agent = JoystickAgent(env)
        epi_counter = -1

        for _ in range(n_epi):
            epi_counter += 1
            total_reward = 0
            observation = env.reset()
            for t in range(1000):
                env.render()
                action = agent.act(observation)
                observation, reward, done, info = env.step(action)
                total_reward += reward
                if done:
                    print("Episode {}: {:.2f} reward, {} timesteps".format(epi_counter, total_reward, t+1))
                    human_data[0] = total_reward
                    human_data[1] = t+1
                    break
                
                # enforce loop speed (30 Hz)
                time.sleep(1/30)

        # save log to file
        file_addr = './data/human/{}_log.csv'.format(exp_name)
        np.savetxt(file_addr, human_data, delimiter=',')
        print('[*] * Human Performance Summary *')
        print('[*] Best reward: {} | Mean reward: {:.2f} | Std dev: {:.2f}'.format(np.max(human_data[:,0]), np.mean(human_data[:,0]),np.std(human_data[:,0])))
        print('[*] Log saved at {}'.format(file_addr))
                
    except KeyboardInterrupt:
        env.close()
        agent.close()
