#original version

languages_orig = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages_orig]

print(lengths)

#list comprehension version

languages_comp = len(["Python", "Perl", "Ruby", "Go", "Java", "C"])
print(languages_comp)

z = [x for x in range(0,101) if x % 3 == 0]
print(z)