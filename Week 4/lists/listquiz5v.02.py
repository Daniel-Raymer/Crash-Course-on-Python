#The guest_list function reads in a list of tuples with the name, age, and profession of each party guest,
#and prints the sentence "Guest is X years old and works as __." for each one.
#For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer"))
#should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer.
#Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that.


#ntuple stands for nested tuple
def guest_list(guests):
    for index, ntuple in enumerate(guests):
        print("{n} is {a} years old and works as {p}".format(n = ntuple[0], a = ntuple[1], p = ntuple[2]))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""