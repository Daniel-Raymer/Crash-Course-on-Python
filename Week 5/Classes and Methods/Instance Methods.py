#class Piglet:
#    pass

#hamlet = Piglet()



#class Piglet:
#    def speak(self):
#        print("oink oink")
        
#hamlet = Piglet()
#hamlet.speak()

#class Piglet:
#    name = "piglet"
#    def speak(self):
#        print("Oink! I'm {}! Oink!".format(self.name))
        
#hamlet = Piglet()
#hamlet.name = "Hamlet"
#hamlet.speak()

#petunia = Piglet()
#petunia.name = "Petunia"
#petunia.speak()

class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18
    
piggy = Piglet()
print(piggy.pig_years())

piggy.years = 2
print(piggy.pig_years())