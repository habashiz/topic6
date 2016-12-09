import os, sys, stat

def myFonction (chemin, maliste, word):
	os.chdir(chemin)
	i = 0
	while(i < len(maliste)):
		#indique le nom de fichier à traiter
		nomFichier = maliste[i]
		#Copie du contenu du fichier dans une chaine de caractère qui sera traiter par la suite
		fichier = open(nomFichier, "r")
		makeimportant = "<span class =\"important\">" + word + "</span>"
		contenu = fichier.read().replace(word, makeimportant)
		fichier.close()
		print(contenu)
		i+=1