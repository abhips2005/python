'''
Name:Abhijith S
Project: To find the smallest number
Date: 15.10.2024
Version: 1.0
'''

btotal=0
tbh=0
gtotal=0
tgh=0
n=int(input("Enter the total number of students: "))
for x in range(1,n):
    gender=input("Enter your gender (M/F): ")
    height=int(input("Enter your height: "))
    if gender=="M":
        btotal+=1
        tbh=tbh+height
    else:
        gtotal+=1
        tgh=tgh+height
bavg=tbh/btotal
gavg=tgh/gtotal
print(f"Total number of boys: {btotal}")
print(f"Total number of girls: {gtotal}")
print(f"Average height of boys: {bavg}")
print(f"Average height of girls: {gavg}")


