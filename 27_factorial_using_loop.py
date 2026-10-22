num = int(input("enter any number: "))
fact = 1
if num < 0:
    print("cannot find factorial of negative number...")
elif num == 0 and num == 1:
    print("factorial of given number is 1...")
else:
    for i in range(2, num + 1):
        fact *= i
    print("factorial :", fact)