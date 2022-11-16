from Coordonnee import Coordonnee
from Direction import Direction
from Mer import Mer
from SousMarin import SousMarin


def print_hi(name):
	print("fff")

if __name__ == '__main__':
	mer = Mer()
	sousMarin = SousMarin(4)
	mer.ajouterSousMarin(sousMarin)
	sousMarin.placer(Coordonnee(1, 2, 2), Direction.DROITE)
	print(mer.getSousMarins()[0].getCoords())
	#print(mer.getSousMarins()[0].getCoords()[0])

