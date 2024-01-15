class Forme :
    def aire (self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire (self):
        aire = self.largeur * self.hauteur
        print (aire)

forme = Rectangle (4,5)

forme.aire()