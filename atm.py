"""
Write a program that simulates an ATM Machine, the operation of the
program should be as follows:
    
Upon running the program, it should ask the user to choose from the
operations below:

i.Check Account Balance($2 fee) 
ii.Make a withdrawal($10 fee) 
iii.Check banking statement($4 fee) 
iv.Make a transfer to local bank($4 fee) 
v. Make a transfer to international banks($8 fee).international currencie
supported are Euros, Pounds and Australian Dollars. Check current
conversion rates online. Don't forget that base currency is in USD. 
vi. Book a flight Ticket($20 for flights $100(Economy) and $35 fee for flights
above $250(first class), $50 fee for $500(executive))
vii. Register for BVN(free)
viii. Buy Airtime(glo, MTN, Airtel, Etisalat) free for any amount
ix. Buy Data(Ntel, Spectranet, Smile, Swift) use standard rates of MTN
data bundles and its free for all networks
Initial balance = $2500
"""

class ATM_Operations:

    def __init__(self):
        self.statement = []
        self.balance = 2500

    def check_balance(self):
        self.balance -= 2
        #===================
        operation = "Check Balance"
        fee = 2
        new_balance = self.balance
        self.statement.append([operation,fee,new_balance])
        #====================
        return self.balance

    def make_withdrawal(self,amount):
        fee = 10
        if amount + fee > self.balance:
            print("Insufficient Fund")

        else:
            print("Withrawal Successful")
            self.balance -= amount + fee
            
            operation = "Cash Withrawal"
            fee = 10
            new_balance = self.balance
            self.statement.append([operation,fee,new_balance])
        
    def check_banking_statement(self):
        fee = 4
        if fee > self.balance:
            print("Insufficient Fund")

        else:
            if len(self.statement) == 0:
                print("No records available")
            else:
                fee = 4
                self.balance -= fee
                operation = "Check Banking Statement"
                new_balance = self.balance
                self.statement.append([operation,fee,new_balance])
                
                print("Your Banking Statement Is as Below\n")
                print(f"{"Operation":<30}{"Fee":<5}{"New Balance":<12}")
                for record in self.statement:
                    print(f"{record[0]:<30}{record[1]:<5}{record[2]:<12}")
                print()

    def local_transfer(self,amount,account_number,bank_name):
        fee = 4
        if fee + amount > self.balance:
            print("Insufficient Fund")

        else:
            print("Transfer Successful")
            
            self.balance -= fee + amount
            operation = f"Loc_Trans_{account_number}_{bank_name}"
            new_balance = self.balance
            self.statement.append([operation,fee,new_balance])

    def international_transfer(self,amount,country,bank_name,acc_num):
        fee = 8
        usd_to_euro = 0.9
        usd_to_pounds = 0.76
        usd_to_aud = 1.46
        total_amount = 0
        
        if country == "Europe":
            total_amount = fee + (amount * usd_to_euro)

        elif country == "GBP":
            total_amount = fee + (amount * usd_to_pounds)

        elif country == "AUD":
            total_amount = fee + (amount * usd_to_aud)
        
        if fee + total_amount > self.balance:
            print("Insufficient Fund")

        else:
            print("Transfer Successful")
            
            self.balance -= fee + total_amount
            operation = f"Int_Trans_{acc_num}_{bank_name}"
            new_balance = self.balance
            self.statement.append([operation,fee,new_balance])
        
        
    def book_flight(self,destination,location,tariff):
        amount = 0
        if tariff == 1:
            amount = 120

        elif tariff == 2:
            amount =285

        elif tariff == 3:
            amount = 550

        if amount > self.balance:
            print("Insufficient Fund")

        else:
            print("Transaction Successful")
            
            self.balance -= amount
            operation = f"Flight_tkt_{location[:4]}_{destination[:4]}"
            new_balance = self.balance
            self.statement.append([operation,fee,new_balance])
        
print("Welcome to awa ATM")
print("Insert your card")
input("Enter your pin\t")
atm = ATM_Operations()

while True:
    print("\nChoose any Option of your choice\n")
    print("1. Check Balance")
    print("2. Make Withdawals")
    print("3. Check Banking Statement")
    print("4. Local Transfer")
    print("5. International Transfer")
    print("6. Book a flight")
    print("7. Quit\n")
    option = int(input("Enter the number corresponding to your option\t"))

    if option == 1:
        atm.check_balance()

    elif option == 2:
        amount = float(input("Enter Amount to withdraw\t"))
        atm.make_withdrawal(amount)
        
    elif option == 3:
        atm.check_banking_statement()

    elif option == 4:
        bank_name = input("Enter Recipient's Bank Name\t")
        account_number = input("Enter Recipient's Account Number\t")
        amount = float(input("Enter Amount to Transfer\t"))
        atm.local_transfer(amount,account_number,bank_name)
        
    elif option == 5:
        
        print("1. Euro")
        print("2. Pounds")
        print("3. Australian Dollars")
        curr = input("Select Destination Currency")
        while curr not in ["1","2","3"]:
            print("Invalid Input")
            print("1. Euro")
            print("2. Pounds")
            print("3. Australian Dollars")
            curr = int(input("Select Destination Currency"))

        bank_name = input("Enter Recipient's Bank Name\t")
        acc_num = input("Enter Recipient's Account Number\t")
        amount = float(input("Enter Amount to Transfer\t"))
        
        atm.international_transfer(amount,curr,bank_name,acc_num)
    elif option == 6:
        #break
    else:
        print("Invalid Input")

                















