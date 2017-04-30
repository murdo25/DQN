import tensorflow as tf
import numpy as np
import gym
import random

#chose an environment

#env.render()


class DQN:
    def __init__(self,env):
        self.env = gym.make('SpaceInvaders-v0')
        self.state = self.env.reset()
        self.experience = []
        self.epsilon = .75
        #self.action_space = self.env.action_space
        
    def select_action(self):
        if (random.uniform(0.0,1.0) < self.epsilon):
            #take random action
            action = self.env.action_space.sample()
            statePrime,reward,terminal,_ = self.env.step(action)
            
            #add the observation s,a,r,s' to the experience memory
            self.experience.append(self.state, action, reward, statePrime, terminal)
            
            #Update
            self.state = statePrime
            self.epsilon -= 1/1000.0
            
        else:
            #chose the best action with respect to your Q funtion
            action = self.Qnetwork()         
            
            #add the observation s,a,r,s' to the experience memory
            statePrime,reward,terminal,_ = self.env.step(action)
            
            self.experience.append(self.state, action, reward, statePrime, terminal)
            
            
    def Qnetwork(self):
        #arg_max(a) (Q(st),a;theta)          
        #convnet leading to an action
    
    
    
        action = 0
        return action
            

    def updateQnetwork(state):
        pass








dqn = DQN()

#for each episode
for episode in range(10000):   
    #take a step bassed on your current Q function
    state = env.reset()
    for i in range(1000):
        action = dqn.select_action(state)
        state  = env.step(action)
        
        continue
    #update Q-values

