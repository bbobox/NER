#-*- coding: utf-8 -*-

import treetaggerwrapper  # For proper print of sequences.
import pprint

class WebSite:
    """
    Represente un Site Web d'association et son contenu
    """

    def __init__(self,url,desc,title):

        self.title = title
        self.url = url
        self.desc = desc
        self.nwords = 0

    def setDesc(self, text):
        self.desc = text


    def printDesc(self):
        print(self.desc)

    def setActivity(self,activity):
        """
        tye d'activite
        """
        self.activity = activity
        
    def wordsNumber(self, n):
        self.nwords = n        




class Word:

    """
    Represente un mot du dictionnaire
    """
    def __init__(self,word):

        self.content = word;
        self.listDoc = {} #"liste des sites lequel le mot apparait"
        


    def linkToText(self, url, occ):
        info = {'occ': occ}
        self.listDoc[url]= info

class Dictionnary:
    """
    Represente le dictionnaire

    """

    def __init__(self):
        self.listeNoeudFils = []
        self.racineArbre = Word("")

    def ajoutNoeudFils(self, fils): # Ajout d'un fils dans l'arbre
        self.listeNoeudFils.append(fils)

    def estFeuille(self):
        return (self.listeNoeudFils == [])

    def ajoutMot(self, mot):
        #print("Parcours de :",self.racineArbre.content)
        if (len(self.listeNoeudFils) == 0):
            if(self.racineArbre == ""):
                A = Dictionnary()
                A.racineArbre = mot
                self.listeNoeudFils.append(A)
            else:
                m = self.racineArbre
                B = Dictionnary()
                B.racineArbre = m
                A = Dictionnary()
                A.racineArbre = mot
                if (A.racineArbre.content < B.racineArbre.content):
                    self.listeNoeudFils.append(A)
                    self.listeNoeudFils.append(B)
                else:
                    self.listeNoeudFils.append(B)
                    self.listeNoeudFils.append(A)
        else:
            if (len(self.listeNoeudFils) == 1):

                A = self.listeNoeudFils[0]
                B = Dictionnary()
                B.racineArbre = mot
                self.listeNoeudFils = []
                if (A.racineArbre.content < B.racineArbre.content):
                    self.listeNoeudFils.append(A)
                    self.listeNoeudFils.append(B)
                else:
                    self.listeNoeudFils.append(B)
                    self.listeNoeudFils.append(A)

            else:
                a = self.listeNoeudFils[1].racineArbre.content
                if (mot.content < a):
                    #print("Parcours de :",self.listeNoeudFils[0].racineArbre.content)
                    self.listeNoeudFils[0].ajoutMot(mot)
                else:
                    #print("Parcours de :",self.listeNoeudFils[1].racineArbre.content)
                    self.listeNoeudFils[1].ajoutMot(mot)

    def parcoursArbre(self):
        if (self.listeNoeudFils == []):
            print ( "word :", self.racineArbre.content," ",self.racineArbre.listDoc)
            print ("------------------")
        else:
            #print ( "noeud :", self.racineArbre.content)
            #print ("taille neoud:",len (self.listeNoeudFils))
            for i in self.listeNoeudFils:
                i.parcoursArbre()

    def estDansArbre(self, mot):
        res = False
        n = len((self.listeNoeudFils))
        #print("nombre de fils :",n)
        if (n == 0):
            #print("visite de :",self.racineArbre.content)
            if (mot.content == self.racineArbre.content):
                res = True
        else:
              if (n == 1):
                  res = self.listeNoeudFils[0].estDansArbre(mot)
              else:
                  if(mot.content >= self.listeNoeudFils[1].racineArbre.content):
                      res = self.listeNoeudFils[1].estDansArbre(mot)
                  else:
                      res = self.listeNoeudFils[0].estDansArbre(mot)
        return res

    def majMotArbre(self, mot):
        if self.estDansArbre(mot) == False:
            self.ajoutMot(mot)
        else:
            n = len((self.listeNoeudFils))
            if( n == 0):
                print()
                if (mot.content == self.racineArbre.content):
                    #self.racineArbre.listDoc.append(mot.listDoc[0])
                    for i in mot.listDoc:
                        self.racineArbre.listDoc[i]=mot.listDoc[i]
                    #self.racineArbre.listDoc.append(mot.listDoc[0])
                    #self.racineArbre.nbOcc = self.racineArbre.nbOcc + mot.listDoc[0]['nbOcc']
            else:
                if ( n == 1 ):
                     self.listeNoeudFils[0].majMotArbre(mot)
                else:
                    if(mot.content >= self.listeNoeudFils[1].racineArbre.content):
                        self.listeNoeudFils[1].majMotArbre(mot)
                    else:
                        self.listeNoeudFils[0].majMotArbre(mot)

    def recupInfoMot(self, mot_form_text):
        mot = Word(mot_form_text)
        info_mot = mot
        if self.estDansArbre(mot) == False:
            info_mot = None
        else:
            n = len((self.listeNoeudFils))
            if (n == 0):
                if (mot.content == self.racineArbre.content):
                    info_mot = self.racineArbre
            else:
                if (n == 1):
                    info_mot = self.listeNoeudFils[0].recupInfoMot(mot_form_text)
                else:
                    if (mot.content >= self.listeNoeudFils[1].racineArbre.content):
                        info_mot = self.listeNoeudFils[1].recupInfoMot(mot_form_text)
                    else:
                        info_mot = self.listeNoeudFils[0].recupInfoMot(mot_form_text)
        return info_mot

    def __str__(self):
        self.parcoursArbre()
        return "Fin Parcours"


