
class SuperPowers:
    def __init__(self):
        self.my_string = ""
        self.my_list = [str()]
    def string_maker(self, string_para):
        """adds parameter to string attribute when called"""
        self.my_string = string_para
    def list_adder(self, list_para):
        """appends parameter to list"""
        self.my_list.append(list_para)
    def __str__(self):
        return "Current attributes for {x} are:\n-Strings: {y}\n-List: {z}".format(
            x=self.__repr__(), y=self.my_string, z=self.my_list)

danny = SuperPowers()
danny.string_maker("string1")
danny.list_adder(205)
danny.list_adder("heyhey")
print(danny)
danny

#Notes:
#according to https://stackoverflow.com/questions/1984162/purpose-of-repr-method
#dunder repr is used for developers wheras dunder str is used for end users?