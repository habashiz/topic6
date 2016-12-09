import os, sys, stat

def makeImportantToWord(chemin, maliste, word):
	#Mise en place dans le repertoire indiquer par l'utilisateur
	os.chdir(chemin)
	i = 0
	while(i < len(maliste)):
		contenuFinal = ""
		#indique le nom de fichier à traiter
		nomFichier = maliste[i]
		#Ouvrir les fichier a traiter un à un
		fichier = open(nomFichier, "r")
		#Instancier uen chaine de caracter avec les parametre d'une balise span en class important tel demander dans le projet
		makeimportant = "<span class =\"important\">" + word + "</span>"
		#Instancier une chaine de caractère avec le contenu de notre fichier initial 
		contenuFichier = fichier.read()
		print(contenuFichier)
		#Tester si un le mot fait partie du fichier
		if word in contenuFichier:
			contenuFinal = contenuFichier.replace(word, makeimportant)
			#print(contenuFinal)
			fichier.close()
		#renomage du fichier initial avec l'ajout de l'extension (.old)
			newNameFile = nomFichier + ".old"
			os.chmod(nomFichier, stat.S_IWRITE)
			os.rename(nomFichier, newNameFile)
			#Création d'un nouveau fichier et ecriture de notre nouveau contenu traité
			fichierFinal = open(nomFichier, "w")
			fichierFinal.write(contenuFinal)
			fichierFinal.close()
		i+=1