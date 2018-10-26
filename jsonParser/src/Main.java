import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

import org.json.simple.parser.ParseException;

import gestionJSON.LectureJSON;

public class Main {

	public static void main(String[] args) {
		if(args.length<2) {
			System.out.println("Utilisation: jsonParser NOM_FICHIER.json NOM_FICHER.txt [SEPARATEUR_DE_DOCUMENT]");
			System.out.println("\nLe SEPARATEUR_DE_DOCUMENT est une chaîne de texte qui permet de repérer les groupe d'information appartenant au même document.");
		}
		else {
			try {
				ArrayList<String> lines=LectureJSON.readJSON(new FileReader(args[0]));
				FileWriter file=new FileWriter(args[1]);
				String docSeparator="";
				if(args.length>2) docSeparator=args[2];
				for(String s: lines) {
					if(s!=null) {
						if(s.compareTo("\n")!=0) file.write(s+"\n");
						else file.write(docSeparator+s);
					}
					else file.write(s+"\n");
				}
				file.flush();
				file.close();
			} catch (ParseException e) {
				e.printStackTrace();
				System.err.println("Le fichier d'entrée "+args[0]+" n'est pas convenablement formaté en JSON !\n L'élément racine doit être un tableau JSON contenant des objets JSON !");
			} catch (FileNotFoundException e) {
				e.printStackTrace();
				System.err.println("Les fichiers "+args[0]+" et "+args[1]+" sont introuvable !\nVérifier que vous avez les droits de lecture sur ces fichiers !");
			} catch (IOException e) {
				e.printStackTrace();
				System.err.println("Impossible de lire ou d'écrire !\nVérifier que vous avez les droits de lecture et d'écriture !");
			}
		}
	}
}