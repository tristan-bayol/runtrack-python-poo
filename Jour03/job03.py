class Tache: 
    def __init__ (self, titre, description):
        self.titre = titre
        self.desc = description
        self.statut = False

    def endtask (self):
        self.statut = True

    def infostask(self):
        return "Tâche à faire" if not self.statut else "Tâche terminée"

    # retourne une chaîne de caractères représentant les informations sur la tâche initié dans le constructeur
    def __str__(self):
        return f"Tâche: {self.titre}\nDescription: {self.desc}\nStatut: {self.infostask()}"

# class ListDeTache :
            
manger = Tache("manger", "je dois manger")
print (manger)
manger.endtask()
print (manger)