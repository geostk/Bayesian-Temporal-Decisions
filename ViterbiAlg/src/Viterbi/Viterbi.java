package Viterbi;

import Viterbi.Path;

public class Viterbi{

	public static int[] viterbiAlg(int[] obs, double[] probsInit, Path[] map){
		double[][] V = new double[obs.length][map.length];
		int path[][] = new int[map.length][obs.length];

		for (int i = 0; i < map.length; i++){
			V[0][i] = probsInit[0] * map[i].emissionProbList[obs[0]];
			System.out.println("Diagnostic A: " + probsInit[0] * map[i].emissionProbList[obs[0]] + " in state " + i);
			path[i][0] = i;
		}
		for (int i = 1; i < obs.length; i++){
			int[][] newpath = new int[map.length][obs.length];
			boolean hasChanged = false;
			if(i > 1 && !hasChanged){
				for(int x = 0; x < map.length; x++){
					map[x].changeDir();
				}
				hasChanged = true;
			}
			for(int j = 0; j < map.length; j++){
				double prob = 0;
				int state;
				for(int k = 0; k < map.length; k++){
					double nprob = V[i - 1][k] * map[k].transProbList[j] * map[j].emissionProbList[obs[i]];
					if(nprob > prob){
						prob = nprob;
						state = k;
						V[i][j] = prob;
						System.arraycopy(path[state], 0, newpath[j], 0, i);
						newpath[j][i] = j;
						System.out.println("Diagnostic: " + prob + " in state " + state);
					}
				}
			}
			path = newpath;
		}

		double prob = 0;
		int state = 0;
		for(int i = 0; i < map.length; i++){
			System.out.println("Diagnostic 2: " + V[obs.length - 1][i] + " in state " + i);
			if(V[obs.length - 1][i] > prob){
				prob = V[obs.length - 1][i];
				state = i;
			}
		}
		return path[state];
	}

}