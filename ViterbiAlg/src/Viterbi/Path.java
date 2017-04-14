package Viterbi;

public class Path{
	char type;
	int stateNum;
	double[] transProbList;
	double[] emissionProbList;

	public Path(int stateIn){
		stateNum = stateIn;
		emissionProbList = new double[3];
		transProbList = new double[8];
		if(stateIn < 2 || stateIn > 6){
			type = 'H';
			emissionProbList[0] = 0.05;
			emissionProbList[1] = 0.9;
			emissionProbList[2] = 0.05;
		}
		else if(stateIn == 2){
			type = 'T';
			emissionProbList[0] = 0.05;
			emissionProbList[1] = 0.05;
			emissionProbList[2] = 0.9;
		}
		else{
			type = 'N';
			emissionProbList[0] = 0.9;
			emissionProbList[1] = 0.05;
			emissionProbList[2] = 0.05;
		}
		if(stateIn == 2 || stateIn > 4){
			transProbList[stateIn] = 1.0;
		}
		else{
			transProbList[stateIn] = 0.1;
			transProbList[stateIn + 1] = 0.9;
		}
	}

	public void changeDir(){
		if(stateNum == 4){
			transProbList[5] = 0.0;
			transProbList[stateNum] = 1.0;
		}
		else if(stateNum == 5){
			transProbList[5] = 0.1;
			transProbList[7] = 0.9;
		}
		else if(stateNum < 5){
			transProbList[stateNum + 1] = 0.0;
			transProbList[stateNum + 3] = 0.9;
		}
	}
}