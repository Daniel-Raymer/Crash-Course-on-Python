class Fruit:
    def __init__(self, colour, flavour):
        self.colour = colour
        self.flavour = flavour
        
class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")
print(granny_smith.flavour)

print(carnelian.colour)