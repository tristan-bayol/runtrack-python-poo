class Personne :   
    def __init__(self, nom):
        self.nom = nom
        self.age = 14

    def afficherAge (self):
        print (self.age)

    def bonjour (self):
        print ("Hello")

    def modifierAge (self, new_age):
        self.age = new_age
        return self.age

class Eleve (Personne):   
    def allerEnCours (self):
        print ("Je vais en cours")

    def afficherAge (self):
        print ("J'ai", self.age, "ans")

class Professeur :
    def __init__(self,matiere):
        self.__matiereEnseignée = matiere

    def enseigner (self):
        print ("Le cours va commencer")

titou = Personne("Titou")
tristan = Eleve("Tristan")

tristan.afficherAge()