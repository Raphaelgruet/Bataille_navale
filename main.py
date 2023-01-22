import sys

from Partie import Partie
from colorama import init
from vue.FenetrePrincipal import FenetrePrincipal

# Fichier main

if __name__ == '__main__':
	init()
	for arg in sys.argv:
		if arg == "nogui":
			Partie().lancementPreparation()
	fenetre = FenetrePrincipal()
