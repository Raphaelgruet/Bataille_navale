import tkinter

from Partie import Partie

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
		self.__fenetre.title("Bataille navale")
		self.__fenetre.geometry("600x600")
		self.__fenetre.resizable(width=False, height=False)
		self.__frame = tkinter.Frame(self.__fenetre)
		self.__frame.columnconfigure(0, weight=1)
		self.__buttonNouvSolo = tkinter.Button(self.__frame, text="Nouvelle partie SOLO", width=20, height=2, relief="flat", bg=COLOR_VERT, command=self.lancementPartieSolo)
		self.__buttonNouvDuo = tkinter.Button(self.__frame, text="Nouvelle partie DUO", width=20, height=2, relief="flat", bg=COLOR_VERT, command=self.lancementPartieSolo)
		self.__buttonCharger = tkinter.Button(self.__frame, text="Charger une partie", width=20, height=2, relief="flat", bg=COLOR_VERT, command=self.lancementPartieSolo)
		self.__buttonCredit = tkinter.Button(self.__frame, text="CREDIT", width=20, height=2, relief="flat", bg=COLOR_BLEU, command=self.credit)
		self.__buttonQuitter = tkinter.Button(self.__frame, text="QUITTER", width=20, height=2, relief="flat", bg=COLOR_ROUGE, command=self.quitter)
		self.afficher()
		self.update()

	def afficher(self):
		#self.__frame.config(bg=COLOR_VIOLET)
		self.__frame.pack(fill="x", anchor="center", expand=True)
		self.__buttonNouvSolo.grid(row=0, column=0, pady=5, padx=10, sticky="nsew")
		self.__buttonNouvDuo.grid(row=1, column=0, pady=5, padx=10, sticky="nsew")
		self.__buttonCharger.grid(row=2, column=0, pady=5, padx=10, sticky="nsew")
		self.__buttonCredit.grid(row=3, column=0, pady=5, padx=10, sticky="nsew")
		self.__buttonQuitter.grid(row=4, column=0, pady=5, padx=10, sticky="nsew")

	def update(self):
		while self.__ouverte:
			self.__fenetre.update()

	def lancementPartieSolo(self):
		self.__ouverte = False
		self.__fenetre.destroy()
		partie = Partie()
		partie.lancementGraphique()

	def quitter(self):
		self.__ouverte = False
		self.__fenetre.destroy()

	def credit(self):
		pass
