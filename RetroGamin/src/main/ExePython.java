package main;

import java.io.BufferedReader;
import java.io.InputStreamReader;


public class ExePython {
public Process pythonMenu, pythonGame;
	public ExePython() {
		try {
			new FileManage();
			ProcessBuilder pythonm = new ProcessBuilder("python","Main_Menu.py");
			pythonMenu = pythonm.start(); 		//Executes the pygame
			BufferedReader in = new BufferedReader(new InputStreamReader(pythonMenu.getInputStream()));
			String[] AllPythonPrints = new String[1];
			int length = 0;
			while(pythonMenu.isAlive()) {
				String string = in.readLine();//this can get input from console
				if(string != null) {
					length++;
					String[] copy = AllPythonPrints;
					AllPythonPrints = new String[length];
					for(int copyar = 0; copyar < length-1; copyar++) { //makes the new string part of the array
						AllPythonPrints[copyar] = copy[copyar];
					}
					AllPythonPrints[length-1] = string;
				}
			}
			for(int findRUN = 0; findRUN < length; findRUN++) {
				String substring = AllPythonPrints[findRUN].substring(0, 5);
				if(substring.equals("#RUN#")) {
					runGame(AllPythonPrints[findRUN].substring(5));
					break;
				}else if(substring.equals("#END#")) { //probably won't be used in final version i'm just sick of infinite subprocesses
					break;
				}
			}
			in.close();
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void runGame(String pygame) {
		try {
			ProcessBuilder pythong = new ProcessBuilder("python","projects/"+pygame);
			pythonGame = pythong.start();
			while(pythonGame.isAlive()) {
				Thread.sleep(5); //@TODO test if this affects pygame
			}
			new ExePython(); //reopens the menu once the game is closed
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
			new ExePython(); //Starts the Main_Menu pygame
	}
	
}
