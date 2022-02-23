# -*- coding: utf-8 -*-
"""Bank  Project Python Dictionaries
cust_data = {}
new_user_attributes = ['name', 'address', 'phone num', 'govt id', 'amount']

 
import random

def new_user():
  # Step 1: Create a random five-digit account number and store it in 'acc_num' variable
  acc_num =random.randint(10000,99999)    # Write your code here
  while acc_num in cust_data.keys():
    acc_num=random.randint(10000,99999)
    new_user_inputs=[]


  for i in range(len(new_user_attributes)):
    user_input = input("Enter " + new_user_attributes[i] + ":\n")
    if new_user_attributes[i] == 'amount':
      new_user_inputs.append(int(user_input))
    else:
      new_user_inputs.append(user_input)
  cust_data[acc_num] = dict(zip(new_user_attributes, new_user_inputs))

  print("Your Details are added Sucessfully")
  print("Your Account number is",acc_num)

new_user()
cust_data
def existing_user():
  acc_num = int(input("Enter Your Account Number: "))  # Write your code here
  while acc_num not in cust_data:
    acc_num = int(input("Not found. Please enter your correct account number:\n"))
    
  # Step 2: Print the welcome message to the user.
  # Write your code here
  print("Welcome, ",cust_data[acc_num]['name'],"!")
  print("Enter 1 to check your balance.\nEnter 2 to withdraw an amount.\nEnter 3 to deposit an amount.")

  # Step 3: Asking the user to select a valid choice. 
  user_choice = input()
  while user_choice not in ['1','2','3']:
    print("\nInvalid input!")
    print("Enter 1 to check your balance.\nEnter 2 to withdraw an amount.\nEnter 3 to deposit an amount.")
    user_choice = input()
  
  # Step 4:
  # If 'user_choice == 1' then display the account balance i.e. 'cust_data[acc_num]['amount']'
  if user_choice == '1':
    print("Available Balance ",cust_data[acc_num]['amount'])
    # Write your code here  
      
  # Else if 'user_choice == 2' then subtract the withdrawal amount from the available balance.
  elif user_choice == '2':
    amt = int(input("\nEnter the amount to be withdrawn:\n"))
    if amt > cust_data[acc_num]['amount']:
      print("\nInsufficient balance.\nAvailable balance:", cust_data[acc_num]['amount'])
    else:
      new_amt = int(cust_data[acc_num]['amount']) - amt
      cust_data[acc_num]['amount'] = new_amt
      print("\nWithdrawal successful.\nAvailable Balance:", cust_data[acc_num]['amount'])

  # Else if 'user_choice == 3' then add the deposit amount to the available balance.
  elif user_choice == '3':
    amt = int(input("\nEnter the amount to be deposited:\n"))
    new_amt = int(cust_data[acc_num]['amount']) + amt
    cust_data[acc_num]['amount'] = new_amt
    print("\nDeposit successful.\nAvailable Balance:", cust_data[acc_num]['amount'])

existing_user()


while True:
  valid_inputs = ['1','2','3']
  print("Welcome to the Horizon Bank!")
  print("\nEnter 1 if you are a new customer.\nEnter 2 if you are an existing customer.\nEnter 3 to terminate the application.") 

  user_choice = input()
  while user_choice not in ['1','2','3']:
    print("Invalid input!")
    print("Enter 1 if you are a new customer.\nEnter 2 if you are an existing customer.\nEnter 3 to terminate the application.\n")
    user_choice = input()

  if (user_choice=="1"):
    new_user()
    print("Thank You, for banking With Us !")
    break

  elif (user_choice=="2"):
    existing_user()
    print("Thank You, for banking With Us !")
    break

  # Else If the user enters 3, then terminate the application with the 'Thank you, for banking with us!' message. 
  elif (user_choice=="3"):
    print("Thank You, for banking With Us !")
    break
