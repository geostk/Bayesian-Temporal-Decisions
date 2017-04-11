import numpy as np
import itertools
import random
from filtrieren import TransitionModel, ObservationModel

terrains = ['N']*40 + ['H']*20 + ['T']*20 + ['B']*10
random.shuffle(terrains)
GrossesGelaende = np.reshape(np.asmatrix(terrains), (9, 10))

def startingplace():
	indX = random.randrange(0,9)
	indY = random.randrange(0,9)

	if GrossesGelaende[indX,indY] == 'B':
		return startingplace()
	else:
		return (indX,indY)

def randomactions():
	actionseq = []
	possibleactions = ['U', 'D', 'L', 'R']

	for _ in itertools.repeat(None, 100):
		actionseq.append(possibleactions[random.randrange(0,3)])

	return actionseq

def PointsAndReadings(start, actionseq):
	points = [] 
	readings = []

	cellfrom = start
	for i in range(0, 100):
		latest = tuple(TransitionModel(cellfrom, actionseq[i]))
		print i
		points.append(latest)
		readings.append(ObservationModel(GrossesGelaende[latest]))
		cellfrom = latest

	return points,readings

def generatefile(index):
	sp = startingplace()
	actionseq = randomactions()
	points, readings = PointsAndReadings(sp, actionseq)
	
	target = open("output" + str(index) + ".txt", "w")

	target.write(str(GrossesGelaende) + "\n")
	target.write("x_0y_0: " + str(sp) + "\n")
	target.write("x_iy_i: " + str(points) + "\n")
	target.write("\\alpha_i: " + str(actionseq) + "\n")
	target.write("\\epsilon_i: " + str(readings))

	target.close()

def main():
	generatefile(0)

if __name__ == "__main__":
	main()
