import os

def makeImportantToWord(chemin, maliste, word):
	#Mise en place dans le repertoire indiquer par l'utilisateur
	os.chdir(chemin)
	i = 0
	while(i <= len(maliste)):
		#indique le nom de fichier à traiter
		nomFichier = maliste[i]
		#Copie du contenu du fichier dans une chaine de caractère qui sera traiter par la suite
		fichier = open(nomFichier, "r")
		contenu = fichier.read()
		fichier.close()
		#renomage du fichier initial avec l'ajout de l'extension (.old)
		newNameFile = nomFichier + ".old"
		rename(nomFichier, newNameFile)
		#Si notre string representant le fichier initial contient le mot qu'on voudrais intéragir avec
		if contenu.find(word):
			#instanciation d'une chaine de caractere avec une balise entourant le mot escompé
			makeimportant = "<span class =\"important\">" + word + "</span>"
			#Parcour de la chaine de caractere et ecriture de la balise "important"
			contenu.replace(word, makeimportant)
			#Création d'un nouveau fichier et ecriture de notre nouveau contenu traité
			fichierFinal = open(nomFichier, "w")
			fichierFinal.write(contenu)