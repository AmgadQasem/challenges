n = int(input("fact number for : "))

factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(factorial)
