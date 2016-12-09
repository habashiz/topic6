# ZAIDI Hakim
# CDI 2ème année
# Topic 6 : Modifier du HTML avec Python

import os, sys, stat

from pathModule import *
from wordModule import *

#bool indiquant l'execution du programme
execution = True
print("Ce programme permet d'entourer un mot avec une balise statique \n <span class=important/> sur un fichier html depuis un repertoire donnée")
while(execution):
	#Instanciation de deux listes corespondant respectivement a la liste des fichier html dans le repertoire et de la liste des fichiers modifiés depuis notre méthode correspondante
	listFiles = list()
	listFilesModified = list()

	directory = input("Veuillez indiquer un repertoire: ")
	#La méthode est importée depuis le module "pathModule" est permet de lister les fichiers html centenus dans le repertoire indiqué 
	listFiles = getFilesDirectory(directory)
	print(listFiles)

	mot = input("Veuillez indiquer le mot que vous voulez entourer de balise span class important: ")

	#La méthode est importée depuis le module "wordModule" est permet d'inserer une balise span class important sur du contenu html
	listFilesModified = makeImportantToWord(directory, listFiles, mot)
	if len(listFilesModified) != 0:
		print("Les fichiers contenant le mot et modifiés sont : ")
		print(listFilesModified)
		print("Une copie des fichiers initiaux est sauvegarder avec le nom initial du fichier avec l'extention .old sur le mème repertoire")
	else :
		print("Aucun fichier ne contient le mot passé en parametre, par consequent aucun fichier n'a etait modifié")

	exe = input("Si vous voulez reexecuter le programme taper o, si non taper n : ")
	if exe == 'n':
		execution = False	