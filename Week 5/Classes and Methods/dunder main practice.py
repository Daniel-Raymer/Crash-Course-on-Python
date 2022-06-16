class MyClass:
    def __init__(self, para):
        """constructor initialised for self"""
        self.para = para
        
    def __str__(self):
        """returns object as str when called without method"""
        return "{}".format(self.para)
    
    def __main
    
myobject = MyClass("object1")

print(myobject)