'''
Name : Abhijith S
Date : 03.10.2024
Project : Calculator to do basic maths operations.
Version : 1.1
Updates : Check for the option entered by the user is valid before proceeding.
          Added error message for divion by 0.
          Added more options for your to give input to choice variable.
'''

def calculator():
   print("Welcome to calculator")
   print("What operation do you want to do: \n1.Addition \n2.Substraction \n3.Multiplication \n4.Division")
   choice=input("Choose the corresponsing option: ")
   
   if choice not in ['1', '2', '3', '4','Add','Sub','Mul','Div','+','-','*','/']: #Checking user's input
        print("Choose the correct option and try again!")
        return
      
   num1=float(input("Enter the first number: "))
   num2=float(input("Enter the second number: "))
   
   if choice=='1' or choice=='Add' or choice=='+':
       print(f"Result: {num1+num2}")
   elif choice=='2' or choice=='Sub' or choice=='-':
       print(f"Result: {num1-num2}")
   elif choice=='3' or choice=='Mul' or choice=='*':
       print(f"Result: {num1*num2}" )
   elif choice=='4' or choice=='Div' or choice=='/':
      if num2 != 0:   #Checking division by 0
         print(f"Result: {num1/num2}")
      else:
       print("Division by 0 is not possible")

calculator()
              
