class Point :

    def __init__ (self, x, y):
        self.horizontale = x
        self.verticale = y

    def afficherLesPoints (self):
        print ("coordonnées : ", self.horizontale, self.verticale)

    def afficherX (self):
        print ("x = ", self.horizontale)

    def afficherY (self):
        print ("y = ", self.verticale)    

    def setchangerX (self, xvalue):
        self.horizontale = xvalue

    def getchangerX(self):
        return  self.horizontale 
    
    def setchangerY (self, yvalue):
        self.verticale = yvalue
    
    def getchangerY (self):
        return self.verticale
    
test = Point (5,7)

test.afficherLesPoints()
test.afficherX()
test.afficherY()
test.setchangerX(56)
test.getchangerX()
test.afficherLesPoints()