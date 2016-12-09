# Aftec
# ZAIDI Hakim
# CDI 2ème année
# Topic 6 : Modifier du HTML avec Python

import os, sys, stat

from pathModule import *
from wordModule import *

print("Ce programme permet d'entourer un mot avec une balise statique \n<span class=important/> sur un fichier html depuis un repertoire donné. \nAttention, ne jamais passer en parametre un mot correspondant à la syntaxe \ndes balises html afin d'eviter des erreurs dans votre code ")
print("********************************************************************************")
#bool indiquant l'execution ou non du programme
execution = True
while(execution):
	#Instanciation de deux listes corespondant respectivement a la liste des fichier html dans le repertoire et de la liste des fichiers modifiés depuis notre méthode correspondante
	listFilesDirectory = list()
	listFilesModified = list()

	directory = input("Veuillez indiquer un repertoire: ")
	#La méthode est importée depuis le module "pathModule" est permet de lister les fichiers html centenus dans le repertoire indiqué 
	listFilesDirectory = getFilesDirectory(directory)
	print("Ce repertoire contient les fichiers html suivants: ")
	print(listFilesDirectory)
	if len(listFilesDirectory) != 0:
		mot = input("Veuillez indiquer le mot que vous voulez entourer avec la balise <span class='important'/>: ")
		#La méthode est importée depuis le module "wordModule" est permet d'inserer une balise span class important sur du contenu html
		listFilesModified = makeWordImportant(directory, listFilesDirectory, mot)
		if len(listFilesModified) != 0:
			print("Les fichiers modifiés sont : ")
			print(listFilesModified)
			print("Une copie des fichiers initiaux est sauvegardée avec le nom initial du fichier et l'extention .old dans le même repertoire")
		else :
			print("Aucun fichier ne contient le mot passé en parametre, par conséquent aucun fichier n'a était modifié")

		exe = input("Si vous voulez reéxecuter le programme taper o, si non taper n : ")
		if exe == 'n':
			execution = False
	else : 
		print("Aucun fichier html trouvé dans ce repertoire")