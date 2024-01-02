class Personne :
    def __init__(self, nom, prenom):
        self.name = nom
        self.firstname = prenom
    
    def SePresenter (self):
        print ("Je suis", self.name, self.firstname)


personne1 = Personne ("Aicha", "Ouattara")
personne2 = Personne ("Tristan", "Bayol")

personne1.SePresenter()
personne2.SePresenter()