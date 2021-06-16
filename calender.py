numOffset = int(input("Enter value of offset "))
numDay = int(input("Enter the number of days: "))
def display(offset, numday):
    if offset == 6:
        offset = -1
    numCount = 0
    print("Sun\tMon\tTues\tWed\tThurs\tFri\tSat")
    for i in range(-offset,numday+1,1):
        if i <= 0:
            print("\t",end="")
            numCount += 1
        elif numCount % 7 == 6:
            print(i,"\t",end="\n")
            numCount += 1
        else:
            print(i,"\t",end="")
            numCount += 1
display(numOffset,numDay)
        
