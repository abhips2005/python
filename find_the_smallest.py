'''
Name:Abhijith S
Project: To find the smallest number
Date: 15.10.2024
Version: 1.0
'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1<num2 and num1<num3:
    print(f"Nuber {num1} is the smallest")
elif num2<num1 and num2<num3:
    print(f"Number {num2} is the smallest")
else:
    print(f"Number {num3} is the smallest")