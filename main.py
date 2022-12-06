from Partie import Partie
from colorama import init


if __name__ == '__main__':
	init()
	Partie()
	'''joueur=Joueur("nom")
	sousMarin = SousMarin(4)
	joueur.getMer().ajouterSousMarin(sousMarin)
	sousMarin.placer(Coordonnee(1, 2, 2), Direction.DROITE)
	print(joueur.getMer().getSousMarins()[0].getCoords())
	print(joueur.getMer().getSousMarins()[0])'''