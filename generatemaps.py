import numpy as np
import random
from filtrieren import TransitionModel, ObservationModel

terrains = ['N']*40 + ['H']*20 + ['T']*20 + ['B']*10
random.shuffle(terrains)
GrossesGelaende = np.asmatrix(terrains)
GrossesGelaende = np.reshape(GrossesGelaende, (9, 10))

def startingplace():
	indX = random.randrange(0,9)
	indY = random.randrange(0,9)

	if GrossesGelaende[indX,indY] == 'B':
		return startingplace()
	else:
		return [indX,indY]

def generatefile():
	firstline = "x0y0: " + str(startingplace()) + "\n"

	target = open("output.txt", "w")
	target.write(firstline)
	target.close()

def main():
	print GrossesGelaende
	generatefile()

if __name__ == "__main__":
	main()
