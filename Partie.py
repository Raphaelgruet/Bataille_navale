import os

import yaml
from Joueur import Joueur
from Outils import cls, posXY
from Mer import Mer
from colorama import Fore, Style, Back
from Coordonnee import Coordonnee
from SousMarin import SousMarin
from Direction import Direction
from datetime import datetime

from vue.FenetreJoueur import FenetreJoueur


# Class Partie
class Partie:
	__joueurs = [None, None]
	__id = "partie_" + datetime.now().strftime("%H_%M_%S")
	__temps = 0
	tour = 1
	dimensionsMers = Coordonnee(10, 5, 3)

	def __init__(self):
		pass
		#self.lancementPreparation()
		#self.partirSur2Ecran()
		#self.charger("partie_22_09_47")
		#self.lancementGraphique()
		#self.partirSur2Ecran()

	def lancementGraphique(self):
		fenetres = []

		# Creation des joueurs
		for i in range(2):
			self.__joueurs[i] = Joueur("Joueur " + str(i+1))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(4))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(3))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(3))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(2))

		# Creation des fenêtres
		for i in range(2):
			fenetre = FenetreJoueur(self.__joueurs[i], self.__joueurs[(i + 1) % 2])
			fenetres.append(fenetre)

		while fenetres[0].estPret() == False or fenetres[1].estPret() == False:
			fenetres[0].getFenetre().update()
			fenetres[1].getFenetre().update()

		for fenetre in fenetres:
			fenetre.afficheJeu()

		while not self.testVictoire():
			fenetres[0].setJouable(True)
			while fenetres[0].estJouable():
				for fenetre in fenetres:
					fenetre.getFenetre().update()
			fenetres[1].setJouable(True)
			while fenetres[1].estJouable():
				for fenetre in fenetres:
					fenetre.getFenetre().update()

		gagnant = self.testVictoire()
		print("#####################################\n")
		print("  VICTOIRE de " + str(gagnant) + " !\n")
		print("#####################################")
		'''for fenetre in fenetres:
			fenetre.mainloop()'''

	def lancementPreparation(self):

		# Partie test
		cls()
		Mer.affichagePlateauVide(1, 2, Back.WHITE)
		posXY(1, 24)
		print("---------- Bataille navale ----------")
		input("appuyer sur entrer pour commencer la partie ...")
		cls()

		# Creation des joueurs

		self.__joueurs[1] = Joueur("b")
		self.__joueurs[0] = Joueur("c")  # Creation des joueurs à partir du nom entré dans le terminal
		print("Cette bataille opposera", self.__joueurs[0].getNom().upper(), "contre",
			  self.__joueurs[1].getNom().upper())
		print("Bonne bataille !")
		input()
		cls()

		# choix couleur

		self.__joueurs[0].setCouleur(Back.YELLOW)
		self.__joueurs[1].setCouleur(Back.GREEN)
		self.__joueurs[1].setCouleur2(Fore.LIGHTGREEN_EX)
		self.__joueurs[0].setCouleur2(Fore.LIGHTYELLOW_EX)
		print(self.__joueurs[0], "a choisi la couleur", self.__joueurs[0].getCouleur() + "   ", Style.RESET_ALL, ",",
			  self.__joueurs[1],
			  "aura donc la couleur", self.__joueurs[1].getCouleur() + "   ", Style.RESET_ALL)
		input()
		cls()

		'''
		Mer.affichagePlateauVide(1, 2, Back.WHITE)
		print("Bonjour, vous voici sur le jeu de bataille navale")
		input("Appuyer sur entrer pour commencer la partie")
		cls()

		# Creation des joueurs
		for i in range(2):
			self.__joueurs[i] = Joueur(input("Le joueur " + str(
				i + 1) + " entre son prénom :"))  # Creation des joueurs à partir du nom entré dans le terminal
		print("Cette bataille opposera", self.__joueurs[0].getNom().upper(), "contre",
			  self.__joueurs[1].getNom().upper())
		print("Bonne bataille !")
		input()
		cls()

		# choix couleur
		self.__joueurs[0].choixCouleur()
		if self.__joueurs[0].getCouleur() == Back.GREEN:

			self.__joueurs[1].setCouleur2(Fore.LIGTHYELLOW_EX)
			self.__joueurs[1].setCouleur(Back.YELLOW)
		else:
			self.__joueurs[1].setCouleur(Back.GREEN)
			self.__joueurs[1].setCouleur2(Fore.LIGTHGREEN_EX)
		print(self.__joueurs[0], "a choisi la couleur", self.__joueurs[0].getCouleur() + "   ", Style.RESET_ALL, ",",
			  self.__joueurs[1], "aura donc la couleur", self.__joueurs[1].getCouleur() + "   ", Style.RESET_ALL)
		input()'''

		# Placement des sous-marins
		for i in range(2):
			# Les sous-marins sont ajoutés dans la mer du joueur
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(4))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(3))
			'''self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(3))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(2))'''

			# Attribution des positions des sous-marins du joueur
			for j in range(len(self.__joueurs[i].getMer().getSousMarins())):
				cls()
				self.__joueurs[i].getMer().affichage(Back.WHITE, self.__joueurs[i].getCouleur(), True)
				# Placement des sous-marins
				print(self.__joueurs[i].getCouleur2(), self.__joueurs[i], "place ses sous-marins", Style.RESET_ALL)
				placer = False
				while not placer:
					try:
						# print(
						# direction, x, y, z = Partie.demandeEmplacement(self, j)
						# coord = Coordonnee(x, y, z)
						coord = Coordonnee(1, j + 1, 1)
						# self.__joueurs[i].getMer().getSousMarins()[j].placer(coord, direction)
						self.__joueurs[i].getMer().getSousMarins()[j].placer(coord, Direction.DROITE)
						placer = True
					except Exception as e:
						print(e)

				if j == len(self.__joueurs[i].getMer().getSousMarins()) - 1:
					self.__joueurs[i].getMer().affichage(Back.WHITE, self.__joueurs[i].getCouleur(), True)
			input()

		self.sauvegarder()
		cls()
		posXY(1, 1)
		print("La partie commence")
		print(Fore.LIGHTCYAN_EX,"C'est à " + self.__joueurs[0].getNom() + " de commencer")
		input()
		cls()
		for i in range(2):
			if self.__joueurs[i].getCouleur() == Back.YELLOW:
				self.__joueurs[i].setCouleur(Back.GREEN)
			else:
				self.__joueurs[i].setCouleur(Back.YELLOW)

		self.lancementPartie()

	def lancementPartie(self):

		# Commencement de la partie
		while True:
			i = (self.tour-1)%2
			self.__joueurs[i].getMer().affichage(self.__joueurs[i].getCouleur(), self.__joueurs[i].getCouleur(), False)
			# Detection coordonnées + impact
			print(self.__joueurs[i].getCouleur2())
			x, y, z = self.demandeImpact(20)
			coord = Coordonnee(x, y, z)
			self.__joueurs[i].getMer().impact(coord)
			print(Style.RESET_ALL)
			self.__joueurs[i].getMer().affichage(self.__joueurs[i].getCouleur(), self.__joueurs[i].getCouleur(), False)

			self.tour += 1
			self.sauvegarder()

			# Détection victoire
			gagnant = self.testVictoire()
			if gagnant is None:
				input()
				cls()
			else:
				print("#####################################\n")
				print("  VICTOIRE de " + str(gagnant) + " !\n")
				print("#####################################")
				return True

	# TODO problème "en vu"
	def partirSur2Ecran(self):
		cls()
		Mer.affichagePlateauVide(1, 2, Back.WHITE)
		print("Bonjour, vous voici sur le jeu de bataille navale")
		input("Appuyer sur entrer pour commencer la partie sur deux ecrans differents")
		cls()
		# Creation des joueurs
		for i in range(2):
			self.__joueurs[i] = Joueur(input("Le joueur " + str(
				i + 1) + " entre son prénom :"))  # Creation des joueurs à partir du nom entré dans le terminal
		print("Cette bataille opposera", self.__joueurs[0].getNom().upper(), "contre",
			  self.__joueurs[1].getNom().upper())
		print("Bonne bataille !")
		input()
		cls()

		# choix couleur
		self.__joueurs[0].choixCouleur()
		if self.__joueurs[0].getCouleur() == Back.GREEN:

			self.__joueurs[1].setCouleur(Back.YELLOW)
			self.__joueurs[1].setCouleur2(Fore.LIGHTYELLOW_EX)
		else:
			self.__joueurs[1].setCouleur(Back.GREEN)
			self.__joueurs[1].setCouleur2(Fore.LIGHTYELLOW_EX)
		print(self.__joueurs[0], "a cho      isi la couleur", self.__joueurs[0].getCouleur() + "   ", Style.RESET_ALL)
		input()

		# Placement des sous-marin
		# Les sous-marins sont ajoutés dans la mer du joueur
		self.__joueurs[0].getMer().ajouterSousMarin(SousMarin(4))
		self.__joueurs[0].getMer().ajouterSousMarin(SousMarin(3))
		'''self.__joueurs[0].getMer().ajouterSousMarin(SousMarin(3))
		self.__joueurs[0].getMer().ajouterSousMarin(SousMarin(2))'''
		# Attribution des positions des sous-marins du joueur
		for j in range(len(self.__joueurs[0].getMer().getSousMarins())):
			cls()
			self.__joueurs[0].getMer().affichage(Back.WHITE, self.__joueurs[0].getCouleur(), True)
			# Placement des sous-marins
			print(self.__joueurs[0].getCouleur(), self.__joueurs[0], "place ses sous-marins", Style.RESET_ALL)
			placer = False
			while not placer:
				try:
					print(self.__joueurs[0].getCouleur2())
					# direction, x, y, z = Partie.demandeEmplacement(self, j)

					# coord = Coordonnee(x, y, z)
					coord = Coordonnee(1, j + 1, 1)
					# self.__joueurs[0].getMer().getSousMarins()[j].placer(coord, direction)
					self.__joueurs[0].getMer().getSousMarins()[j].placer(coord, Direction.DROITE)
					placer = True
				except Exception as e:
					print(e)

			if j == len(self.__joueurs[0].getMer().getSousMarins()) - 1:
				print(Style.RESET_ALL)
				self.__joueurs[0].getMer().affichage(Back.WHITE, self.__joueurs[0].getCouleur(), True)
		input()

		cls()
		posXY(1, 1)
		# qui commmence
		print("La partie commence")
		print("C'est à " + self.__joueurs[0].getNom() + " de commencer")
		input()
		cls()
		# Commencement de la partie
		while True:
			self.__joueurs[0].getMer().affichageEnSolo(self.__joueurs[0].getCouleur(), True)
			self.__joueurs[1].getMer().affichageEnSolo(self.__joueurs[1].getCouleur(), False)
			posXY(1, 41)
			print(self.__joueurs[0].getCouleur2())
			print("ou votre adversaire a t-il tire?")
			x, y, z = Partie.demandeImpact(self, 0)
			print(Style.RESET_ALL)
			coord = Coordonnee(x, y, z)
			self.__joueurs[0].getMer().impact(coord)
			coup=False
			while coup==False:
				self.__joueurs[0].getMer().affichageEnSolo(self.__joueurs[0].getCouleur(), True)
				self.__joueurs[1].getMer().affichageEnSolo(self.__joueurs[1].getCouleur(), False)
				posXY(1, 41)
				print("                                        ")
				posXY(1, 41)
				print(self.__joueurs[1].getCouleur2(), "ou avez vous tire?")
				# verification d'un impact unique
				impactUnique=False
				while impactUnique==False:
					posXY(0,0)
					x, y, z = Partie.demandeImpact(self, 0)
					coord = Coordonnee(x, y, z)
					j=0
					for i in self.__joueurs[1].getMer().getImpacts():
						if i == coord:
							j=j+1
						print(j)
					if j == 0:
						impactUnique=True
				typeImpact = ""
				# demande de l'etat de ma case
				while not (typeImpact == "t" or typeImpact == "c" or typeImpact == "r" or typeImpact == "v"):
					typeImpact=self.phraseEnY46("Entrez le resultat de votre impact (si vous avez touche, entrer :\"t\", si vous avous avez coule, entrer :\"c\", si vous avez vous un sous marin, entrer :\"v\", si vous avous avez rien eu, entrer :\"r\"")
				print(Style.RESET_ALL)
				self.__joueurs[1].getMer().impact(coord)
				self.__joueurs[1].getMer().setImpactsType(typeImpact)

				print(Style.RESET_ALL)
				# si coule
				if typeImpact=="c":
					cls()
					self.__joueurs[0].getMer().affichageEnSolo(self.__joueurs[0].getCouleur(), True)
					self.__joueurs[1].getMer().affichageEnSolo(self.__joueurs[1].getCouleur(), False)
					print("indiquez les cases du bateau coule")
					input()
					coule=False
					while coule==False:
						caseIdentifie = False
						while caseIdentifie == False:
							x, y, z = Partie.demandeImpact(self, 0)
							coord = Coordonnee(x, y, z)
							for i in self.__joueurs[1].getMer().getImpacts():
								if i == coord and self.__joueurs[1].getMer().getImpactsType()[self.__joueurs[1].getMer().getImpacts().index(i)]=="t":
									self.__joueurs[1].getMer().getImpactsType()[self.__joueurs[1].getMer().getImpacts().index(i)]="c"
									caseIdentifie = True
						AjoutCoule =""
						while not (AjoutCoule=="y" or AjoutCoule=="n"):
							AjoutCoule =self.phraseEnY46("\"y\" si vous avez un case a ajouter sinon \"n\"")
						self.__joueurs[0].getMer().affichageEnSolo(self.__joueurs[0].getCouleur(), True)
						self.__joueurs[1].getMer().affichageEnSolo(self.__joueurs[1].getCouleur(), False)
						if(AjoutCoule=="n"):
							coule = True
							coup = True
					print(Style.RESET_ALL)
				else:
					ajoutCoup = ""
					while not (ajoutCoup == "y" or ajoutCoup == "n"):
						ajoutCoup = self.phraseEnY46("\"y\" s\'y a des cases en vue sinon\"n\"")
					if (ajoutCoup == "n"):
						coup = True
			# Détection defaite
			if self.__joueurs[0].getPV() == 0:
				print("#####################################\n")
				print("#   VICTOIRE de votre Adversaire!   #\n")
				print("#####################################")
				return True
			else:
				input()
				cls()

	def testVictoire(self):
		# Fonction qui retourne le joueur qui a gagné la partie dans le cas ou celle-ci est terminée,
		# dans le cas contraire la fonction retourne None
		for i in range(2):
			if self.__joueurs[i].getPV() == 0:
				return self.__joueurs[i]
		return None

	def demandeEmplacement(self, j):

		x, y, z = -1, -1, -1
		direction = None
		print("Entrez les coordonnées de votre impact " + str(j + 1) + " :")
		while not 0 < x < Partie.dimensionsMers.getX() + 1:
			try:
				x = int(input("  La COLONNE du debut de votre sous-marin = "))
			except:
				print("vous avez fait une erreur, veillez recommencer")

		while not 0 < y < Partie.dimensionsMers.getY() + 1:
			try:
				y = int(input("  La LIGNE du debut de votre sous-marin = "))
			except:
				print("vous avez fait une erreur, veillez recommencer")

		while not 0 < z < Partie.dimensionsMers.getZ() + 1:
			try:
				z = int(input("  La PROFONDEUR de votre sous-marin = "))
			except:
				print("vous avez fait une erreur, veillez recommencer")

		while not (
				direction == Direction.DROITE or direction == Direction.GAUCHE or direction == Direction.HAUT or direction == Direction.BAS):
			try:
				direction = input(
					"  La DIRECTION de votre sous-marin (\"D\"=DROITE, \"G\"=GAUCHE, \"H\"=HAUT, \"B\"=BAS) = ")
				if direction == "D":
					direction = Direction.DROITE
				elif direction == "B":
					direction = Direction.BAS
				elif direction == "H":
					direction = Direction.HAUT
				else:
					direction = Direction.GAUCHE
			except:
				print("vous avez fait une erreur, veillez recommencer")
		return direction, x, y, z

	def demandeImpact(self, r):

		posXY(1, 42 - r)
		print("                                                                                          ")
		print("                                                                                          ")
		print("                                                                                          ")
		print("                                                                                          ")
		print("                                                                                          ")
		x, y, z = -1, -1, -1
		posXY(1, 42 - r)
		print("Entrez les coordonnées de votre impact :")
		while not 0 < x < Partie.dimensionsMers.getX() + 1:
			try:
				posXY(1, 43 - r)
				print("                                                                                          ")
				posXY(1, 43 - r)
				x = int(input("  La COLONNE de votre impact = "))
			except:
				print("\nvous avez fait une erreur, veillez recommencer")

		while not 0 < y < Partie.dimensionsMers.getY() + 1:
			try:
				posXY(1, 44 - r)
				print("                                                                                         ")
				posXY(1, 44 - r)
				y = int(input("  La LIGNE de votre impact = "))
			except:
				print("\nvous avez fait une erreur, veillez recommencer")
				input()

		while not 0 < z < Partie.dimensionsMers.getZ() + 1:
			try:
				posXY(1, 45 - r)
				print("                                                                                         ")
				posXY(1, 45 - r)
				z = int(input("  La PROFONDEUR de votre impact = "))
			except:
				print("\nvous avez fait une erreur, veillez recommencer")

		return x, y, z

	def sauvegarder(self):
		absolute_path = os.path.dirname(__file__)
		file = open(absolute_path + "/saves/" + self.__id, "w")
		data = {"tour": self.tour, "joueurs": {}}

		for i in range(2):
			sousMarins = {}
			impacts = []
			for impact in self.__joueurs[i].getMer().getImpacts():
				impacts.append(str(impact))
			for sousMarin in self.__joueurs[i].getMer().getSousMarins():
				coords = {}
				for coord in sousMarin.getCoords():
					coords[str(coord)] = sousMarin.getCoords()[coord]
				sousMarins["sousMarin_" + str(sousMarin)] = coords
			data["joueurs"]["joueur_" + str(i)] = {"nom": self.__joueurs[i].getNom(),
												   "couleur": self.__joueurs[i].getCouleur(),
												   "sousMarins": sousMarins,
												   "impacts": impacts}
		yaml.dump(data, file)

	def charger(self, fichier):
		absolute_path = os.path.dirname(__file__)
		file = open(absolute_path + "/saves/" + fichier, "r")
		data = yaml.load(file, yaml.Loader)

		self.tour = data["tour"]
		i = 0
		for valeursJoueur in data["joueurs"].values():
			joueur = Joueur(valeursJoueur["nom"])
			joueur.setCouleur(valeursJoueur["couleur"])
			for valeursImpact in valeursJoueur["impacts"]:
				coord = Coordonnee(0, 0, 0)
				coord.setWithString(valeursImpact)
				joueur.getMer().addImpact(coord)
			for sousMarinCoords in valeursJoueur["sousMarins"].values():
				sousMarin = SousMarin(len(sousMarinCoords.values()))
				for valeursSousMarin in sousMarinCoords.keys():
					coord = Coordonnee(0, 0, 0)
					coord.setWithString(valeursSousMarin)
					sousMarin.getCoords()[coord] = sousMarinCoords[valeursSousMarin]
				joueur.getMer().ajouterSousMarin(sousMarin)
			self.__joueurs[i] = joueur
			i += 1

		print(data)
		self.lancementPartie()

	def phraseEnY46(self,phrase):
		try:
			posXY(1, 46)
			print("                                                                                                                                                                                ")
			posXY(1, 46)
			reponse = input(phrase).lower()
		except:
			print("vous avez fait une erreur, veillez recommencer")
		return reponse