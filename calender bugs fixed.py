#step1==>start
#step2==>collect input"month and year" as integers
month=int(input("enter a month number 1-12\t"))
year=1753
#year=int(input("enter a year\t"))
#step3==>define your function
#it should collect 2 parraameter"date and year"
def cal(month,year):
    #step4==>initialize a var to rep the offset of the first month"january"
    #you can edit it to work for a year with a diffrent offset for january
    Sum=0
    #step5==>initialize var for all months, it should all contain a range with the
    #start being the negative offset and the stop being the number of days in the month
    #number of days +1 so it will include the last day
    Jan=range((Sum),31+1)
    #step6==>append the days to sum
    Sum+=Jan[-1]
    #step7==>make account for leap years
    if year%4==0:
        #this is a leap year
        Feb=range(-(Sum%7),29+1)
        Sum+=Feb[-1]
    else:
        Feb=range(-(Sum%7),28+1)
        Sum+=Feb[-1]
    Mar=range(-(Sum%7),31+1)
    Sum+=Mar[-1]
    Apr=range(-(Sum%7),30+1)
    Sum+=Apr[-1]
    May=range(-(Sum%7),31+1)
    Sum+=May[-1]
    June=range(-(Sum%7),30+1)
    Sum+=June[-1]
    July=range(-(Sum%7),31+1)
    Sum+=July[-1]
    Aug=range(-(Sum%7),31+1)
    Sum+=Aug[-1]
    Sep=range(-(Sum%7),30+1)
    Sum+=Sep[-1]
    Oct=range(-(Sum%7),31+1)
    Sum+=Oct[-1]
    Nov=range(-(Sum%7),30+1)
    Sum+=Nov[-1]
    Dec=range(-(Sum%7),31+1)
    Sum+=Dec[-1]
    #step8==>convert month from integer to its rep var
    #step9==>set a var that contains the names of each month"it will be used later"
    if month==1:
        month=Jan
        n='JANUARY'
    elif month==2:
        month=Feb
        n='FEBUARY'
    if month==3:
        month=Mar
        n='MARCH'
    if month==4:
        month=Apr
        n='APRIL'
    if month==5:
        month=May
        n='MAY'
    if month==6:
        month=June
        n='JUNE'
    if month==7:
        month=July
        n='JULY'
    if month==8:
        month=Aug
        n='AUGUST'
    if month==9:
        month=Sep
        n='SEPTEMBER'
    if month==10:
        month=Oct
        n='OCTOBER'
    if month==11:
        month=Nov
        n='NOVEMBER'
    if month==12:
        month=Dec
        n='DECEMBER'
    #step10==>print the name of the month and the year
    print(n,year)
    #step11==>format the week days"i used tabs"
    print("Su\tMo\tTu\tWe\tTh\tFr\tSa")
    #this is to format the days
    #step12==>format the days
    a=7+month[0]
    #step13==>print the days 
    for x in month:
        #for months that starts on a sunday
        if a==1:
            if x < 0:
                print("\t",end="")
            elif x == 0:
                print("\n",end="")
            elif x%7 == 0:
                print(x,"\n",end="")
            elif x>0 and x<7:
                print(x,"\t",end="")
            elif x>6 and x<13:
                print(x,"\t",end="")
            elif x>12 and x<20:
                print(x,"\t",end="")
            elif x>19 and x<27:
                print(x,"\t",end="")
            else:
                print(x,"\t",end="")
        #for others
        else:        
            if x <=0:
                print("\t",end="")
            elif x%7==(a-1) or x==(a-1):
                print(x,"\n")
            elif x>0 and x<7:
                print(x,"\t",end="")
            elif x>6 and x<13:
                print(x,"\t",end="")
            elif x>12 and x<20:
                print(x,"\t",end="")
            elif x>19 and x<27:
                print(x,"\t",end="")
            else:
                print(x,"\t",end="")
#step14==>call your function
#while True:
    #month=int(input("\nenter a month number 1-12\t"))
    #year=int(input("\nenter a year\t"))
cal(month,year)
#step15==>stop
