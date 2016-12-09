import os 

#La méthode permet de lister les fichiers html dans un repertoire donné
def getFilesDirectory(directory):
    maliste = list()
    try:
    	for element in os.listdir(directory):
    		if element.endswith('html'):
    			maliste.append(element)
    except FileNotFoundError:
    	#Récuperer le repertoire courant
    	repCour = os.getcwd()
    	print("le repertoire indiqué n'existe pas, le dossier courant suivant sera utilisé:  "+repCour)
    	getFilesDirectory(repCour)
    return maliste		