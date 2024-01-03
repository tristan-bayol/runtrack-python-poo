class Student :

    __credits = 0

    def __init__(self, nom, prenom, num_etudiants):
        self.__name = nom
        self.__firstname = prenom
        self.__student_number = num_etudiants

    def get_name (self):
        return self.__name
    
    def get_firstname (self):
        return self.__firstname
    
    def get_students_number (self):
        return self.__student_number
    
    def add_creddits (self, value):
        if value > 0:
            Student.__credits = Student.__credits + value
            return Student.__credits
        else :
            print("Veuillez saisir une valeur supérieur a 0")

    def __studentEval (self):
        if Student.__credits >= 90:
            return 4
        elif Student.__credits < 90 and Student.__credits >= 80:
            return 3
        elif Student.__credits < 80 and Student.__credits >= 70:
            return 2
        elif Student.__credits < 70 and Student.__credits >= 60:
            return 1
        else :
            return 0      
    
    def studentInfo (self):
        print ("Name =", self.__name)
        print ("Prénom =", self.__firstname)
        print ("id =", self.__student_number)
        __level = Student.__studentEval(self)
        if __level == 4:
            print ("Niveau = Excellent")
        elif __level == 3:
            print ("Niveau = Très Bien")
        elif __level == 2:
            print ("Niveau = Bien")
        elif __level == 1:
            print ("Niveau = Passable")
        else :
            print ("Niveau = Insuffisant")

John = Student ("John", "Doe", 145)
        

John.add_creddits(10)
John.add_creddits(40)
John.add_creddits(17)
John.studentInfo()