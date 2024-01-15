class Rectangle :
    def __init__ (self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre (self):
        perimetre = (self.__longueur + self.__largeur) * 2
        print (perimetre)

    def surface (self):
        surface = self.__longueur * self.__largeur
        print (surface)

    def getlongueur (self):
        return self.__longueur

    def setlongueur (self, newL):
        self.__longueur = newL

    def getlargeur (self):
        return self.__largeur
    
    def setlargeur (self, newl):
        self.__largeur = newl

class Parallelepipede (Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        # super().__init__(longueur, largeur) SUPER est une fonction python pour récupérer les attributs de la class parent
        Rectangle.__init__(self, longueur, largeur)
        self.hauteur = hauteur

    def volume (self):
        #Ici on utilise les get car les attributs __longueur et __largeur sont privés
        volume = self.getlongueur() * self.getlargeur() * self.hauteur
        print (volume)


forme = Parallelepipede (10, 5, 2)
 
forme.perimetre()
forme.surface()
forme.volume()
