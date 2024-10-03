'''
Name : Abhijith S
Date : 02.10.2024
Project : Money management app
Version : 1.1
Updates : Feature to save user data*
          Check for null values in expense and income
'''

import os
def load_budget():
    """Loads the budget from a file if it exists, otherwise initializes it to 0."""
    if os.path.exists("budget.txt"):
        with open("budget.txt", "r") as file:
            return float(file.read())
    else:
        return 0.0

def save_budget(budget):  #Saves the current budget to a file.
    with open("budget.txt", "w") as file:
        file.write(str(budget))

def budget_app():
    budget = load_budget()  # Load the budget from file

    while True:
        print("\nSimple Budget App")
        print("1. Add income")
        print("2. Add expense")
        print("3. View balance")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            if amount>0:
               budget += amount
               print("Income added.")
            else:
                print("Income should be grater than 0.")
              
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            if amount>0:
                if amount<= budget:
                    budget -= amount
                    print("Expense added.")
                else:
                    print("Insufficient balance for this expense")
            else:
                print("Expense should be grater than 0.")
                
        elif choice == '3':
            print(f"Current balance: ${budget:.2f}")
            
        elif choice == '4':
            save_budget(budget) #save the current budget to file
            print("Budget saved. Exiting app. Goodbye!")
            break
        else:
            print("Invalid option!")

budget_app()
