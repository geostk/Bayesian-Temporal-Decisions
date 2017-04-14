import numpy as np
import itertools
import random
from filtrieren import TransitionModel, ObservationModel
np.set_printoptions(threshold='nan')

def generatemap():
	terrains = ['N']*5000 + ['H']*2000 + ['T']*2000 + ['B']*1000
	random.shuffle(terrains)
	GrossesGelaende = np.reshape(np.asmatrix(terrains), (100, 100))
	return GrossesGelaende

def startingplace(mappo):
	indX = random.randrange(0,np.shape(mappo)[0])
	indY = random.randrange(0,np.shape(mappo)[1])

	if mappo[indX,indY] == 'B':
		return startingplace(mappo)
	else:
		return (indX,indY)

def randomactions(howmany):
	actionseq = []
	possibleactions = ['U', 'D', 'L', 'R']

	for _ in itertools.repeat(None, howmany):
		actionseq.append(possibleactions[random.randrange(0,4)])

	return actionseq

def PointsAndReadings(mappo, start, actionseq):
	points = [] 
	readings = []

	cellfrom = start
	for i in range(0, len(actionseq)):
		latest,throwaway = TransitionModel(mappo, cellfrom, actionseq[i])
		tlatest = tuple(latest)
		points.append(tlatest)
		readings.append(ObservationModel(mappo[tlatest]))
		cellfrom = tlatest

	return points,readings

def generatefiles(mappo, mapID, howmany):
	for i in range(0, howmany):
		sp = startingplace(mappo)
		actionseq = randomactions(100)
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
		generatefiles(generatemap(), i, 10)

if __name__ == "__main__":
	main()
