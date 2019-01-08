# Named-entity recognition (NER)
---
Application de graphes Unitex sur tex :
  - deplacer/copier l'executable `LocatePattern.sh` dans le même répertoire que l'exécutable des commandes UniteX `UnitexToolLogger`.
  - exécuter `LocatePattern.sh` depuis son nouvel emplacement avec les paramètres suivants :
		-f : chemin du ficher texte.
		-c : cehmin de dossier Unitex-GramLab.*.*/French
		-g : chemin de graphe/automate Unitex à appliquer

Utilisation des programmes python:
  - version de python : -python3
  - modules requis:
    -nltk
    -scikit-learn
    -spacy
    -sapcy_lefff
    -msgpack<0.6.0

Lancement test : `python3 -m spacy download fr` puis `python3 main.py -i inputfile.txt -o outputfile`

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
