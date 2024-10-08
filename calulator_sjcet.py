'''
Name:Abhijith S
Project: Basic calculator
Date: 08.10.2024
Version: 1.0
'''
print("Welcome to calculator")
num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))
sum=num1+num2
sub=num2-num1
mul=num1*num2
div=num1/num2
mod=num1%num2
result = (num1 + num2) * (num3 / 2)

print(f"The sum of num1 and num2 is: {sum}")
print(f"The difference when num2 is subtracted from num1 is: {sub}")
print(f"The product of num1 and num2 is: {mul}")
print(f"The quotient when num1 is divided by num2 is: {div}")
print(f"The remainder when num1 is divided by num2 is: {mod}")
print(f"The result of (num1 + num2) * num3 / 2 is: {result}")