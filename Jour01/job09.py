class Produit:

    tva = 1.196

    def __init__(self, nom, prixHT):
        self.name = nom
        self.prixHT = prixHT

    def calcul (self):
        print ("Le prix TTC de",self.name, "est de",self.prixHT * Produit.tva)
    
    def setname (self, newname):
        self.name = newname

    def setprice (self, value):
        self.prixHT = value



    
ordinateur = Produit("Ordi", 2500)
ecran = Produit ("TV", 750)

ordinateur.calcul()
ecran.calcul()

ordinateur.setname("PC")
ordinateur.setprice(1500)
ordinateur.calcul()
