'''
Name:Abhijith S
Project: Name : string concactenation
Date: 08.10.2024
Version: 1.0
'''


first_name=input("Eneter your first name : ")
last_name=input("Enter your last name : ")
name=first_name + " " + last_name
leng= len(last_name)
print(leng)
ext_last_name=name[:leng-2]
print(ext_last_name)
