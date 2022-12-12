import tkinter
from Coordonnee import Coordonnee
from Direction import Direction

COLOR_BLEU = "#8BD3E6"
COLOR_GRIS = "#cccccc"
COLOR_GRIS_FONCE = "#202020"
COLOR_VERT = "#89E894"
COLOR_ROUGE = "#ffadad"
COLOR_VIOLET = "#bdb2ff"


class FenetreJoueur:

	def __init__(self, joueur, adversaire):
		self.__joueur = joueur
		self.__adversaire = adversaire
		self.__buttons = []
		self.__sousMarinButtons = []
		self.__pret = False

		self.__fenetre = tkinter.Tk()
		self.__fenetre.title("Bataille navale - " + joueur.getNom())
		self.__fenetre.geometry("1280x720")
		self.__fenetre.resizable(width=False, height=False)

		self.__preparationFrame = tkinter.Frame(self.__fenetre)
		self.__jeuFrame = tkinter.Frame(self.__fenetre)

		self.__labelAction = tkinter.Label(self.__fenetre, text="Sélectionner vos sous-marins et placez les sur le plateau.")
		self.__labelErreur = tkinter.Label(self.__fenetre, foreground="red")

		self.__merFramePreparation = tkinter.Frame(self.__preparationFrame)
		self.__merFrameJeu = tkinter.Frame(self.__jeuFrame)
		self.__nameLabel = tkinter.Entry(self.__preparationFrame, width=20)
		self.__nameLabel.insert(0, joueur.getNom())
		self.__readyButton = tkinter.Button(self.__preparationFrame, text="PRET", width=20, height=2, relief="flat", bg=COLOR_VERT, command=self.interactionPret)
		self.__sousMarinFrame = tkinter.Frame(self.__preparationFrame)

		self.__selectedSousMarin = None
		#self.getButtonFromCoordonnee(Coordonnee(5, 4, 3)).config(bg=COLOR_ROUGE)

		self.affichePreparation()

	def mainloop(self):
		self.__fenetre.mainloop()

	def affichePreparation(self):
		self.__labelAction.pack(anchor="center", expand=1)
		self.__labelErreur.pack(anchor="center", expand=1)
		self.__preparationFrame.pack(anchor="center", expand=1)
		frameProfondeurs = tkinter.Frame(self.__preparationFrame)
		for i in range(3):
			labelProfondeur = tkinter.Label(frameProfondeurs, text="Profondeur : " + str((i+1)*100) + "m")
			labelProfondeur.pack(side="left", expand=1)
		frameProfondeurs.grid(row=0, column=0, columnspan=2, sticky="nsew")
		self.__merFramePreparation.grid(row=1, column=0, columnspan=2, sticky="nsew")
		self.__nameLabel.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
		self.__readyButton.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
		self.__sousMarinFrame.grid(row=2, column=0, rowspan=2, sticky="nsew")

		for i in range(len(self.__joueur.getMer().getSousMarins())):
			sousMarin = self.__joueur.getMer().getSousMarins()[i]
			sousMarinButton = tkinter.Button(self.__sousMarinFrame, text="sousMarin [" + str(sousMarin.getTaille()) + "] - " + "Non placé", relief="flat", command= lambda idx=i: self.selectionneSousMarin(idx), bg=COLOR_GRIS)
			self.__sousMarinButtons.append(sousMarinButton)
			sousMarinButton.pack(fill="both", pady=1, padx=10)

		self.createButtonsPreparation()

	def afficheJeu(self):
		self.__preparationFrame.destroy()
		self.__jeuFrame.pack(anchor="center", expand=1)
		self.createButtonsJeu()
		frameProfondeurs = tkinter.Frame(self.__jeuFrame)
		for i in range(3):
			labelProfondeur = tkinter.Label(frameProfondeurs, text="Profondeur : " + str((i + 1) * 100) + "m")
			labelProfondeur.pack(side="left", expand=1)
		frameProfondeurs.grid(row=0, column=0, columnspan=2, sticky="nsew")
		self.__merFrameJeu.grid(row=1, column=0, columnspan=2, sticky="nsew")
		labelPV = tkinter.Label(self.__jeuFrame, text="Points de vie : " + str(self.__joueur.getPV()) + "/" + str(self.__joueur.getMaxPV()))
		labelPV.grid(row=2, column=0)

	def selectionneSousMarin(self, index):
		for button in self.__sousMarinButtons:
			button.config(bg="#cccccc")
		self.__selectedSousMarin = self.__joueur.getMer().getSousMarins()[index]
		self.__sousMarinButtons[index].config(bg=COLOR_BLEU)

	def interactionCasePreparation(self, coordonnee):
		if self.__selectedSousMarin is None:
			self.__labelErreur.config(text="[!] Vous devez sélectionner un sous-marin !")
			return
		try:
			self.__selectedSousMarin.placer(coordonnee, Direction.DROITE)
			self.recolorPreparation()
			self.__labelErreur.config(text="")
			indexSousMarin = self.__joueur.getMer().getSousMarins().index(self.__selectedSousMarin)
			self.__sousMarinButtons[indexSousMarin].config(text="sousMarin [" + str(self.__selectedSousMarin.getTaille()) + "] - " + "Placé")
		except Exception as e:
			self.__labelErreur.config(text="[!] " + str(e))

	def interactionCaseJeu(self, coordonnee):
		self.__adversaire.getMer().impact(coordonnee)
		self.recolorJeu()

	def interactionPret(self):
		for sousMarin in self.__joueur.getMer().getSousMarins():
			if len(sousMarin.getCoords()) < 1:
				self.__labelErreur.config(text="[!] Vous devez placer tous vos sous-marins !")
				return
		if not self.__pret:
			self.__pret = True
			self.__readyButton.config(bg=COLOR_GRIS)
		else:
			self.__pret = False
			self.__readyButton.config(bg=COLOR_VERT)

	def createButtonsPreparation(self):
		for z in range(3):
			frame = tkinter.Frame(self.__merFramePreparation)
			frame.grid(row=0, column=z, padx=10, pady=10, sticky="nsew")
			for y in range(5):
				for x in range(10):
					button = tkinter.Button(frame, text="", width=4, height=2, relief="flat", bg=COLOR_GRIS, command= lambda coord=Coordonnee(x+1, y+1, z+1): self.interactionCasePreparation(coord))
					button.grid(row=y, column=x, padx=1, pady=1)
					self.__buttons.append(button)

	def createButtonsJeu(self):
		self.__buttons.clear()
		for z in range(3):
			frame = tkinter.Frame(self.__merFrameJeu)
			frame.grid(row=0, column=z, padx=10, pady=10, sticky="nsew")
			for y in range(5):
				for x in range(10):
					button = tkinter.Button(frame, text="", width=4, height=2, relief="flat", bg=COLOR_GRIS, command= lambda coord=Coordonnee(x+1, y+1, z+1): self.interactionCaseJeu(coord))
					button.grid(row=y, column=x, padx=1, pady=1)
					self.__buttons.append(button)

	def recolorPreparation(self):
		for button in self.__buttons:
			button.config(bg=COLOR_GRIS)
		for sousMarin in self.__joueur.getMer().getSousMarins():
			for coord in sousMarin.getCoords():
				self.getButtonFromCoordonnee(coord).config(bg=COLOR_GRIS_FONCE)

	def recolorJeu(self):
		for impact in self.__adversaire.getMer().getImpacts():
			self.getButtonFromCoordonnee(impact).config(bg=COLOR_BLEU)
		for sousMarin in self.__adversaire.getMer().getSousMarins():
			for coord in sousMarin.getCoords():
				if sousMarin.getCoords()[coord] == 't':
					self.getButtonFromCoordonnee(coord).config(bg=COLOR_ROUGE)
				elif sousMarin.getCoords()[coord] == 'c':
					self.getButtonFromCoordonnee(coord).config(bg=COLOR_VIOLET)
				elif sousMarin.getCoords()[coord] == 'v':
					self.getButtonFromCoordonnee(coord).config(bg=COLOR_VERT)

	def getButtonFromCoordonnee(self, coordonnee):
		mer = self.__joueur.getMer()
		return self.__buttons[coordonnee.getX()-1+mer.getDimentionX()*(coordonnee.getY()-1)+mer.getDimentionX()*mer.getDimentionY()*(coordonnee.getZ()-1)]

	def estPret(self):
		return self.__pret

	def getFenetre(self):
		return self.__fenetre