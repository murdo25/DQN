import sys
import gym
#import a3c


def main(argv):
	#chose a game, and num steps
	game = 'game name'
	steps = 1000
	agent = a3c()

	if(len(argv) > 1):
		env = gym.make(game)
		state = env.reset()
   		for i in xrange(int(argv[1])):
			for i in xrange(steps):
				action = agent.act(state)
        			observation, reward, done, info = env.step(action)
				#WHAT ON EARTH DO I DO WITH ALL THE OBSERVATIONS AND REWARDS IN a3c?
					
	else:
		print("ERROR, no input in argv[1]. Need num episodes")	
	pass

if __name__ == "__main__":
    main(sys.argv)
