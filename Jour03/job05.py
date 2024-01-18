class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = int(vie)

class Ennemie:
    def __init__(self, nom, vie):
        self.enemie = nom
        self.enemie_hp = int(vie)

class Jeu:
    niveau = 0

    @classmethod
    def choisir_Niveau(cls):
        cls.niveau = input("\n1: Facile\n2: Difficile\nDans quelle difficulté souhaitez-vous jouer ? ")

    def lancerJeu(self):
        Jeu.choisir_Niveau()
        if Jeu.niveau == "1":
            Player1 = Personnage("Hero", 20)
            Player2 = Ennemie("Alien", 10)

        elif Jeu.niveau == "2":
            Player1 = Personnage("Hero", 20)
            Player2 = Ennemie("Alien", 20)

        print(f"Personnage = {Player1.nom}, Vie = {Player1.vie}")
        print(f"Ennemie = {Player2.enemie}, Vie = {Player2.enemie_hp}")

# Créer une instance de la classe Jeu
game = Jeu()
# Lancer le jeu
game.lancerJeu()


