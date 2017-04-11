import numpy as np
import itertools
import random
from filtrieren import TransitionModel, ObservationModel

def generatemap():
	terrains = ['N']*40 + ['H']*20 + ['T']*20 + ['B']*10
	random.shuffle(terrains)
	GrossesGelaende = np.reshape(np.asmatrix(terrains), (9, 10))
	return GrossesGelaende

def startingplace(mappo):
	indX = random.randrange(0,9)
	indY = random.randrange(0,9)

	if mappo[indX,indY] == 'B':
		return startingplace(mappo)
	else:
		return (indX,indY)

def randomactions():
	actionseq = []
	possibleactions = ['U', 'D', 'L', 'R']

	for _ in itertools.repeat(None, 100):
		actionseq.append(possibleactions[random.randrange(0,3)])

	return actionseq

def PointsAndReadings(mappo, start, actionseq):
	points = [] 
	readings = []

	cellfrom = start
	for i in range(0, 100):
		latest = tuple(TransitionModel(mappo, cellfrom, actionseq[i]))
		points.append(latest)
		readings.append(ObservationModel(mappo[latest]))
		cellfrom = latest

	return points,readings

def generatefiles(mappo, mapID):
	for i in range(0, 10):
		sp = startingplace(mappo)
		actionseq = randomactions()
		points, readings = PointsAndReadings(mappo, sp, actionseq)
	
		target = open("output" + str(mapID) + "-" + str(i) + ".txt", "w")
		target.write("mapID: " + str(mapID) + "; path " + str(i) + "\n" + str(mappo) + "\n")
		target.write("x_0y_0: " + str(sp) + "\n")
		target.write("x_iy_i: " + str(points) + "\n")
		target.write("\\alpha_i: " + str(actionseq) + "\n")
		target.write("\\epsilon_i: " + str(readings))

		target.close()

def main():
	for i in range(0, 10):
		generatefiles(generatemap(), i)

if __name__ == "__main__":
	main()
