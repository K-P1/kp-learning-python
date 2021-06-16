"""Write a program that simulates an ATM Machine, the operation of the program should be as follows:
Upon running the program, it should ask the user to choose from the operations below:
	i.	Check Account Balance($2 fee) 
	ii.	Make a withdrawal($10 fee) 
	iii.	Check banking statement($4 fee) 
	iv.	Make a transfer to local bank($4 fee) 
	v. Make a transfer to international banks($8 fee).international currencies supported are Euros, Pounds and Australian Dollars. Check current conversion rates online. Don't forget that base currency is in USD. 
  vi. Book a flight Ticket($20 for flights below $100 and $35 fee for flights above $100)
  vii. Register for BVN(free)
  viii. Buy Airtime(glo, MTN, Airtel, Etisalat) free for any amount
   ix. Buy Data(Ntel, Spectranet, Smile, Swift) use standard rates of MTN data bundles and its free for all networks

Initial balance = $2500"""

#psuedo code
"""
1- Start
2- Import datetime and random
3- Assign all starting variables
4- Create the welcome page
5- Set an infinite loop
6- Collect input "pin" from user
7- If the pin correspond with the one the system has proceed
   else give an error message
8- Print out all transaction that can be performed by the atm, and index them, eg:
    1=Check balance
    2=Withdrawal
    3=Bank statement
    4=Local transfers
    5=International transfers
    6=Book flight
    7=Register for BVN
    8=Buy airtime
    9=Buy data
    10=Quit
9- Tell the user to select an option
10- If user select 1:
     -ask if they would like a slip for the transaction
     -display date and current balance
     -give slip if it was requested
     -deduct the fee for checking balance
11- If user select 2:
     -ask for account type
     -ask for withdrawal amount
     -if the user has the amount allow the withdrawal
      else print insufficient funds
     -deduct the withdrawn amount from the user balance
12- If the user select 3:
     -ask for account type
     -print statement
     -deduct funds for viewing statement
13- If the user select 4:
     -ask for account type
     -collect account number
     -collect amount
     -confirm if the user has the amount he/she is trying to send
     -if yes deduct the amount from balance
      else give error message
14- If the user select 5:
     -ask for currency type
     -inform of the 3 currency permitted
     -collect account number
     -collect amount
     -convert amount to USD
     -print the USD equivalent
     -if the user has the amount allow the transaction
      else give error message
     -deduct the sent money from the balance
15- If the user select 6:
     -collect price of flight
     -if price is less than or equal to $100
      duduct from balance
      deduct 20 from balance
     -if price is more than 100
      duduct from balance
      deduct 35 from balance
16- If the user select 7:
     -ask if they want BVN generated now!
     -if yes generate a random 11 digit number
     -if no "break"
17- If the user select 8:
     -ask user to select network
     -collect amount to be recharged
     -if the user has the amount deduct it from balance
      else give error message
18- If the user select 9:
     -ask user to select network
     -create data plans and assign price in USD
     -tell user to select a plan
     -if the user has enough money to buy the plan allow the transaction
      else give error message
     -duduct the data price from the balance
19- If the user select 10:
     -break
20- Stop/End
"""

from datetime import datetime
from datetime import date
from datetime import time
import random
print("*"*40+"WELCOME TO GBENGZ BANK"+"*"*40)
pin=2002
inserted_pin=int(input("enter your pin: "))
if inserted_pin==pin:
    print("welcome mr whoever\nplease chose from the following options")
    print("1.\tCheck Account Balance($2 fee)\n2.\tMake a withdrawal($10 fee)\n3.\tCheck banking statement($4 fee)\n4.\tMake a transfer to local bank($4 fee)\n5.\tMake a transfer to international banks($8 fee)\n6.\tBook a flight Ticket\n7.\tRegister for BVN(free)\n8.\tBuy Airtime\n9.\tBuy Data")
    initial_balance=2500
    option=int(input("enter a number between 1-10: "))
    if option==1:
        print("do you want a receipt for this transaction?\n1.yes\n2.no")
        receipt=int(input(":"))
        if receipt==1:
            print(f"your balance as at {date.today()} is:${initial_balance-2}\nTAKE YOUR RECEIPT....THANKS FOR CHOOSING GBENGZ BANK")
        elif receipt==2:
            print(f"your balance as at is:${initial_balance-2}\nTHANKS FOR CHOOSING GBENGZ BANK....")
        else:
            print("invalid option try again")


    elif option==2:
        print("do you want a receipt for this transaction?\n1.yes\n2.no")
        answer=int(input(":"))
        if answer==1:
            print("ok")
            amount=float(input("enter an amount to withdraw: "))
            print(f"your balance is:${(initial_balance-amount)-10}\nTAKE YOUR RECEIPT....THANKS FOR CHOOSING GBENGZ BANK")
        elif answer==2:
            print("ok")
            amount=float(input("enter an amount to withdraw: "))
            print(f"your balance is:${(initial_balance-amount)-10}THANKS FOR CHOOSING GBENGZ BANK....")
        else:
            print("invalid option try again")


    elif option==3:
        print("i dont know what the heck a bank statement is")


    elif option==4:
        print("WELCOME TO THE LOCAL TRANSFER")
        print("do you want a receipt for this transaction?\n1.yes\n2.no")
        answer=int(input(":"))
        if answer==1:
            print("ok")
            acct_no=int(input("enter destination acct_no: "))
            amount=float(input("enter amount you want to transfer: "))
            print("TRANSFER SUCCESSFUL!!!")
            print(f"your balance as at {date.today()} is:${(initial_balance-amount)-4}\nTAKE YOUR RECEIPT....THANKS FOR CHOOSING GBENGZ BANK")
        
        elif answer==2:
            print("ok")
            acct_no=("enter destination acct_no: ")
            amount=float(input("enter an amount to transfer: "))
            print("TRANSFER SUCCESSFUL!!!")
            print(f"your balance as at {date.today()} is:${(initial_balance-amount)-4}THANKS FOR CHOOSING GBENGZ BANK....")
        
        else:
            print("invalid option try again")

    elif option==5:
        print("WELCOME TO THE INTERNATIONAL TRANSFER")
        print("only three currencies are supported")
        print("1.\tEuro\n2.\tPounds Sterling\n3.\tAustrilian Dollar")
        currency=float(input("select a currency(1-3): "))
        if currency<4:
            if currency==1:
                acct_no=int(input("Enter destination account number:\t"))
                amount=float(input("Enter amount you want to send in Euro:\t"))
                amount=amount*1.1
                print("thats $",amount," in USD",sep="")
                if acct_no > 0 and amount > 0:
                    if amount<=initial_balance:
                        print("TRANSFER SUCCESSFUL!!!")
                        print(f"balance as at {date.today()} is {(initial_balance-amount)-8}\nTHANKS FOR CHOOSING GBENGZ BANK")
                    else:
                        print("INSUFFICIENT FUNDS")
                else:
                    print("invalid account number try again\nTHANKS FOR CHOOSING GBENGZ BANK")
                            
            elif currency==2:
                acct_no=int(input("Enter destination account number:\t"))
                amount=float(input("Enter amount you want to send in Pounds:\t"))
                amount=amount*1.28
                print("thats $",amount," in USD",sep="")
                if acct_no > 0 and amount > 0:
                    if amount<=initial_balance:
                        print("Transfer SUCCESFUL!!!")
                        print(f"balance as at {date.today()} is {(initial_balance-amount)-8}\nTHANKS FOR CHOOSING GBENGZ BANK")        
                           
                    else:
                        print("INSUFFICIENT FUNDS")
                else:
                    print("invalid account number try again\nTHANKS FOR CHOOSING GBENGZ BANK")
                
                        
               
            elif currency==3:
                acct_no=int(input("Enter destination account number:\t"))
                amount=float(input("Enter amount you want to send in AUD:\t"))
                amount=amount*0.68
                print("thats $",amount," in USD",sep="")
                if acct_no > 0 and amount > 0:
                    if amount<=initial_balance:
                        print("Transfer SUCCESFUL!!!")
                        print(f"balance as at {date.today()} is {(initial_balance-amount)-8}\nTHANKS FOR CHOOSING GBENGZ BANK")
                            
                    else:
                        print("INSUFFICIENT FUNDS")
                else:
                    print("invalid account number try again\nTHANKS FOR CHOOSING GBENGZ BANK")

    elif option==6:
        print("YOU HAVE CHOSEN TO BOOK A FLIGHT")
        print("1.\teconomy class(below$100)\tfee is below $20\n2.\tbusiness class(between $100 and $300)\tfee is below $20 and $35\n3.\tfirst class(above $500)\tabove $100")
        print("choose one from above")
        flight=int(input(":"))
        if flight <=3:
            if flight==1:
                amount=float(input("enter the amount(below $100): "))
                if amount<=initial_balance:
                    print("YOU HAVE SUCCESSFULLY BOOKED AN ECONOMY CLASS")
                    print(f"your balance as at {date.today()} is:${(initial_balance-amount)-20}\nTHANKS FOR CHOOSING GBENGZ BANK....")
                else:
                    print("INSUFFICIENT FUNDS")

            elif flight==2:
                amount=float(input("enter the amount(between $100 and $300): "))
                if amount<=initial_balance:
                    print("YOU HAVE SUCCESSFULLY BOOKED A BUSINESS CLASS")
                    print(f"your balance as at {date.today()} is:${(initial_balance-amount)-35}\nTHANKS FOR CHOOSING GBENGZ BANK....")
                else:
                    print("INSUFFICIENT FUNDS")

            elif flight==3:
                amount=float(input("enter the amount(above $500): "))
                if amount<=initial_balance:
                    print("YOU HAVE SUCCESSFULLY BOOKED A FIRST CLASS")
                    print(f"your balance as at {date.today()} is:${(initial_balance-amount)-100}\nTHANKS FOR CHOOSING GBENGZ BANK....")
                else:
                    print("INSUFFICIENT FUNDS")

    elif option==7:
        name=input("Enter your name: ")
        age=int(input("Enter your age: "))
        address=input("Enter your home address: ")
        country=input("Enter your nationality: ")
        if age>=18:
            print("you are eligible to have a BVN")
            print("would you like to process your BVN?\n1.\tyes\n2.\tno")
            number=int(":")
            if number==1:
                print("Hold on your BVN is processing........")
                BVN=random.randint(10000000000,100000000000)
                print(f" your BVN is {BVN})
            if number==2:
                      print("BVN will not be processed\nTHANKS FOR CHOOSING GBENGZ BANK")
                      
                      

    elif option==8:
        print("select the airtime you want to buy: ")
        print("1.\tairtel/n2.\tMTN\n3.\tGLO\n4.\tEtisalat")
        number=int(input(":"))
        if number==1:
            phone_no=int(input("enter your phone number: "))
            amount=float(input("enter amount: "))
            if amount<initial_balance:
                print("RECHARGE SUCCESSFUL")
                print("airtel....the smartphone network")
                print("THANKS FOR CHOOSING GBENGZ BANK")
            else:
                print("INSUFFICIENT FUNDS")
        elif number==2:
            phone_no=int(input("enter your phone number: "))
            amount=float(input("enter amount: "))
            if amount<initial_balance:
                print("RECHARGE SUCCESSFUL")
                print("MTN.....everywhere you go")
                print("THANKS FOR CHOOSING GBENGZ BANK")
            else:
                print("INSUFFICIENT FUNDS")
        elif number==3:
            phone_no=int(input("enter your phone number: "))
            amount=float(input("enter amount: "))
            if amount<initial_balance:
                print("RECHARGE SUCCESSFUL")
                print("glo....the smartphone the grandmasters of data")
                print("THANKS FOR CHOOSING GBENGZ BANK")
            else:
                print("INSUFFICIENT FUNDS")
        elif number==4:
            phone_no=int(input("enter your phone number: "))
            amount=float(input("enter amount: "))
            if amount<initial_balance:
                print("RECHARGE SUCCESSFUL")
                print("THANKS FOR CHOOSING GBENGZ BANK")
            else:
                print("INSUFFICIENT FUNDS")

    elif option==9:
        print("select your ethernet: ")
        print("1.\tNtel\n2.\tspectranet3.\tsmile\n4.swift")
        number=int(input(":"))
        if number==1:
            print("select bundle: \n1.\t$100-75mb\n2.\t$200-200mb\n3.\t$500-750mb\n4.\t$1000-1.5gb")
            bundle=int(input(":"))
            if bundle==1:
                print("this will cost you $100\n1.\tcontinue\n2.\tcancel")
                proceed=int(input(":"))
                if proceed==1:
                    print("your subscription of 75mb is succesful")
                if proceed==2:
                    print("subsricption is cancelled")
            if bundle==2:
                print("this will cost you $200\n1.\tcontinue\n2.\tcancel")
                proceed=int(input(":"))
                if proceed==1:
                    print("your subscription of 200mb is succesful")
                if proceed==2:
                    print("subsricption is cancelled")
            if bundle==3:
                print("this will cost you $500\n1.\tcontinue\n2.\tcancel")
                proceed=int(input(":"))
                if proceed==1:
                    print("your subscription of 750mb is succesful")
                if proceed==2:
                    print("subsricption is cancelled")
            if bundle==4:
                print("this will cost you $1000\n1.\tcontinue\n2.\tcancel")
                proceed=int(input(":"))
                if proceed==1:
                    print("your subscription of 1.5gb is succesful")
                if proceed==2:
                    print("subsricption is cancelled")
        if number==2:
            print("select bundle: \n1.\t$100-75mb\n2.\t$200-200mb\n3.\t$500-750mb\n4.\t$1000-1.5gb")
            bundle=int(input(":"))
            if bundle==1:
                print("this will cost you $100\n1.\tcontinue\n2.\tcancel")
                proceed=int(input(":"))
                if proceed==1:
                    print("your subscription of 75mb is succesful")
                if proceed==2:
                    print("subsricption is cancelled")
            if bundle==2:
                print("this will cost you $200\n1.\tcontinue\n2.\tcancel")
                proceed=int(input(":"))
                if proceed==1:
                    print("your subscription of 200mb is succesful")
                if proceed==2:
                    print("subsricption is cancelled")
            if bundle==3:
                print("this will cost you $500\n1.\tcontinue\n2.\tcancel")
                proceed=int(input(":"))
                if proceed==1:
                    print("your subscription of 750mb is succesful")
                if proceed==2:
                    print("subsricption is cancelled")
            if bundle==4:
                print("this will cost you $1000\n1.\tcontinue\n2.\tcancel")
                proceed=int(input(":"))
                if proceed==1:
                    print("your subscription of 1.5gb is succesful")
                if proceed==2:
                    print("subsricption is cancelled")
        if number==3:
            print("select bundle: \n1.\t$100-75mb\n2.\t$200-200mb\n3.\t$500-750mb\n4.\t$1000-1.5gb")
            bundle=int(input(":"))
            if bundle==1:
                print("this will cost you $100\n1.\tcontinue\n2.\tcancel")
                proceed=int(input(":"))
                if proceed==1:
                    print("your subscription of 75mb is succesful")
                if proceed==2:
                    print("subsricption is cancelled")
            if bundle==2:
                print("this will cost you $200\n1.\tcontinue\n2.\tcancel")
                proceed=int(input(":"))
                if proceed==1:
                    print("your subscription of 200mb is succesful")
                if proceed==2:
                    print("subsricption is cancelled")
            if bundle==3:
                print("this will cost you $500\n1.\tcontinue\n2.\tcancel")
                proceed=int(input(":"))
                if proceed==1:
                    print("your subscription of 750mb is succesful")
                if proceed==2:
                    print("subsricption is cancelled")
            if bundle==4:
                print("this will cost you $1000\n1.\tcontinue\n2.\tcancel")
                proceed=int(input(":"))
                if proceed==1:
                    print("your subscription of 1.5gb is succesful")
                if proceed==2:
                    print("subsricption is cancelled")
        if number==1:
            print("select bundle: \n1.\t$100-75mb\n2.\t$200-200mb\n3.\t$500-750mb\n4.\t$1000-1.5gb")
            bundle=int(input(":"))
            if bundle==1:
                print("this will cost you $100\n1.\tcontinue\n2.\tcancel")
                proceed=int(input(":"))
                if proceed==1:
                    print("your subscription of 75mb is succesful")
                if proceed==2:
                    print("subsricption is cancelled")
            if bundle==2:
                print("this will cost you $200\n1.\tcontinue\n2.\tcancel")
                proceed=int(input(":"))
                if proceed==1:
                    print("your subscription of 200mb is succesful")
                if proceed==2:
                    print("subsricption is cancelled")
            if bundle==3:
                print("this will cost you $500\n1.\tcontinue\n2.\tcancel")
                proceed=int(input(":"))
                if proceed==1:
                    print("your subscription of 750mb is succesful")
                if proceed==2:
                    print("subsricption is cancelled")
            if bundle==4:
                print("this will cost you $1000\n1.\tcontinue\n2.\tcancel")
                proceed=int(input(":"))
                if proceed==1:
                    print("your subscription of 1.5gb is succesful")
                if proceed==2:
                    print("subsricption is cancelled")
else:
    print("wrong pin")
