class CompteBancaire :

    __decouvert = False

    def __init__ (self,num_compte, nom, prenom, solde):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde

    def setdecouvert (self):
        self.__decouvert = True
        
    def afficher (self):
        print (f"Compte Numéro : {self.__num_compte} / Proprietaire : {self.__nom} , {self.__prenom}")

    def afficherSolde (self):
        print (f"Solde du compte n°{self.__num_compte} : {self.__solde} euros")

    def versement (self, addmonnaie):
        self.__solde = self.__solde + addmonnaie
        self.afficherSolde()
        self.setagios()
        return self.__solde
    
    def retrait(self, retmonnaie):
        self.__solde = self.__solde - retmonnaie
        if self.__solde < 0 and not self.__decouvert :
            print("ERREUR : Solde insuffisant")
        else :
            self.afficherSolde()
            self.setagios()
            return self.__solde
    
    def setagios (self):
        if self.__solde < 0:
            print ("Attention ce compte est a découvert des agios sont appliquées")
            return True
        else :
            return False
    
    def virement(self, compte_cible, montant):
            if montant <= 0:
                print("ERREUR : Montant de virement invalide")
                return

            if compte_cible == self.__num_compte:
                print("ERREUR : Le compte source et le compte cible ne peuvent pas être les mêmes.")
                return

            if self.__solde < montant:
                print("ERREUR : Solde insuffisant pour effectuer le virement")
                return

            # Retrait du montant du compte source
            self.__solde = self.__solde - montant
            print(f"Virement du compte n° {self.__num_compte} vers le compte n° {compte_cible.__num_compte} d'un montant de {montant} euros effectué avec succès.")
            self.afficherSolde()

            # Ajout du montant au compte cible
            compte_cible.versement(montant)

jason = CompteBancaire(1234, "Jason", "Tatum", 5000)
magic= CompteBancaire(5678, "Magic", "Johnson", -500)

jason.afficher()
jason.afficherSolde()
jason.setdecouvert()
jason.versement(2500)
jason.retrait(1000)

magic.afficher()
magic.afficherSolde()


jason.virement(magic, 10000)
jason.virement(magic, 500)

