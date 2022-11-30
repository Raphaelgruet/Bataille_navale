from Joueur import Joueur
from Outils import cls, posXY
from Mer import Mer
from colorama import Fore, Style, Back
from Coordonnee import Coordonnee
from SousMarin import SousMarin
from Direction import Direction
class partie:

	__joueurs = [None, None]
	__temps = 0

	def __init__(self):
		partie.lancementPartie(self)

	def lancementPartie(self):
		cls()
		print(Back.GREEN)
		Mer.affichagePlateauVide(1, 2)
		print(Style.RESET_ALL)
		posXY(1,24)
		print("boujour, vous voici sur le jeu de bateille navale ")
		#input("appuyer sur entrer pour commencer la partie")
		cls()

		#creation des joueurs
		for i in range(2):
			self.__joueurs[i] = Joueur(input("Le joueur " + str(i+1) + " entre son prénom :")) #Creation des joueurs à partir du nom entré dans le terminal

		print("Cette bataille opposera", self.__joueurs[0].getNom().upper(), "contre", self.__joueurs[1].getNom().upper())
		print("Bonne bataille !")

		#input()
		cls() # <== Je sais pas à quoi ça sert mais ça a pas l'air de faire grand chose

		#savoir la couleur
		self.__joueurs[0].choixCouleur()
		if self.__joueurs[0].getCouleur() == "B":
			self.__joueurs[1].setCouleur("R")
		else:
			self.__joueurs[1].setCouleur("B")

		print(self.__joueurs[0], "a choisi la couleur", self.__joueurs[0].getCouleur() + "," , self.__joueurs[1], "aura donc la couleur", self.__joueurs[1].getCouleur())

		#placement des sous-marins
		for i in range(2):
			print (self.__joueurs[i], "place ses sous-marins")
			#Les sous-marins sont ajoutés dans la mer du joueur
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(4))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(3))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(3))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(2))
			#Attribution des positions des sous-marins du joueur
			for j in range(len(self.__joueurs[i].getMer().getSousMarins())):
				x = int(input("Entrez la ligne du debut de votre sousMarin " + str(j+1) + "\n"))
				y = int(input("Entrez la colone du debut de votre sousMarin " + str(j+1) + "\n"))
				z = int(input("Entrez la profondeur du debut de votre sousMarin " + str(j+1) + "\n"))
				direction = input("Entrez la direction de votre sousMarin " + str(j+1) + " (\"D\"=DROITE, \"G\"=GAUCHE, \"H\"=HAUT, \"B\"=BAS)\n")
				coord = Coordonnee(x, y, z)
				self.__joueurs[i].getMer().getSousMarins()[j].placer(coord, direction)
		cls()
		print(Back.GREEN)
		Mer.affichagePlateauVide(1, 2)
		print(Style.RESET_ALL)

		if self.__joueurs[0].getcouleur() == "B":
			couleur = Back.BLUE
		for i in sousMarin.getCoords().keys():
			x,y=i.emplacementCoordonnee()
			affichagePion(x, y, couleur)
		#placement des sousmarin
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

def test():
	# affichage d'une coordonne sur plateau
	c = Coordonnee(9, 1, 1)
	print(Style.RESET_ALL)
	print(Back.RED)
	x, y = c.emplacementCoordonnee()
	posXY(x, y)
	print("   ")
	posXY(x, y + 1)  # a tester
	print("   ")
	print(Style.RESET_ALL)
	input()
	#def saugerde(self...):
	#def savegarde(self...)