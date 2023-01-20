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
import random

# Class Partie
class Partie:
	__joueurs = [None, None]
	__id = "partie_" + datetime.now().strftime("%d-%m-%Y_%Hh%Mm%Ss")
	__temps = 0
	tour = 1
	dimensionsMers = Coordonnee(10, 5, 3)

	def __init__(self):
		pass
		self.__fenetres = []
		#self.preparationGraphique()
		#self.charger("partie_22_09_47")
		#self.lancementGraphique()

	def creationDesJoueur(self):
		# Partie test
		cls()
		Mer.affichagePlateauVide(1, 2, Back.WHITE)
		posXY(73, 28)
		print("---------- Bataille navale ----------")
		posXY(70, 29)
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
		'''cls()
		Mer.affichagePlateauVide(1, 2, Back.WHITE)
		posXY(73, 28)
		print("---------- Bataille navale ----------")
		posXY(70, 29)
		input("appuyer sur entrer pour commencer la partie ...")
		cls()
		# Creation des joueurs
		for i in range(2):
			self.__joueurs[i] = Joueur(input("Le joueur " + str(
				i + 1) + " entre son prénom :").upper())  # Creation des joueurs à partir du nom entré dans le terminal
		print("Cette bataille opposera", self.__joueurs[0].getNom(), "contre", self.__joueurs[1].getNom())
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
			self.__joueurs[1].setCouleur2(Fore.LIGHTGREEN_EX)
		print(self.__joueurs[0], "a choisi la couleur", self.__joueurs[0].getCouleur() + "   ", Style.RESET_ALL)
		print(self.__joueurs[1], "aura pour couleur", self.__joueurs[1].getCouleur() + "   ", Style.RESET_ALL)
		input()'''

	def placementSousMarins(self,NombreDeJoueur, Ia):
		for i in range(NombreDeJoueur):
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(4))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(3))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(3))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(2))
			# Attribution des positions des sous-marins du joueur
			for j in range(len(self.__joueurs[i].getMer().getSousMarins())):
				if (Ia == True and i != 1):
					cls()
					self.__joueurs[i].getMer().affichage(Back.WHITE, self.__joueurs[i].getCouleur(), True)
					# Placement des sous-marins
					print(self.__joueurs[i].getCouleur(), self.__joueurs[i], "place ses sous-marins", Style.RESET_ALL)
				placer = False
				while not placer:
					try:
						if Ia==True and i==1:
							x, y, z = random.randint(1,10), random.randint(1, 5), random.randint(1, 3)
							if 10-self.__joueurs[i].getMer().getSousMarins()[j].getTaille()<x<=10:
								if 5-self.__joueurs[i].getMer().getSousMarins()[j].getTaille()<y<=5:
									direction=random.choice([Direction.GAUCHE, Direction.HAUT])
								elif 0<y<=self.__joueurs[i].getMer().getSousMarins()[j].getTaille():
									direction=random.choice([Direction.BAS, Direction.GAUCHE])
								else:
									direction = random.choice([Direction.BAS, Direction.GAUCHE, Direction.HAUT])
							elif 0<x<=self.__joueurs[i].getMer().getSousMarins()[j].getTaille():
								if 5-self.__joueurs[i].getMer().getSousMarins()[j].getTaille()<y<=5:
									direction=random.choice([Direction.DROITE, Direction.HAUT])
								elif 0<y<=self.__joueurs[i].getMer().getSousMarins()[j].getTaille():
									direction=random.choice([Direction.BAS, Direction.DROITE])
								else:
									direction = random.choice([Direction.BAS, Direction.DROITE, Direction.HAUT])
							else:
								if 5-self.__joueurs[i].getMer().getSousMarins()[j].getTaille()<y<=5:
									direction=random.choice([Direction.GAUCHE, Direction.HAUT, Direction.DROITE])
								elif 0<y<=self.__joueurs[i].getMer().getSousMarins()[j].getTaille():
									direction=random.choice([Direction.BAS, Direction.GAUCHE, Direction.DROITE])
								else:
									direction=random.choice([Direction.BAS, Direction.GAUCHE, Direction.HAUT, Direction.DROITE])
							coord = Coordonnee(x, y, z)

						else:
							print(self.__joueurs[i].getCouleur2())
							direction=Direction.DROITE
							# direction, x, y, z = Partie.demandeEmplacement(self, j)
							coord = Coordonnee(1, j + 1, 1)
						# coord = Coordonnee(x, y, z)
						self.__joueurs[i].getMer().getSousMarins()[j].placer(coord, direction)
						placer = True
					except Exception as e:
						print(e)
				if (Ia == True and i != 1) or (Ia == False):
					if j == len(self.__joueurs[i].getMer().getSousMarins()) - 1:
						print(Style.RESET_ALL)
						self.__joueurs[i].getMer().affichage(Back.WHITE, self.__joueurs[i].getCouleur(), True)
						input()
		cls()
		posXY(1, 1)

	def preparationGraphique(self):
		# Creation des joueurs

		for i in range(2):
			self.__joueurs[i] = Joueur("Joueur " + str(i + 1))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(4))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(3))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(3))
			self.__joueurs[i].getMer().ajouterSousMarin(SousMarin(2))

		# Creation des fenêtres
		for i in range(2):
			fenetre = FenetreJoueur(self.__joueurs[i], self.__joueurs[(i + 1) % 2])
			self.__fenetres.append(fenetre)

		while self.__fenetres[0].estPret() == False or self.__fenetres[1].estPret() == False:
			self.__fenetres[0].getFenetre().update()
			self.__fenetres[1].getFenetre().update()

		self.lancementGraphique()

	def lancementGraphique(self):

		if len(self.__fenetres) < 1:
			for i in range(2):
				fenetre = FenetreJoueur(self.__joueurs[i], self.__joueurs[(i + 1) % 2])
				self.__fenetres.append(fenetre)

		for fenetre in self.__fenetres:
			fenetre.afficheJeu()

		while not self.testVictoire():
			self.__fenetres[0].setJouable(True)
			while self.__fenetres[0].estJouable():
				for fenetre in self.__fenetres:
					fenetre.getFenetre().update()
			self.sauvegarder()
			self.__fenetres[1].setJouable(True)
			while self.__fenetres[1].estJouable():
				for fenetre in self.__fenetres:
					fenetre.getFenetre().update()
			self.sauvegarder()

		gagnant = self.testVictoire()
		print("#####################################\n")
		print("  VICTOIRE de " + str(gagnant) + " !\n")
		print("#####################################")
		'''for fenetre in fenetres:
			fenetre.mainloop()'''
	def menu(self):
		n=-1
		print("choissiez votre mode:\n")
		print("1: contre Ia:\n")
		print("3: sur deux ecran:\n")
		print("2: 1VS1 sur le meme ecran\n")
		while not 0 < n < 4:
			try:
				n = int(input())
			except:
				print(" vous avez fait une erreur, veillez recommencer")
		return n
		# Placement des sous-marins

	def lancementPreparation(self):
		n = self.menu()
		if (n == 2):
			self.creationDesJoueur()
			self.placementSousMarins(2, False)
		elif (n == 1):
			self.creationDesJoueur()
			self.placementSousMarins(2, True)
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
		if(n==1):
			self.lancementPartieIa()
		elif(n==3):
			self.partirSur2Ecran()
		else:
			self.lancementPartie()

	def lancementPartieIa(self):
		# Commencement de la partie
		while True:
			i = (self.tour - 1) % 2
			j = (self.tour) % 2
			if i==0:
				self.__joueurs[j].getMer().affichage(self.__joueurs[i].getCouleur(), self.__joueurs[i].getCouleur(), False)
			# Detection coordonnées + impact
			print(self.__joueurs[j].getCouleur2())
			if (i == 1):
				x, y, z = self.demandeImpactIa(j)
			else:
				x, y, z = self.demandeImpactIa(j)
				#x, y, z = self.demandeImpact(20)
			coord = Coordonnee(x, y, z)
			self.__joueurs[j].getMer().impact(coord)
			print(Style.RESET_ALL)
			self.__joueurs[j].getMer().affichage(self.__joueurs[i].getCouleur(), self.__joueurs[i].getCouleur(), False)
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

	def partirSur2Ecran(self):

		self.creationDesJoueur()
		# Placement des sous-marin
		self.placementSousMarins(1,False)
		# qui commmence
		print("La partie commence")
		print("C'est à " + self.__joueurs[0].getNom() + " de commencer")
		input()
		cls()
		# Commencement de la partie
		while True:  # tant qu'il a des PV
			self.__joueurs[0].getMer().affichageEnSolo(self.__joueurs[0].getCouleur(), True)
			self.__joueurs[1].getMer().affichageEnSolo(self.__joueurs[1].getCouleur(), False)
			Partie.neyttoyageScript(self, 1)
			posXY(1, 41)
			emplacement = 0
			while not 0 < emplacement < 3:
				try:
					posXY(1, 41)
					print(
						"                                                                                                                        \n                                                                                                                               ")
					print("                                                           ")
					posXY(1, 41)
					emplacement = int(input(
						"1 : voulez-vous placer un pion sur votre plateau\n2 : voulez-vous placer un pion sur le plateau adverse\n"))
				except:
					print("vous avez fait une erreur, veillez recommencer")

			Partie.neyttoyageScript(self, 1)
			posXY(1, 41)
			if emplacement == 1:
				print(self.__joueurs[0].getCouleur2(), "ou votre adversaire a t-il tire?")
				x, y, z = Partie.demandeImpact(self, 0)
				print(Style.RESET_ALL)
				coord = Coordonnee(x, y, z)
				self.__joueurs[0].getMer().impact(coord)
			elif emplacement == 2:
				print(self.__joueurs[1].getCouleur2(), "ou avez vous tire?")
				# verification d'un impact unique/////////////////////////////////////a utiliser a d'autre endroitb (creer une fonction)/////////////////////////////
				impactUnique = False
				while impactUnique == False:
					x, y, z = Partie.demandeImpact(self, 0)
					coord = Coordonnee(x, y, z)
					typeImpact = ""
					while not (typeImpact == "t" or typeImpact == "c" or typeImpact == "r" or typeImpact == "v"):
						try:
							posXY(1, 41)
							print(
								"                                                                                                                                                                                                    ")
							posXY(1, 41)
							typeImpact = input(
								"Entrez le resultat de votre impact (si vous avez touche, entrer :\"t\", si vous avous avez coule, entrer :\"c\", si vous avez vous un sous marin, entrer :\"v\", si vous avous avez rien eu, entrer :\"r\"").lower()
						except:
							print("\nvous avez fait une erreur, veillez recommencer")
					j = 0
					for key in self.__joueurs[1].getMer().getImpactsType().keys():
						if key == coord:
							if self.__joueurs[1].getMer().getImpactsType()[key] != "t":
								j = j + 1
					if j == 0:
						impactUnique = True
					else:
						Partie.neyttoyageScript(self, 1)
						print("vous avez selectionne une case deja remplit, veillez recommencer")

				# demande de l'etat de ma case

				print(Style.RESET_ALL)
				self.__joueurs[1].getMer().setImpactsType(coord, typeImpact)
				print(Style.RESET_ALL)
			if self.__joueurs[0].getPV() == 0:
				print("#####################################\n")
				print("#   VICTOIRE de votre Adversaire!   #\n")
				print("#####################################")
				return True
			else:
				cls()
	def testVictoire(self):
		# Fonction qui retourne le joueur qui a gagné la partie dans le cas ou celle-ci est terminée,
		# dans le cas contraire la fonction retourne None
		for i in range(2):
			if self.__joueurs[i].getPV() == 0:
				return self.__joueurs[i]
		return None

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
				coord.setWithArray(eval(valeursImpact))
				joueur.getMer().addImpact(coord)
			for sousMarinCoords in valeursJoueur["sousMarins"].values():
				sousMarin = SousMarin(len(sousMarinCoords.values()))
				for valeursSousMarin in sousMarinCoords.keys():
					coord = Coordonnee(0, 0, 0)
					coord.setWithArray(eval(valeursSousMarin))
					sousMarin.getCoords()[coord] = sousMarinCoords[valeursSousMarin]
				joueur.getMer().ajouterSousMarin(sousMarin)
			self.__joueurs[i] = joueur
			i += 1

		print(data)
		#self.lancementPartie()
		self.lancementGraphique()

	def demandeEmplacement(self, j):
		x, y, z = -1, -1, -1
		direction = None
		posXY(1, 23)
		print("Entrez les coordonnées de votre impact " + str(j + 1) + " :")
		while not 0 < x < Partie.dimensionsMers.getX() + 1:
			try:
				posXY(1, 24)
				print("                                                                                         ")
				posXY(1, 24)
				x = int(input("  La COLONNE du debut de votre sous-marin = "))
			except:
				print("vous avez fait une erreur, veillez recommencer")

		while not 0 < y < Partie.dimensionsMers.getY() + 1:
			try:
				posXY(1, 25)
				print("                                                                                         ")
				posXY(1, 25)
				y = int(input("  La LIGNE du debut de votre sous-marin = "))
			except:
				print("vous avez fait une erreur, veillez recommencer")

		while not 0 < z < Partie.dimensionsMers.getZ() + 1:
			try:
				posXY(1, 26)
				print("                                                                                         ")
				posXY(1, 26)
				z = int(input("  La PROFONDEUR de votre sous-marin = "))
			except:
				print("vous avez fait une erreur, veillez recommencer")

		while not (
				direction == Direction.DROITE or direction == Direction.GAUCHE or direction == Direction.HAUT or direction == Direction.BAS):
			try:
				posXY(1, 27)
				print("                                                                                                   ")
				posXY(1, 27)
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

		Partie.neyttoyageScript(self, r)
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
				print("         vous avez fait une erreur, veillez recommencer")

		while not 0 < y < Partie.dimensionsMers.getY() + 1:
			try:
				posXY(1, 44 - r)
				print("                                                                                         ")
				posXY(1, 44 - r)
				y = int(input("  La LIGNE de votre impact = "))
			except:
				print("         vous avez fait une erreur, veillez recommencer")
				input()

		while not 0 < z < Partie.dimensionsMers.getZ() + 1:
			try:
				posXY(1, 45 - r)
				print("                                                                                         ")
				posXY(1, 45 - r)
				z = int(input("  La PROFONDEUR de votre impact = "))
			except:
				print("         vous avez fait une erreur, veillez recommencer")

		Partie.neyttoyageScript(self, r)
		return x, y, z


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

	def neyttoyageScript(self, positionIniciale):
		posXY(1, 42 - positionIniciale)
		print("                                                                                                                                                   ")
		print("                                                                                          ")
		print("                                                                                          ")
		print("                                                                                          ")
		print("                                                                                          ")
		print("                                                                                          ")
		posXY(1, 41 - positionIniciale)
	def posAnciennePieceIa(self,joueur):
		dodo= Coordonnee(0, 0, 0)
		for sousMarin in joueur.getMer().getSousMarins():
			for coordonne in sousMarin.getCoords().keys():
				if (joueur.getSauvegardeDerniereToucheIa() in sousMarin.getCoords()):
					if (sousMarin.getCoords()[joueur.getSauvegardeDerniereToucheIa()] == 't'):
						dodo = coordonne

					elif (sousMarin.getCoords()[joueur.getSauvegardeDerniereToucheIa()] == 'c'):
						dodo = Coordonnee(0, 0, 0)
					else:
						dodo = joueur.getSauvegardeDerniereToucheIa()
				else:
					if (joueur.getMer().getImpacts()[-1] == coordonne):
						if (sousMarin.getCoords()[coordonne] == 't'):
							return coordonne
		return dodo
	def demandeImpactIa(self,joueur):
		if (len(self.__joueurs[joueur].getMer().getImpacts()) != 0):
			self.__joueurs[joueur].setSauvegardeDerniereToucheIa(self.posAnciennePieceIa(self.__joueurs[joueur]))
			for sousMarin in self.__joueurs[joueur].getMer().getSousMarins():
				for coordonne in sousMarin.getCoords().keys():
					if sousMarin.getCoords()[coordonne] == 'v':
						return coordonne.getX(), coordonne.getY(), coordonne.getZ()
#retenu d'une coordonne touche
		if (self.__joueurs[joueur].getSauvegardeDerniereToucheIa()!=Coordonnee(0, 0, 0)):
			impactUnique = False
			caseAutourPlein=0
			while impactUnique == False:
				x, y, z = random.randint(-1,1)+self.__joueurs[joueur].getSauvegardeDerniereToucheIa().getX(), random.randint(-1,1)+self.__joueurs[joueur].getSauvegardeDerniereToucheIa().getY(), self.__joueurs[joueur].getSauvegardeDerniereToucheIa().getZ()
				if caseAutourPlein>100:
					x, y, z = random.randint(-2, 2) + self.__joueurs[joueur].getSauvegardeDerniereToucheIa().getX(), random.randint(-2,2) + self.__joueurs[joueur].getSauvegardeDerniereToucheIa().getY(), self.__joueurs[joueur].getSauvegardeDerniereToucheIa().getZ()
				if caseAutourPlein>300:
					x, y, z = random.randint(-3, 3) + self.__joueurs[joueur].getSauvegardeDerniereToucheIa().getX(), random.randint(-3,3) + self.__joueurs[joueur].getSauvegardeDerniereToucheIa().getY(),self.__joueurs[joueur].getSauvegardeDerniereToucheIa().getZ()
				if caseAutourPlein > 600:
					x, y, z = random.randint(-4, 4) + self.__joueurs[joueur].getSauvegardeDerniereToucheIa().getX(), random.randint(-4,4) + self.__joueurs[joueur].getSauvegardeDerniereToucheIa().getY(), self.__joueurs[joueur].getSauvegardeDerniereToucheIa().getZ()
				coord = Coordonnee(x, y, z)
				j = 0
				if (x<1 or x>10 ):
					j = j + 1
				elif( y<1 or y>5 ):
					j = j + 1
				if(j==0):
					for sousMarins in self.__joueurs[joueur].getMer().getSousMarins():
						for coordsousMarin in sousMarins.getCoords().keys():

							if coordsousMarin==coord:
								if  sousMarins.getCoords()[coord]!= 'o':
									if sousMarins.getCoords()[coord]!= 'v':
										j = j + 1
									else:
										j = j + 1
								elif (coordsousMarin in self.__joueurs[joueur].getMer().getImpacts()):
									j = j + 1
				caseAutourPlein+=1
				if j == 0:
					impactUnique = True
			print("coordonne final    ", x, y, z)
			print("self.__joueurs[joueur].getSauvegardeDerniereToucheIa()   ", self.__joueurs[joueur].getSauvegardeDerniereToucheIa())
			print("caseAutourPlein   ",caseAutourPlein)
			input()
			return x, y, z
		impactUnique = False
		while impactUnique == False:
			x, y, z = random.randint(1, 10), random.randint(1, 5), random.randint(1, 3)
			coord = Coordonnee(x, y, z)
			j = 0
			for key in self.__joueurs[j].getMer().getImpacts():
				if key == coord:
						j = j + 1
			if j == 0:
				impactUnique = True
		return x, y, z
