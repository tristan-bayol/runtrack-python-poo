class Livre :

    __disponible = True

    def __init__ (self, titre, auteur, nbr_pages):
        self.__title = titre
        self.__autor = auteur
        self.__pages = nbr_pages

    def get_title (self): 
        return self.__title
    def set_title (self, title):
        self.__title = title

    def get_autor (self): 
        return self.__autor
    def set_autor (self, autor):
        self.__autor = autor

    def get_pages (self):
         return self.__pages
    
    def set_pages (self, pages):
        if type(pages) == int and pages >= 0:
            self.__pages= pages
        else:
            print ("Erreur, veuillez entre un nombre entier positif")

    def verification(self):
        if Livre.__disponible == True:
            return True
        else:
            return False

    def emprunter(self):
        if Livre.verification(self):
            Livre.__disponible = False
            print("Livre emprunté avec succès.")
        else:
            print("Livre non disponible.")

    def rendre(self):
        if not Livre.verification(self):
            Livre.__disponible = True
            print("Livre rendu avec succès.")
        else:
            print("Le livre est déjà disponible.")

    
livre1 = Livre ("Seven deadly Sin", "Moi", 200)
print(livre1.get_title())
print(livre1.get_autor())
print(livre1.get_pages())

livre1.emprunter()
livre1.rendre()
livre1.rendre()

