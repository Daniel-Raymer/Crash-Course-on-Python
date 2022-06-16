def factorial(n):
    result = 1
    for i in range(n):
        result += i*result
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120