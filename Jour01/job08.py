class Cercle:

    def __init__(self, x):
        self.rayon = x

    def setrayon (self, value):
        self.rayon = value
    
    def circonference (self):
        return (self.rayon * 2) * 3.141592653589793
        # diametre x pi

    def aire (self):
        return 3.141592653589793 * (self.rayon * self.rayon)
        # pi x rayon²

    def diametre (self):
        return self.rayon * 2
    
    def affficherInfos(self):
        print ("Rayon",self.rayon)
        print ("Circonférence =",Cercle.circonference(self))
        print ("Aire=",Cercle.aire(self))
        print ("Diàmetre=",Cercle.diametre(self))
        print("")

cercle1 = Cercle(4)
cercle2 = Cercle(7)

cercle1.affficherInfos()
cercle2.affficherInfos()
cercle1.setrayon(6)
cercle1.affficherInfos()