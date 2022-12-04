from Coordonnee import Coordonnee
from Direction import Direction
from Mer import Mer
from SousMarin import SousMarin
from Partie import partie
from Joueur import Joueur
import fixpath
from colorama import init


if __name__ == '__main__':
	init()
	partie()
	'''joueur=Joueur("nom")
	sousMarin = SousMarin(4)
	joueur.getMer().ajouterSousMarin(sousMarin)
	sousMarin.placer(Coordonnee(1, 2, 2), Direction.DROITE)
	print(joueur.getMer().getSousMarins()[0].getCoords())
	print(joueur.getMer().getSousMarins()[0])'''