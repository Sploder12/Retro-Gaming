package main;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;

public class FileManage {
	public FileManage() { //eventually it will get them from github or some other website to conserve pi space
		String names = "";
		File folder = new File("projects");
		File[] listOfProjects = folder.listFiles();
		try {
			BufferedWriter findprojs = new BufferedWriter(new FileWriter("projlist.txt"));
			for(short py = 0; py < listOfProjects.length; py++) { //Using .length istead of making a variable because i'd rather-
				names = listOfProjects[py].getName();			 //-have the pi use cpu then ram because reloading is allowed to take long
				findprojs.write(names);
				findprojs.newLine();
			}
			findprojs.close(); //creates a file with all the names of the projects to be referenced in the Main_Menu.py
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
}
