package gestionJSON;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.jsoup.Jsoup;

public class LectureJSON {
	private static JSONParser parser=new JSONParser();

	@SuppressWarnings("unchecked")
	public static ArrayList<String> readJSON(FileReader received) throws ParseException, IOException { //Permet d'avoir la racine du JSON
		ArrayList<String> s=new ArrayList<String>();
		Iterator<JSONObject> iterator=((JSONArray) parser.parse(received)).iterator();
		while(iterator.hasNext()) {
			 JSONObject obj=iterator.next();
             Iterator<String> objIterator=obj.values().iterator();
             while(objIterator.hasNext()) {
            	 String line=objIterator.next();
	        	 if(line!=null) {
	        		 line=line.replace("\u0003", "");
	        		 line=line.replace("\u0092", "'");
	        		 line=line.replace("\u009c", "œ");
	        		 line=line.replace("\t", "");
	        		 line=line.replace("\r", "");
	        		 line=line.replace("\n", " ");
	        		 line=Jsoup.parse(line).text();
	        		 String[] splitted=line.split(" ");
	        		 line="";
	        		 for(int i=0; i<splitted.length; i++) {
	        			 String word=splitted[i];
	        			// A cause d'un bug de Unitex qui ne prend pas en charge les mots de plus de 1004 caractères
	        			 if(word.length()>1004) {
	        				 word=word.substring(0, 1003);
	        				 splitted[i]=word;
	        			 }
	        			 line=line+word+" ";
	        		 }
	        		 line=line.trim();
	        	 }
	        	 else line="";
	        	 s.add(line);
             }
             s.add("\n"); // pour séparer les sites
        }
		return s;
	}
}