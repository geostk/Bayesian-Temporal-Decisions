package heatmapgenerator.model;

import java.util.Arrays;


public class Vertex{
	int x, y;
	char type;
	double heatProb;

	Vertex parent;

	public Vertex(int startx, int starty, char typeIn){
		parent = null;
		x = startx;
		y = starty;
		type = typeIn;
	}

	public void setParent(Vertex parIn){
		parent = parIn;
	}
}