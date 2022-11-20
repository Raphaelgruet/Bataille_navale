from Coordonnee import Coordonnee
from Direction import Direction
from SousMarin import SousMarin
from Partie import partie
import fixpath
from colorama import init


if __name__ == '__main__':
	init()
	partie()
	'''mer = Mer()
	sousMarin = SousMarin(4)
	mer.ajouterSousMarin(sousMarin)
	sousMarin.placer(Coordonnee(1, 2, 2), Direction.DROITE)
	print(mer.getSousMarins()[0].getCoords())
	print(mer.getSousMarins()[0])'''




