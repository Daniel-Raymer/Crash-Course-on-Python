#original version

multiples_orig = []
for x in range(1, 11):
    multiples_orig.append(x*7)
print(multiples_orig)

#list comprehension version

multiples_comp = [ x*7 for x in range(1,11) ]
print(multiples_comp)