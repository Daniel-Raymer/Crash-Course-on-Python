#pay attention to the variables and object inspector when running
#the debug tool on the sort() and sorted() functions, you will
#find the behaviour very interesting.

numbers = [4, 6, 2, 7, 1]
numbers.sort()
print(numbers)

names = ["Carlos", "Ray", "Alex", "Kelly"]
print(names)
print(sorted(names))
print(names)
print(sorted(names, key=len))