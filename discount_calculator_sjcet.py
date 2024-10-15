'''
Name:Abhijith S
Project: To calculate the discount based on the bill amount
Date: 15.10.2024
Version: 1.0
'''

bill=int(input("Enter your total bill amount: "))
if bill>500:
    discount=(bill/100)*20
    to_pay=bill-discount
    print(f"Total to pay after discount is Rs. {to_pay}")
elif bill>=200:
    discount = (bill / 100)*10
    to_pay = bill - discount
    print(f"Total to pay after discount is Rs. {to_pay}")
else:
    print(f"The total bill to pay is {bill}")
