num = int(input("enter a number"))

if num % 2 == 0:
    if num % 5 == 0:
        print(num, "is divisible by 2 and 5")
    else:
        print(num, "is divisible by 2 but not by 5")
elif num % 5 == 0:
        print(num, "is divible by 5 but not 2")
else:
     print(num, "is not divisible by 2 and 5")
