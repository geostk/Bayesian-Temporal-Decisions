import numpy as np
import random

terrain = np.matrix(
[['H', 'N', 'T'],
['N', 'N', 'N'],
['N', 'B', 'H']])

prior = np.matrix(
[[0.125, 0.125, 0.125],
[0.125, 0.125, 0.125], 
[0.125, 0, 0.125]]) #prior[2,1] == 'B'

actions = ['Right', 'Right', 'Down', 'Down']
readings = ['N', 'N', 'H', 'H']

def TransitionModel(cellfromimmutable, action):
	cellfrom = list(cellfromimmutable)
	cellto = cellfrom #cellto changes when cellfrom changes. bc python
	if action == 'Right' or action == 'R':
		cellto[0] += 1
	elif action == 'Left' or action == 'L':
		cellto[0] -= 1
	elif action == 'Up' or action == 'U':
		cellto[1] += 1
	elif action == 'Down' or action == 'D':
		cellto[1] -= 1
	else:
		return nil

	if cellto[0] <= -1 or cellto[0] >= 3:
		return list(cellfromimmutable)
	elif cellto[1] <= -1 or cellto[1] >= 3:
		return list(cellfromimmutable)
	elif cellto[0] == 1 and cellto[1] == 2:
		return list(cellfromimmutable)
	
	if random.randrange(0, 100) < 90:
		return cellto
	else:
		return list(cellfromimmutable) 

def ObservationModel(reading):
	prob = random.randrange(0, 100)
	if prob < 90:
		return reading
	elif prob >= 90 and prob < 95:
		if reading == 'N':
			return 'H'
		elif reading == 'H':
			return 'T'
		elif reading == 'T':
			return 'N'
	elif prob >= 95 and prob < 100:
		if reading == 'N':
			return 'T'
		elif reading == 'H':
			return 'N'
		elif reading == 'T':
			return 'H'			
	
#for x in np.nditer(prior):
#	print x

def main():
	print TransitionModel((2,0), 'Right') #cannot do so, other is blocked
	print ObservationModel(terrain[2,0])
