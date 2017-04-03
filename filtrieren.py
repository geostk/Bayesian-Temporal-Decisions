import numpy as np

terrain = np.matrix(
[['H', 'N', 'T'],
['N', 'N', 'N'],
['N', 'B', 'H']])

prior = np.matrix(
[[0.125, 0.125, 0.125],
[0.125, 0.125, 0.125], 
[0.125, 0.125, 0.125]])

actions = ['R', 'R', 'R', 'R']
readings = ['N', 'N', 'H', 'H']

def move(prevmap, action):
	for pos in np.nditer(prevmap):
		

	return none

for x in np.nditer(prior):
	print x
