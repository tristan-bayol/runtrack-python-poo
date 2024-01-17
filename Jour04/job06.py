class Vehicule :
    def __init__(self, marque, modèle, année, prix):
        self.marque = marque
        self.modele = modèle
        self.annee = année
        self.prix = prix

    def informationsVehicule (self):
        print (f"Marque = {self.marque}\nModèle = {self.modele}\nAnnée = {self.annee}\nPrix = {self.prix} Euros")
    
    def demmarer (self) :
        print ("ATTENTION, je roule")


class Voiture (Vehicule):
    def __init__(self, marque, modèle, année, prix):
        super().__init__(marque, modèle, année, prix)
        self.portes = 4
        
    def informationsVehicule (self):
        print (f"Marque = {self.marque}\nModèle = {self.modele}\nAnnée = {self.annee}\nPrix = {self.prix} Euros \nNombre de porte = {self.portes} ")

    def demmarer (self) :
        print ("ATTENTION, je roule en VOITURE")

class Moto (Vehicule):
    def __init__(self, marque, modèle, année, prix):
        super().__init__(marque, modèle, année, prix)
        self.roues = 2
    
    def informationsVehicule(self):
        print (f"Marque = {self.marque}\nModèle = {self.modele}\nAnnée = {self.annee}\nPrix = {self.prix} Euros \nNombre de roue = {self.roues} ")

    def demmarer (self) :
        print ("ATTENTION, je roule en MOTO")

voiture = Voiture ("BMW", "120D", 2011, 15000)
voiture.informationsVehicule()
voiture.demmarer()

moto = Moto ("Yamaha", "1200 Vmax", 1987, 4500)
moto.informationsVehicule()
moto.demmarer()