class Animal :
    
    age = 0

    def __init__ (self):
        self.name = ""
    
    def vieillir (self):
        new_age = Animal.age + 1
        print ("L'age de l'animale ", new_age," ans")
    
    def nommer (self, newname):
        self.name = newname
        print ("L'animal se nomme ", newname)

panda = Animal()

print("L'age de l'animale ", panda.age," ans")
panda.vieillir()
panda.nommer("Luna")