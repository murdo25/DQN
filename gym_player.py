import gym
import numpy as np


#env = gym.make('Asteroids-ramDeterministic-v0')
#env = gym.make('Asteroids-ramDeterministic-v3')
#env = gym.make('Robotank-v3')
env = gym.make('LunarLander-v2')

env.reset()
env.render()

for i_episode in range(100):
    observation = env.reset()
    
    for j in range(10000):
        env.render()
        print(observation)
        action = env.action_space.sample()
        #action = 2
        observation, reward, done, info = env.step(action)
        
        if done:
            print("episode finished after {} timesteps".format(j+1))
            break
    
    
    
    env.step(env.action_space.sample())
    
    
    
