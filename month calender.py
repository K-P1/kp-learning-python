"""#displayTable()--- to display a calender
#the function takes 2 parameters:numdays and offset
#numdays is the numbers of days in the month
#offset is the day the month starts
numdays=int(input("enter the number of days in the month\t"))
line=[]
A=[]
B=[]
C=[]
D=[]
E=[]
def displayTable(numdays):
"""
A= range(1,31+1)
B= range(1,30+1)
C= range(1,29+1)
D= range(1,28+1)

week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
numdays=0
offset=""
def displayTable(numdays,offset):
    while True:
        numdays=int(input("enter number of days in the month:\t"))
        start_day=input("enter start day of the month in lower case:\t")
        print("enter 0 as number of days to quit")
        offset=start_day.lower()
        start=week.index(offset)
        if numdays==31:
            print("M  T  W  T  F  S  S")
            print('{0:<3}'.format('')*start, end='')
            for days in A:
                print('{0:<3}'.format(days), end='')
                start+=1
                if start==7:
                    print()
                    start=0
            print("\n")
        elif numdays==30:
            print("M  T  W  T  F  S  S")
            print('{0:<3}'.format('')*start, end='')
            for days in B:
                print('{0:<3}'.format(days), end='')
                start+=1
                if start==7:
                    print()
                    start=0
            print("\n")
        elif numdays==29:
            print("M  T  W  T  F  S  S")
            print('{0:<3}'.format('')*start, end='')
            for days in C:
                print('{0:<3}'.format(days), end='')
                start+=1
                if start==7:
                    print()
                    start=0
            print("\n")
        elif numdays==28:
            print("M  T  W  T  F  S  S")
            print('{0:<3}'.format('')*start, end='')
            for days in D:
                print('{0:<3}'.format(days), end='')
                start+=1
                if start==7:
                    print()
                    start=0
            print("\n")
        elif numdays==0:
            break
        else:
            print("the number of days in month that you entered is not valid..."
                  "Please enter a valid number and try again")

displayTable(numdays,offset)
