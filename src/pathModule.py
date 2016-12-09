import os 

#La méthode permet de lister les fichiers html dans un repertoire donné
def getFilesDirectory(directory):
    maliste = list()
    for element in os.listdir(directory):
    	if element.endswith('html'):
    		maliste.append(element)
    return maliste		