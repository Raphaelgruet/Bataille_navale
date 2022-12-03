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
	def demandeEmplacement(self,j):
		x, y, z = -1, -1, -1
		direction = None
		while not 0 < x < 11: #Valeur "hardcoded" à changer avec la taille de la mer
			try:
				x = int(input("Entrez la ligne du debut de votre sousMarin " + str(j + 1) + "\n"))
			except:
				print("vous avez fait une erreur, veillez recommencer")

		while not 0 < y < 6:
			try:
				y = int(input("Entrez la colone du debut de votre sousMarin " + str(j + 1) + "\n"))
			except:
				print("vous avez fait une erreur, veillez recommencer")

		while not 0 < z < 4:
			try:
				z = int(input("Entrez la profondeur du debut de votre sousMarin " + str(j + 1) + "\n"))
			except:
				print("vous avez fait une erreur, veillez recommencer")

		while not (direction == "D" or direction == "G" or direction == "H" or direction == "B"): #FAIT : Correction de la condition
			try:
				direction = input("Entrez la direction de votre sousMarin " + str(j + 1) + " (\"D\"=DROITE, \"G\"=GAUCHE, \"H\"=HAUT, \"B\"=BAS)\n")
			except:
				print("vous avez fait une erreur, veillez recommencer")
		return direction,x,y,z

	def lancementPartie(self):
		"""
		cls()
		Mer.affichagePlateauVide(1, 2)
		posXY(1,24)
		print("boujour, vous voici sur le jeu de bateille navale ")
		input("appuyer sur entrer pour commencer la partie")
		cls()"""
		#creation des joueurs
		for i in range(2):
			self.__joueurs[i] = Joueur('''input("Le joueur " + str(i+1) + " entre son prénom :")''' "b") #Creation des joueurs à partir du nom entré dans le terminal

		"""
		print("Cette bataille opposera", self.__joueurs[0].getNom().upper(), "contre", self.__joueurs[1].getNom().upper())
		print("Bonne bataille !")
		input()
		cls() # <== Je sais pas à quoi ça sert mais ça a pas l'air de faire grand chose
		#savoir la couleur
		self.__joueurs[0].choixCouleur("B")
		"""

		self.__joueurs[0].setCouleur("B")
		if self.__joueurs[0].getCouleur() == "B":
			self.__joueurs[1].setCouleur("R")
		else:
			self.__joueurs[1].setCouleur("B")

		print(self.__joueurs[0], "a choisi la couleur", self.__joueurs[0].getCouleur() + "," , self.__joueurs[1], "aura donc la couleur", self.__joueurs[1].getCouleur())

		#placement des sous-marins
		for i in range(2):
			#Les sous-marins sont ajoutés dans la mer du joueur
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(4))
			'''self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(3))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(3))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(2))''' #En commentaires pour des tests plus rapide
			#Attribution des positions des sous-marins du joueur
			for j in range(len(self.__joueurs[i].getMer().getSousMarins())):

				if self.__joueurs[i].getCouleur() == "B":
					couleur = Back.BLUE
				else:
					couleur = Back.RED
				cls()
				Mer.affichagePlateauVide(1, 2, couleur)


				#print(self.__joueurs[i].getMer().getSousMarins()[j].getCoords()) #je n'est pas de coordonne??????? je veux faire comme la fonction
				for g in self.__joueurs[i].getMer().getSousMarins()[j].getCoords().keys():# la veux les differents positions du sous marin
					x, y = g.emplacementCoordonnee() #la je les transforme en position pour le terminale cdm
					self.__joueurs[i].getMer().affichagePion(x, y, couleur) # et la je les affiche
				posXY(1, 24)

				#Placement des sous-marins
				print(self.__joueurs[i], "place ses sous-marins")
				direction, x, y, z = partie.demandeEmplacement(self,j)
				coord = Coordonnee(x, y, z)

				self.__joueurs[i].getMer().getSousMarins()[j].placer(coord, direction)
				input()
				cls()
		cls()
		posXY(1,1)
		print("nous pouvons commencer")
		print("au joueur " + self.__joueurs[0].getNom() + " de commencer")
		input()
		cls()
		#commencemment partie
		gagne=False
		while not gagne:

			for i in range(2):
				if self.__joueurs[i].getCouleur() == "B":
					couleur = Back.RED
					couleur1 = Back.RED
				else:
					couleur = Back.BLUE
					couleur1 = Back.RED
				Mer.affichagePlateauVide(1, 2,couleur)
				for g in self.__joueurs[i].getMer().getImpacts():# la veux les differents positions du sous marin
					x,y=g.emplacementCoordonnee() #la je les transforme en position pour le terminale cdm
					self.__joueurs[i].getMer().affichagePion(x, y, couleur) # et la je les affiche
				posXY(1, 24)
				direction, x, y, z=partie.demandeEmplacement(self,j)
				coord = Coordonnee(x, y, z)

				self.__joueurs[i].getMer().getSousMarins()[j].placer(coord, direction)
				input()
				cls()





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