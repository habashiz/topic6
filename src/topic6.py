# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import os 
from pathModule import *

listFiles = list()

directory = input("Veuillez indiquer un reperoitre: ")
listFiles = getFilesDirectory(directory)
print(listFiles)

mot = input("Veuillez indiquer le mot que vous vouler classer autant qu'important: ")
