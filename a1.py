'''
    For my assignment I decided to create a simple bank that asks the user if they want to take out a loan or if they
    want to withdraw money from their account. I first ask the user their name and age so I know who the person is. I
    then ask them if they want to take out a loan or if they want to withdraw money from their account. If they choose
    to take out a loan, I then ask how much they want to take out and how long they will take to pay it back. I then
    calculate how much they will have to pay back every month and how much they will pay back in total. The way this
    bank works is the user will pay the original monthly amount in the first month. This is the amount of the loan
    divided by how many months the user will take to pay back the loan. However, after this they will have to pay either
    2% or 5% more every month. It will be 2% for people under the age of 18 and 5% for people 18 and older. If the user
    does not want to take out a loan and instead wants to withdraw money from their account, we will ask them how much
    money they have in their account and how much they want to withdraw. After they withdraw the money I will tell
    them how much money they have left in their account. If a user wants to withdraw more money than they have in their
    account, I will not allow them do this.
'''

def calculate_amount(interest, months, amount): #This function calculates the monthly and total amount a user will have to pay back
    monthly_amount = amount/months #In the first month the user will have to pay whatever amount/months equals to
    total = monthly_amount
    monthly_amount = round(monthly_amount, 2) #In this case the round function rounds the number to the nearest 2 decimals
    print("In month 1 you will have to pay $" + str(monthly_amount))
    for index in range(2, months+1, 1): #This loop starts at 2, goes up until months+1 and increments by 1 each time
        monthly_amount *= interest #This line calculates how much the user has to pay each month
        monthly_amount = round(monthly_amount, 2)
        print("In month "+str(index)+" you will have to pay $"+str(monthly_amount))
        total += monthly_amount #This keeps on adding the monthly_amount to the total until the loop ends
    return round(total, 2) #This returns the value of total, so it can be used in other parts of the program

def withdraw_amount(account_money, withdraw_money): #This function calculates how much money the user will have after they withdraw money
    if withdraw_money > account_money: #This will run if the user is asking to withdraw more money than they have in their account
        print("Sorry you don't have enough money to withdraw")
        exit() #This will exit the program and the program will stop running
    else: #This will run if the user is asking to withdraw money that they have in their account
        account_money -= withdraw_money #This subtracts the user's total money in their account by the money they withdraw
    return round(account_money, 2)

if __name__ == "__main__": #This is the main block of code in my program
    loan = False
    withdraw = False
    name = input("What is your name? ")
    age = int(input("Hi "+name+" How old are you? "))
    decision = input("Do you want to take out a loan or withdraw money (type loan or withdraw)? ")
    decision = decision.lower() #This line takes whatever the user enters and turns it into lowercase letters
    if decision == "loan": #This will run if the user enters loan
        loan = True
    elif decision == "withdraw": #This will run if the user enters withdraw
        withdraw = True
    else: #This will run if the user doesn't enter loan or withdraw
        print("If you don't want a loan or to withdraw money, then why are you here")
        exit()
    if loan: #This will run if loan is equal to True
        amount = float(input("How much money do you want to take out? "))
        months = int(input("How many months do you want to take to pay back the loan? "))
        if age >= 18: #This will run if the user is 18 or older
            print("The total amount of money you will have to pay back is $"+str(calculate_amount(1.05, months, amount)))
            #The line above calls the function and will print the sentence along with whatever calculate_amount returns
        else: #This will run if the user is younger than 18
            print("The total amount of money you will have to pay back is $"+str(calculate_amount(1.02, months, amount)))
    elif withdraw: #This will run if withdraw is equal to True
        account_money = float(input("How much money do you have in your account? "))
        withdraw_money = float(input("How much money do you want to withdraw from your account? "))
        print("You know have $"+str(withdraw_amount(account_money, withdraw_money))+" left in your account")
        # The line above calls the function and will print the sentence along with whatever withdraw_amount returns