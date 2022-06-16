
student = ("Dan", 21,  "male")

print(student.count("male"))
print(student.index("male"))

for x in student:
    print(x)
    
if "Dan" in student:
    print("Dan is here!")