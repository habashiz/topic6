# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import os, sys, stat

from pathModule import *
from wordModule import *
from makeImp import *

listFiles = list()

directory = input("Veuillez indiquer un reperoitre: ")
listFiles = getFilesDirectory(directory)
print(listFiles)

mot = input("Veuillez indiquer le mot que vous vouler classer autant qu'important: ")

makeImportantToWord(directory, listFiles, mot)
#myFonction (directory, listFiles, mot)