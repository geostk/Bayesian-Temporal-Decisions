package Viterbi;

import Viterbi.Path;
import Viterbi.Viterbi;

class Main{
	public static void main(String[] args){
		Path[] currPath = new Path[8];
		Viterbi v = new Viterbi();
		for(int i = 0; i < currPath.length; i++){
			currPath[i] = new Path(i);
		}
		int[] obs = new int[4];
		obs[0] = 0;
		obs[1] = 0;
		obs[2] = 1;
		obs[3] = 1;

		int[] finalPath = new int[4];
		double[] beginning = new double[8];
		for(int i = 0; i < beginning.length; i++){
			beginning[i] = 0.125;
		}
		finalPath = Viterbi.viterbiAlg(obs, beginning, currPath);

		System.out.print("Test: ");
		for(int i = 0; i < obs.length; i++){
			System.out.print(finalPath[i]);
		}
	}
}