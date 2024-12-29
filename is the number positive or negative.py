
print("Is Number Positive Or Negative Game!!!?")

a = int(input("enter any number: "))

if a %2 == 0:
    print("the number is even")
else:
    print("the number is odd")

b = input("Do you want again? press \'y\' if you want press any character yo exit5: ")
while b.lower() == "y" :
    a = int(input("enter any number: "))
    if a % 2 == 0:
        print("the number is even")
    elif a % 2 == 1:
        print("the number is odd")
    b = input("Do you want again? press \'y\' if you want: ")