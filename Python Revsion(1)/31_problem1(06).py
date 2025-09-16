# 1. Write a program to find the greatest of four numbers entered by the user.
num1 = int(input("num1: "))
num2 = int(input("num2: "))
num3 = int(input("num3: "))
num4 = int(input("num4: "))
if (num1 > num2 and num1>num3 and num1>num4):
    print(num1)
elif (num2 > num1 and num2>num3 and num2>num4):
    print(num2)
elif (num3 > num2 and num3>num1 and num3>num4):
    print(num3)
if (num4 > num2 and num4>num3 and num4>num1):
    print(num4)
