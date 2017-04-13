package heatmapgenerator.model;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Map{
	Vertex[][] map;
	int rows = 9;
	int columns = 10;

	int mapID = -1, pathID = -1;
	int initX;
	int initY;

	int[][] groundTruth;

	public Map(File file){
		String line = null;
		groundTruth = new int[100][2];
		if(file != null){
			FileReader fileReader;
			try {
				fileReader = new FileReader(file);
	        	@SuppressWarnings("resource")
				BufferedReader bufferedReader = new BufferedReader(fileReader);
	        	int timesLooped = 0;
	        	while((line = bufferedReader.readLine()) != null){
	        		if(timesLooped < 1){
	        			for(int i = 0; i < line.length(); i++)
	        				if(line.charAt(i) >= '0' && line.charAt(i) <= '9')
	        						if(mapID < -1)
	        							mapID = line.charAt(i) - '0';
	        						else
	        							pathID = line.charAt(i) - '0';
	        		}
	        		else if(timesLooped < 9){
	        			int count = 0;
	        			for(int i = 0; i < line.length(); i++){
	        				switch(line.charAt(i)){
	        					case 'N':
	        						map[timesLooped][count] = new Vertex(timesLooped, count, 'N');
	        						count++;
	        						break;
	        					case 'T':
	        						map[timesLooped][count] = new Vertex(timesLooped, count, 'T');
	        						count++;
	        						break;
	        					case 'B':
	        						map[timesLooped][count] = new Vertex(timesLooped, count, 'B');
	        						count++;
	        						break;
	        					default:
	        						break;
	        				}
	        			}
	        		}
	        		else if(timesLooped < 11){
	        			initX = line.charAt(9) - '0';
	        			initY = line.charAt(12) - '0';
	        		}
	        		else if(timesLooped < 12){
	        			int count = 0;
	        			for(int i = 0; i < line.length(); i++){
	        				if(line.charAt(i) >= '0' && line.charAt(i) <= '9'){
	        					if(count % 2 == 0){
	        						groundTruth[count][0] = line.charAt(i) - '0';
	        						count++;
	        					}
	        					else{
	        						groundTruth[count][0] = line.charAt(i) - '0';
	        					}
	        				}
	        			}
	        		}
	        		else if(timesLooped < 13){
	        			int count = 0;
	        			for(int i = 0; i < line.length(); i++)
	        				if(line.charAt(i) >= 'A' && line.charAt(i) <= 'Z'){

	        				}
	        		}
	        		timesLooped++;
	            }
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
}