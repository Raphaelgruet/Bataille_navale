import os
import tkinter
from Partie import Partie
from PIL import Image, ImageTk

COLOR_BLEU = "#8BD3E6"
COLOR_GRIS = "#cccccc"
COLOR_GRIS_FONCE = "#202020"
COLOR_VERT = "#89E894"
COLOR_ROUGE = "#ffadad"
COLOR_VIOLET = "#bdb2ff"

class FenetrePrincipal:

	def __init__(self):
		self.__ouverte = True
		self.__fenetre = tkinter.Tk()
		self.__fenetre.protocol("WM_DELETE_WINDOW", self.quitter)
		self.__fenetre.title("Bataille navale")
		self.__fenetre.geometry("600x600")
		self.__fenetre.resizable(width=False, height=False)
		self.__frame = tkinter.Frame(self.__fenetre)
		self.__frame.columnconfigure(0, weight=1)
		self.__buttonNouvSolo = tkinter.Button(self.__frame, text="Nouvelle partie SOLO", width=20, height=2, relief="flat", bg=COLOR_VERT, command=self.lancementPartieSolo)
		self.__buttonNouvDuo = tkinter.Button(self.__frame, text="Nouvelle partie DUO", width=20, height=2, relief="flat", bg=COLOR_VERT, command=self.lancementPartieSolo)
		self.__buttonCharger = tkinter.Button(self.__frame, text="Charger une partie", width=20, height=2, relief="flat", bg=COLOR_VERT, command=self.menuChargement)
		self.__buttonCredit = tkinter.Button(self.__frame, text="CREDIT", width=20, height=2, relief="flat", bg=COLOR_BLEU, command=self.credit)
		self.__buttonQuitter = tkinter.Button(self.__frame, text="QUITTER", width=20, height=2, relief="flat", bg=COLOR_ROUGE, command=self.quitter)
		self.__buttonRetour = tkinter.Button(self.__frame, text="RETOUR", width=20, height=2, relief="flat", bg=COLOR_GRIS, command=self.afficher)
		self.__buttonNouvSolo.grid(row=0, column=0, pady=5, padx=10, sticky="nsew")
		self.__buttonNouvDuo.grid(row=1, column=0, pady=5, padx=10, sticky="nsew")
		self.__buttonCharger.grid(row=2, column=0, pady=5, padx=10, sticky="nsew")
		self.__buttonCredit.grid(row=3, column=0, pady=5, padx=10, sticky="nsew")
		self.__buttonQuitter.grid(row=4, column=0, pady=5, padx=10, sticky="nsew")
		self.__frame.pack(fill="x", anchor="center", expand=True)
		image = Image.open("res/submarines.png")
		imageResized = image.resize((600,300), Image.ANTIALIAS)
		imagetk = ImageTk.PhotoImage(imageResized)
		self.__imageLabel = tkinter.Label(self.__fenetre, image=imagetk)
		self.__imageLabel.config()
		self.afficher()
		self.update()

	def clearWindow(self):
		for widget in self.__fenetre.winfo_children():
			widget.pack_forget()

	def afficher(self):
		#self.__frame.config(bg=COLOR_VIOLET)
		self.clearWindow()

		self.__imageLabel.pack()
		self.__frame.pack(fill="x", anchor="center", expand=True)

	def menuChargement(self):
		self.clearWindow()
		self.__imageLabel.pack()
		frameChargement = tkinter.Frame(self.__fenetre)
		frameChargement.columnconfigure(0, weight=1)
		frameChargement.pack(fill="x", anchor="center", expand=True)

		self.__saveList = tkinter.Listbox(frameChargement, selectmode="single")
		for file in os.listdir("saves/"):
			self.__saveList.insert("end", file.title())
		self.__saveList.grid(row=0, column=0, pady=5, padx=10, rowspan=4, sticky="nsew")

		button_chargement = tkinter.Button(frameChargement, text="CHARGER", width=20, height=2, relief="flat", bg=COLOR_VERT, command=self.charger)
		button_chargement.grid(row=4, column=0, pady=5, padx=10, sticky="nsew")
		buttonRetour = tkinter.Button(frameChargement, text="RETOUR", width=20, height=2, relief="flat", bg=COLOR_GRIS, command=self.afficher)
		buttonRetour.grid(row=5, column=0, pady=5, padx=10, sticky="nsew")

	def update(self):
		while self.__ouverte:
			self.__fenetre.update()

	def charger(self):
		if len(self.__saveList.curselection()) > 0:
			sauvegardeName = self.__saveList.get(self.__saveList.curselection()[0])
			self.quitter()
			partie = Partie()
			partie.charger(sauvegardeName)

	def lancementPartieSolo(self):
		self.quitter()
		partie = Partie()
		partie.preparationGraphique()

	def quitter(self):
		self.__ouverte = False
		self.__fenetre.destroy()

	def credit(self):
		pass
