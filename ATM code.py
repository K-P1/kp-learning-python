"""
Write a program that simulates an ATM Machine, the operation of the program should be as
follows:
Upon running the program, it should ask the user to choose from the operations below:
	i.	Check Account Balance($2 fee) 
	ii.	Make a withdrawal($10 fee) 
	iii.	Check banking statement($4 fee) 
	iv.	Make a transfer to local bank($4 fee) 
	v. Make a transfer to international banks($8 fee).international currencies
	supported are Euros, Pounds and Australian Dollars. Check current conversion
	rates online. Don't forget that base currency is in USD. 
        vi. Book a flight Ticket($20 for flights below $100 and $35 fee for flights
        above $100)
        vii. Register for BVN(free)
        viii. Buy Airtime(glo, MTN, Airtel, Etisalat) free for any amount
        ix. Buy Data(Ntel, Spectranet, Smile, Swift) use standard rates of MTN data
        bundles and its free for all networks
Initial balance = $2500
"""
"""
#psuedo code
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
#used in 1&7
from datetime import datetime
from datetime import date
from datetime import time
import random
#assign variables
#base currency is USD"$"
start_balance= 2500
balance=start_balance
user_atm_pin=0000
#welcome page
print("*"*25,"WELCOME TO KP BANK","*"*25)
print("Please insert your card and enter your pin")
print("\n")
while True:
    print("\n")
    entered_pin=int(input("Enter Your Pin:\t"))
    if entered_pin == user_atm_pin:
        print("Correct pin")
        print("Choose your transaction\n")
        print("S/N\tOPTIONS\t\t\t\tFEES\t")
        print("1.  Check balance               \t-> $2")
        print("2.  Withdrawal                  \t-> $10")
        print("3.  Bank statement              \t-> $4")
        print("4.  Local transfers             \t-> $4")
        print("5.  International transfers     \t-> $8")
        print("6.  Book flight:less than $100  \t-> $20")
        print("                above $100      \t-> $35")
        print("7.  Register for BVN            \t-> $0")
        print("8.  Buy airtime                 \t-> $0")
        print("9.  Buy data                    \t-> $0")
        print("10. Quit")
        option=int(input("Select an option 1-10:\t"))
        #the following will be splited into 10 parts numbered 1-10
        #1
        if option == 1:
            #transaction slip
            print("1 for slip, 2 for no slip")
            slip=int(input("Do you want a slip for this inquiry?\t"))
            if slip == 1:
                print("your balance as at \"",date.today(),"\" is ","$",balance,sep="")
                print("Here is your slip! Thanks for using KP bank")
                balance=balance-2
            elif slip == 2:
                print("your balance as at \"",date.today(),"\" is ","$",balance,sep="")
                balance=balance-2
            else:
                print("invalid option, start again and select a valid option")
                print("Thanks for using KP bank")
        #2        
        elif option == 2:
            print("Select your account type")
            print("1. Savings")
            print("2. Current")
            print("3. Credit")
            opt=int(input("Enter your account type\t"))
            if opt<4:
                amount=int(input("Enter amount:\t"))
                if amount>0:
                    if amount<=balance:
                        balance=balance-amount
                        print("Collect your cash! Thanks for using KP bank")
                        balance=balance-10
                    else:
                        print("Insufficient funds")
                else:
                    print("Invalid amount, Try again")
            else:
                print("Invalid selection, try again")
                print("Thanks for using KP bank")
                
        #3
        elif option == 3:
            print("Select your account type")
            print("1. Savings")
            print("2. Current")
            print("3. Credit")
            opt=int(input("Enter your account type\t"))
            if opt<4:
                print("Here your bank statement")
                print("Thanks for using KP bank")
                balance=balance-4
            else:
                print("Invalid selection, try again")
                print("Thanks for using KP bank")
        #4        
        elif option == 4:
            print("Select your account type")
            print("1. Savings")
            print("2. Current")
            print("3. Credit")
            opt=int(input("Enter your account type\t"))
            if opt<4:
                acct_no=int(input("Enter destination account number:\t"))
                amount=float(input("Enter amount you want to send:\t"))
                if acct_no > 0 and amount > 0:
                    if amount<=balance:
                        balance=balance-amount
                        print("Transfer SUCCESFUL!!!")
                        balance=balance-4
                        print("Thanks for using KP bank")
                    else:
                        print("Insufficient funds")
                else:
                    print("Invalid account number or amount, try again")
                    print("Thanks for using KP bank")
        #5            
        elif option == 5:
            print("Only 3 international currencies are supported")
            print("1. Euro")
            print("2. Pounds Sterling")
            print("3. Australian Dollars")
            currency=int(input("Select a currency 1-3:\t"))
            if currency<4:
                #for Euro
                #$1.1 == 1euro
                if currency==1:
                    acct_no=int(input("Enter destination account number:\t"))
                    amount=float(input("Enter amount you want to send in Euro:\t"))
                    amount=amount*1.1
                    print("thats $",amount," in USD",sep="")
                    if acct_no > 0 and amount > 0:
                        if amount<=balance:
                            balance=balance-amount
                            print("Transfer SUCCESFUL!!!")
                            balance=balance-8
                            print("Thanks for using KP bank")
                        else:
                            print("Insufficient funds")
                    else:
                        print("Invalid account number or amount, try again")
                        print("Thanks for using KP bank")
                #for pounds
                #$1.28 == 1pounds
                elif currency==2:
                    acct_no=int(input("Enter destination account number:\t"))
                    amount=float(input("Enter amount you want to send in Pounds:\t"))
                    amount=amount*1.28
                    print("thats $",amount," in USD",sep="")
                    if acct_no > 0 and amount > 0:
                        if amount<=balance:
                            balance=balance-amount
                            print("Transfer SUCCESFUL!!!")
                            balance=balance-8
                            print("Thanks for using KP bank")
                        else:
                            print("Insufficient funds")
                    else:
                        print("Invalid account number or amount, try again")
                        print("Thanks for using KP bank")
                #for AUD
                #$0.68 == 1AUD
                elif currency==3:
                    acct_no=int(input("Enter destination account number:\t"))
                    amount=float(input("Enter amount you want to send in AUD:\t"))
                    amount=amount*0.68
                    print("thats $",amount," in USD",sep="")
                    if acct_no > 0 and amount > 0:
                        if amount<=balance:
                            balance=balance-amount
                            print("Transfer SUCCESFUL!!!")
                            balance=balance-8
                            print("Thanks for using KP bank")
                        else:
                            print("Insufficient funds")
                    else:
                        print("Invalid selection, try again")
                        print("Thanks for using KP bank")
                        option=int(input("Select an option 1-10\t"))
            else:
                print("Invalid account number or amount, try again")
                print("Thanks for using KP bank")
                     
                
        #6        
        elif option == 6:
            price_of_flight=float(input("enter price of flight:\t"))
            if price_of_flight<=100:
                if price_of_flight<=balance:
                    print("Your flight has been booked successfully")
                    print("Vist your airways website for more info")
                    balance=balance-price_of_flight
                    balance=balance-20
                else:
                    print("Insufficient funds")
            elif price_of_flight>100:
                if price_of_flight<=balance:
                    print("Your flight has been booked successfully")
                    print("Vist your airways website for more info")
                    balance=balance-price_of_flight
                    balance=balance-35
            else:
                print("Invalid selection, try again")
                print("Thanks for using KP bank")
                
        #7        
        elif option == 7:
            print("WELCOME TO BVN REG PAGE")
            print("Do you want to generate your BVN now")
            print("1. yes\t\t2. no")
            ans=int(input("pick an option 1-2:\t"))
            if ans == 1:
                print("This is your new BVN number:")
                #this is used to generate a random 11 digit BVN 
                print(random.randint(10000000000,100000000000))
            elif ans == 2:
                print("Thanks for using KP bank")
                break
            else:
                print("Invalid selection, try again")
                print("Thanks for using KP bank")
                
        #8    
        elif option == 8:
            print("SELECT YOUR NETWORK")
            print("1. GLO   \t\t2. MTN")
            print("3. AIRTEL\t\t4. 9MOBILE")
            network=int(input("select an option 1-4:\t"))
            if network<5:
                amount=float(input("Enter amount of airtime you want to buy:\t"))
                if amount<=balance:
                    print("Airtime purchase succesful!")
                    balance=balance-amount
                else:
                    print("Insufecient funds")
            else:
                print("Invalid selection, try again")
                print("Thanks for using KP bank")
        #9        
        elif option == 9:
            print("SELECT YOUR NETWORK")
            print("1. NTEL \t\t2. SPECTRANET")
            print("3. SMILE\t\t4. SWIFT")
            network=int(input("select an option 1-4:\t"))
            if network<5:
                #MTN data plan was used the naira prices has been converted to USD
                print("1. 30mb  -->$0.28\t\t2. 100mb -->$0.55")
                print("3. 750mb -->$1.38\t\t4. 1.5gb -->$2.76")
                print("5. 3.5gb -->$5.52\t\t6. 10gb  -->$13.81")
                print("7. 22gb  -->$27.61")
                plan=int(input("select a data plan\t"))
                if plan==1:
                    if 0.28<=balance:
                        print("Data purchase successful")
                    else:
                        print("Insufecient funds")
                elif plan==2:
                    if 0.55<=balance:
                            print("Data purchase successful")
                    else:
                        print("Insufecient funds")
                elif plan==3:
                    if 1.38<=balance:
                            print("Data purchase successful")
                    else:
                        print("Insufecient funds")             
                elif plan==4:
                    if 2.76<=balance:
                            print("Data purchase successful")
                    else:
                        print("Insufecient funds")
                elif plan==5:
                    if 5.52<=balance:
                            print("Data purchase successful")
                    else:
                        print("Insufecient funds")
                elif plan==6:
                    if 13.81<=balance:
                            print("Data purchase successful")
                    else:
                        print("Insufecient funds")
                elif plan==7:
                    if 27.61<=balance:
                            print("Data purchase successful")
                    else:
                        print("Insufecient funds")
                
                else:
                    print("Invalid selection, try again")
                    print("Thanks for using KP bank")
        #any invalid option will auto break the loop
        else:
            break
    else:
        print("incorrect pin, try again")
        

    
