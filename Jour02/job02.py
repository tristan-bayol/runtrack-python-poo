class Livre :

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



livre1 = Livre ("Seven deadly Sin", "Moi", 200)
print(livre1.get_title())
print(livre1.get_autor())
print(livre1.get_pages())
livre1.set_pages(2.4)
livre1.set_pages(-10)
livre1.set_pages(100)
print(livre1.get_pages())
