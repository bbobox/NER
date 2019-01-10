# Named-entity recognition (NER)
---
Application de graphes Unitex sur tex :
  - deplacer/copier l'executable `LocatePattern.sh` dans le même répertoire que l'exécutable des commandes UniteX `UnitexToolLogger`.
  - exécuter `LocatePattern.sh` depuis son nouvel emplacement avec les paramètres suivants :
		-f : chemin du ficher texte.
		-c : cehmin de dossier Unitex-GramLab.*.*/French
		-g : chemin de graphe/automate Unitex à appliquer

Utilisation du programmes python pour déterminer la fréquence des mots les plus déterminants:
  - version de python: python3
  - modules requis:
    - nltk
    - scikit-learn
    - spacy
    - sapcy_lefff
    - msgpack<0.6.0

Vous devez également télécharger la banque de langue de spacy: `python3 -m spacy download fr`

Lancement: `python3 main.py -i inputfile.txt -o outputfile [-m <mingram>] [-M <maxgram>] [-l <lemmatise true|false>] [-s <stopwords true|false>] [-S <separator>] [-p <pattern>]`

__Liste des arguments:__
  - -i: chemin du fichier taggué par Unitex. __OBLIGATOIRE !__
  - -o: chemin du fichier de sortie au foramt JSON. Il est inutile de préciser l'extension du fichier qui sera automatiquement ajouté. __OBLIGATOIRE !__
  - -m: nombre de n-gram minimal. 1 par défaut.
  - -M: nombre de n-gram maximal. n-gram minimal par-défaut.
  - -l: indique si le fichier d'entrée doit être lemmatisé. true par défaut.
  - -s: indique si l'on retire les stopwords du fichier d'entrée. true par défaut.
  - -S: chaîne de caractère indiquant le séparateur de document dans le fichier d'entrée.
  - -p: chaîne de caractère à rechercher dans le fichier d'entrée et sur laquelle sera établie la fréquence des mots les plus déterminants. "" par défaut, ce qui veut dire pas de recherche particulière.

# JsonParser
---
Parser de fichier JSON en ligne de commande pour mettre sous forme de paragraphe les informations d'en-tête de sites webs (balise title, l'url et les métats-descriptions) stocké en JSON.
__Requiert JAVA !__

## Utilisation
Il prend en entrée un fichier JSON, le nom du fichier de sortie et optionnellment une chaîne de caractère qui servira à séparer les informations de deux sites.
Format de la commande dans une console:
```sh
jsonParser.jar fichier_entre.json fichier_sortie.txt [séparateur]
```

`jsonParser.jar` est une archive JAVA auto-exécutable et devrait fonctionner sans appel explicite à JAVA. Cependant, si votre système d'exploitation n'a pas lié le format `.jar` à JAVA, il se peut que vous deviez précéder la commande ci-dessus par `java -jar`.
