class Voiture :
    
    def __init__ (self, marque, modèle, année, km):
        self.__marque = marque
        self.__modele = modèle
        self.__annee = année
        self.__kilometrage = km
        self.en_marche = False
        self.__reservoir = 50


    def get_marque (self):
        return self.__marque
    def set_marque (self, marque):
        self.marque = marque
    def get_modèle (self):
        return self.__modele
    def set_modele (self, modele):
        self.modele = modele
    def get_annee (self):
        return self.__annee
    def set_annee (self, année):
        self.__annee = année
    def get_km (self):
        return self.__kilometrage
    def set_km (self, km):
        self.__kilometrage = km
    def get_state (self):
        return self.en_marche

    def demmarrer (self):
        if Voiture.__verifier_plein (self) > 5:
            return self.en_marche == True
        else :
            print("Reservoir vide, veuillez faire le plein")
    
    def arreter (self):
        return self.en_marche == False
    
    def __verifier_plein (self):
        return self.__reservoir

voiture = Voiture("BMW","Serie 1", 2011, 138000)
print (voiture.get_marque())
print(voiture.get_modèle())
print(voiture.get_annee())
print(voiture.get_km())
voiture.demmarrer()
print (voiture.get_state())