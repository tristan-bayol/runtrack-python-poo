class Tache: 
    def __init__ (self, titre, description):
        self.titre = titre
        self.desc = description
        self.statut = "a faire"


class ListDeTache:
    def __init__ (self):
        self.list = []

    def add_task (self, tache):
        self.list.append (tache)
    
    def del_task (self, tache):
        self.list.remove (tache)
               
    def end_task(self, tache):
        tache.statut = "Terminer"

    def afficher_liste(self, statut=None):
        if statut is None:
            for tache in self.list:
                print(f'Titre: {tache.titre}, Description: {tache.desc}, Statut: {tache.statut}')
        else:
            filtered_list = [tache for tache in self.list if tache.statut == statut]
            for tache in filtered_list:
                print(f'Titre: {tache.titre}, Description: {tache.desc}, Statut: {tache.statut}')

manger = Tache("Manger", "Je dois manger")
sport = Tache("Faire du sport", "Faire 30 minutes d'exercice")
shopping = Tache("Faire les courses", "Acheter les articles manquants")

liste = ListDeTache()
liste.add_task(manger)
liste.add_task(sport)
liste.add_task(shopping)

# Afficher toutes les tâches
print("\nToutes les tâches:")
liste.afficher_liste()

# Marquer une tâche comme terminée
liste.end_task(manger)

# Afficher les tâches à faire
print("\nTâches à faire:")
liste.afficher_liste(statut="a faire")

# Afficher les tâches terminées
print("\nTâches terminées:")
liste.afficher_liste(statut="Terminer")