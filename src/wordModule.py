import os, sys, stat

def makeWordImportant(chemin, maliste, word):
	#Se placer dans le repertoire indiquer par l'utilisateur
	os.chdir(chemin)
	listFilesModified = list()
	i = 0
	while(i < len(maliste)):
		#Déclaration de la Chaine de caractère contenant le code modifié final
		contenuFinal = ""
		#indique le nom de fichier à traiter
		nomFichier = maliste[i]
		#Ouvrir les fichier a traiter un à un
		fichier = open(nomFichier, "r")
		#Instancier une chaine de caractere avec les parametres d'une balise <span class='important'/> tel que demander dans le projet
		makeimportant = "<span class =\"important\">" + word + "</span>"
		#Instancier une chaine de caractère avec le contenu de notre fichier initial 
		contenuFichier = fichier.read()
		#Tester si le mot fait partie du fichier
		if word in contenuFichier:
			#Ajouter le nom du fichier dans une liste de fichiers modifiés
			listFilesModified.append(nomFichier)
			contenuFinal = contenuFichier.replace(word, makeimportant)
			#print(contenuFinal)
			fichier.close()
			#renomage du fichier initial avec l'ajout de l'extension (.old)
			newNameFile = nomFichier + ".old"
			try:
				os.remove(newNameFile)
			except FileNotFoundError:
				pass
			os.chmod(nomFichier, stat.S_IWRITE)
			os.rename(nomFichier, newNameFile)
			#Création d'un nouveau fichier et ecriture de notre nouveau contenu traité
			fichierFinal = open(nomFichier, "w")
			fichierFinal.write(contenuFinal)
			fichierFinal.close()
		i+=1
	return listFilesModified	