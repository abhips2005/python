'''
Name : Abhijith S
Date : 01.10.2024
Project : Number converter from integer to  Binary, Octal and Hexadecimal
Version : 1.0
'''

def number():
    number=int(input("Enter an integer number:"))
    print(f"Binary: {bin(number)}")
    print(f"Octal: {oct(number)}")
    print(f"Hexadecinaml: {hex(number)}")
number()
