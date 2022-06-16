class Human:
    gender = ""
    orientation = ""
    height = 0
    def __init__(self, name):
        self.name = name
    def introduce_myself(self):
        print("Hi my name is {name}, I am {gender}, {height}cm tall and i'm {orientation}".format(
            name=self.name, gender=self.gender, height=self.height, orientation=self.orientation))
        
class Faggot(Human):
    gender = "Male"
    orientation = "a huge FAGGOT"
    
class Alpha(Human):
    gender = "Male"
    orientation = "that GORILLA DICK NIGGA and I make DYKE pussy WET"
    
class Manlet_Faggot(Faggot):
    height = 90
    
best_bud1 = Manlet_Faggot("Ethan")
best_bud1.introduce_myself()

class Gorilla_Dick_Pussy_God(Alpha):
    height = 250

best_bud2 = Gorilla_Dick_Pussy_God("Tim")
best_bud2.introduce_myself()
