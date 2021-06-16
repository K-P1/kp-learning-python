
month= int( input("Enter value for month: "))
year = int( input("Enter value for year: "))
def getYear(year):
    if year % 4 == 0 or (year % 100 !=0 and year % 400 ==0):
        return 366
    else:
        return 365
def getMonthDay(year, month):
    if month == 2:
        if year % 4 == 0 or(year % 100 !=0 and year % 400 ==0):
            return 29
        else:
            return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31

def getOffset(year, month):
    offset = 0
    for i in range(1753,year):
        offset +=  getYear(year)
        
    for i in range(1,month):

       offset += getMonthDay(year,i)
    print(offset)
    return offset % 7
         
def display(numOffset,numOfDay):
    numCount = 0
    if numOffset == 6: #the idea is that if offset is 6 then it is to be -1
        numOffset = -1
    print("Sun\tMon\tTue\tWed\tThur\tFri\tSat")
    for i in range(-numOffset,numOfDay+1,1) :
        # the negetive offset help to determine the
        #number of space before the date begin
        if i <= 0:
            print("\t", end="")
            numCount +=1
        elif i % 7 == 6:
            print(i, end = "\n")
            numCount+=1
        else:
            print(i, "\t",end ="")
            numCount +=1
print(getOffset(year, month))
display(getOffset(year, month),getMonthDay(year, month))
