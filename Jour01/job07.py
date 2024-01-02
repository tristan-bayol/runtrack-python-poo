class Personnage :

    def __init__ (self):
        self.x = 0
        self.y = 0
    
    def setgauche (self):
        self.x = self.x -1

    def getgauche(self):
        return  self.x     
    
    def setdroite (self):
        self.x = self.x +1

    def getdroite(self):
        return  self.x    

    def setbas (self):
        self.y = self.y -1

    def getbas(self):
        return  self.y     
    
    def sethaut (self):
        self.y = self.y +1

    def gethaut(self):
        return  self.y    

    def position (self):
        print (f'({self.x},{self.y})')


personnage = Personnage ()

personnage.position()
personnage.setgauche()
personnage.getgauche()
personnage.position()
personnage.sethaut()
personnage.gethaut()
personnage.position()
personnage.setgauche()
personnage.getgauche()
personnage.position()
