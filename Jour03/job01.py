class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def afficher_population(self):
        print(f"Population de la ville de {self.__nom} : {self.__nombre_habitants} habitants") 
    
    def afficher_newpopulation (self):
        print (f"Mise a jour de la population de la ville de {self.__nom} : {self.__nombre_habitants} habitants")

class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville
    
    def ajouter_population(self):
    # Accéder à la ville de la personne et augmenter sa population
        self.ville._Ville__nombre_habitants += 1


# Création des objets Ville
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Affichage de la population des villes
paris.afficher_population()
marseille.afficher_population()

# Création des personnes
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Ajout de population avec la méthode ajouter_population
john.ajouter_population()
myrtille.ajouter_population()
chloe.ajouter_population()

# Affichage de la nouvelle population des villes
paris.afficher_newpopulation()
marseille.afficher_newpopulation()