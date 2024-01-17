class Joueur:
    def __init__(self, nom , numéro, position, nbr_buts, nbr_passe_décisive, nbr_yellow_card, nbr_red_card):
        self.nom = nom
        self.number = numéro
        self.pos = position
        self.goal = nbr_buts
        self.assist = nbr_passe_décisive
        self.yellow = nbr_yellow_card
        self.red = nbr_red_card

    def marquerUnBut (self, nbr_buts):
        self.goal = self.goal + nbr_buts
        return self.goal
    
    def effectuerUnePasseDecisive (self, nbr_assist):
        self.assist = self.assist + nbr_assist
        return self.assist
    
    def recevoirUnCartonJaune (self, nbr_yc):
        self.yellow = self.yellow + nbr_yc
        return self.yellow
    
    def recevoirUnCartonRouge (self, nbr_rc):
        self.red = self.red + nbr_rc
        return self.red
    
    def afficherStatistiques (self):
        print (f"\nNom : {self.nom}\nNuméro : {self.number}\nPosition : {self.pos}\nButs : {self.goal}\nPasse Décisives : {self.assist}\nCarton Jaunes : {self.yellow}\nCarton Rouges : {self.red} ")
    

class Equipe:
    def __init__(self, squadname):
        self.squadname = squadname
        self.squadlist = []

    def ajouterJoueur (self, player):
        self.squadlist.append (player)

    def afficher_stats(self):
        total_buts = 0
        total_assists = 0
        total_yellow_cards = 0
        total_red_cards = 0

        for player in self.squadlist:
            total_buts += player.goal
            total_assists += player.assist
            total_yellow_cards += player.yellow
            total_red_cards += player.red
        
        #Sortir le print de la boucle for permet d'afficher une seule fois les stats global plutot que les stats à chaque joueur présents dans la squad
        print(f"\nEquipe : {self.squadname}\nButs : {total_buts}\nPasse Décisives : {total_assists}\nCarton Jaunes : {total_yellow_cards}\nCarton Rouges : {total_red_cards}")

    def mettreAJourStatistiqueJoueur(self, player):
        for joueur in self.squadlist:
            if joueur == player:
                majstats = input("\n1: But\n2: Passe Decisive\n3: Cartons Jaunes\n4: Cartons Rouges\nQuelle statistique souhaitez-vous mettre à jour ? ")

                if majstats == "1":
                    joueur.goal += int(input("Combien de buts ajouter ? "))
                elif majstats == "2":
                    joueur.assist += int(input("Combien de passes décisives ajouter ? "))
                elif majstats == "3":
                    joueur.yellow += int(input("Combien de cartons jaunes ajouter ? "))
                elif majstats == "4":
                    joueur.red += int(input("Combien de cartons rouges ajouter ? "))
                else:
                    print("ERREUR, veuillez saisir un chiffre entre 1 et 4 selon la stat que vous souhaitez modifier")
        
        # Ne pas mettre de return ici pour permettre la mise à jour de tous les joueurs de l'équipe




#Créations des Joueurs
Steven = Joueur ("Gerrard", 8,"MDC",4,3,2,1)
David = Joueur ("Beckham", 7, "MOC", 5,4,1,0)
Paolo = Joueur ("Maldini", 3, "DC", 0,1,4,2)
Pipo = Joueur ("Inzaghi", 9, "BU", 10,3,0,1)

#Créations des Equipes
England = Equipe("Angleterre")
Italie = Equipe("Italie")

#Ajout des joueurs dans les équipes
England.ajouterJoueur(Steven)
England.ajouterJoueur(David)
Italie.ajouterJoueur(Paolo)
Italie.ajouterJoueur(Pipo)

#Afficher les stats des joueurs
Steven.afficherStatistiques()
Paolo.afficherStatistiques()

#Afficher les stats des équipes
England.afficher_stats()
Italie.afficher_stats()

#Maj les stats d'un joueur
Italie.mettreAJourStatistiqueJoueur(Pipo)

#Test du programme
Pipo.afficherStatistiques()
Italie.afficher_stats()