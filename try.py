import numpy as np
import matplotlib.pyplot as plt
import os

class bandit:
	def __init__(self):
		self.k_arm = 10
		self.stepn = 10000
		self.epison = 0.1
		self.alpha = 0.1
		self.deviate = 0.01
		self.mean = 0


	def reset(self):
		self.estimate = np.zeros(10)
		self.n = 0





	def state(self):
		r = np.random.randn()
		self.n +=1
		return r



	def act(self):
		
		if np.random.rand() < self.epison:
			action = np.random.randint(0,9)
			return action

		value = []
		for i,j in zip(self.estimate, [0,1,2,3,4,5,6,7,8,9]):
			value.append((i,j))
		np.random.shuffle(value)
		value.sort(key=lambda x: x[0],reverse= True)
		action = value[0][1]
		return action


def estimate(karm,r):
		n=karm.n
		karm.estimate[action] += (r-karm.estimate[action])*0.1

if __name__ == '__main__':
	karm = bandit()
	karm.reset()
	rewards = np.zeros(10000)
	for a in range(1000):
		r = karm.state()
		action = karm.act()
		estimate(karm,r)
		os.system('pause')
		plt.figure()
		plt.plot(karm.estimate)
		plt.show()
	








