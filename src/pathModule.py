import os 

def getFilesDirectory(directory):
    #return os.listdir(directory)
    maliste = list()
    for element in os.listdir(directory):
    	if element.endswith('html'):
    		maliste.append(element)
    return maliste		