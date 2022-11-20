from Joueur import joueur
from Outils import cls, posXY
from Mer import Mer
from colorama import Fore, Style, Back
from Coordonnee import Coordonnee

class partie:

	__joueur1 = None
	__joueur2 = None
	__temps = 0

	def __init__ (self, nom1, nom2):
		self.__joueur1 = joueur(nom1)
		self.__joueur2 = joueur(nom2)


	def lancerPartie():
		cls()
		print(Back.GREEN)
		Mer.plateauVide(1, 2)
		c=Coordonnee(9,1,1)
		print(Style.RESET_ALL)
		print(Back.RED)
		x,y=c.emplacementCoordonnee()
		posXY(x,y)
		print("   ")
		posXY(x,y+1) # a tester
		print("   ")
		print(Style.RESET_ALL)
		input()
		"""posXY(1,24)
		print("boujour, vous voici sur le jeu de bateille navale ")
		input("appuyer sur entrer pour commencer la partie")
		cls()
		print("que le joueur 1 entre son prenom")
		joueur1=joueur(input())
		print("que le joueur 2 entre son prenom")
		joueur2=joueur(input())
		print("cette bataille opposera ", joueur1.getNom().upper(), " contre ",joueur2.getNom().upper())
		print("bonne bataille")
		input()
		cls()"""


# affichage merJ1
# demande de placement de un sous marin
# affichage merJ1
# demande de placement de un sous marin
# affichage merJ1
# demande de placement de un sous marin
# affichage merJ1
# effacage de la merJ1 et prevention du changement de mer
# affichage merJ2
# demande de placement de un sous marin
# affichage merJ2
# demande de placement de un sous marin
# affichage merJ2
# demande de placement de un sous marin
# affichage merJ2
# effacage de la merJ2 et prevention du commencement
# affichage merJ2Vide et demande au j1 des coordonnees pour impact
# verification du win et affichage resultat
# passage au j2 avec la merVide du j1 et demande des coordonnees pour impact
# affichage resultat
# boucle
# affichage merJ2 et demande au j1 des coordonnees pour impact
# verification du win et affichage resultat
# passage au j2 avec la mer du j1 et demande des coordonnees pour impact
# affichage resultat


	#def saugerde(self...):
	#def savegarde(self...)