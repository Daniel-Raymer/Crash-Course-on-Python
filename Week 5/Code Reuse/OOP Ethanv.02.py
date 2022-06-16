
class Human:
    gender = ""
    orientation = ""
    height = 0
    def __init__(self, name):
        self.name = name
    def introduce_myself(self):
        print("Hi my name is {name}, I am {gender}, {height}cm tall and i'm a huge {orientation}".format(
            name=self.name, gender=self.gender, height=self.height, orientation=self.orientation))
        
class Faggot(Human):
    gender = "Male"
    orientation = "FAGGOT"
    
    
manlet_faggot = Faggot("Ethan")
manlet_faggot.height = 90
manlet_faggot.introduce_myself()