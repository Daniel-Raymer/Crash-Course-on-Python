class Apple:
    def __init__(self, colour, flavour):
        self.colour = colour
        self.flavour = flavour
    def __str__(self):
        return "This apple is {} and its flavour is {}".format(self.colour, self.flavour)
    
help(Apple)