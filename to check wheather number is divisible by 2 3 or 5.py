while 1:
    a=input("enter the number to check ")
    a=int(a)
    if a%2==0:
        print("The Number is divisible by 2")
    elif a%3==0:
        print("The Number is Divisible by 3")
    elif a%5==0:
        print("The Number is divisible by 5")
    else:
        print("The Number is not divisible by 2 3 or 5")
