import numpy as np
import random
from filtrieren import TransitionModel, ObservationModel

#TODO: import TM and OM from filtrieren.py

maps = ['N']*40 + ['H']*20 + ['T']*20 + ['B']*10
random.shuffle(maps)

def startingplace():
	index = random.randrange(0, 99)
	if maps[index] == 'B':
		return startingplace()
	else:
		return maps[index]

print startingplace()
