class Rectangle :

    def __init__ (self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longeur (self):
        return self.__longueur
    
    def set_longueur (self, longueur):
        self.__longueur = longueur
    
    def get_largeur (self):
        return self.__largeur
    
    def set_largeur (self, largeur):
        self.__largeur = largeur

    def valeursrectangles (self):
        print (self.__longueur, self.__largeur)

rectangle = Rectangle(10, 5)
rectangle.valeursrectangles()

rectangle.set_largeur(25)
rectangle.valeursrectangles()

