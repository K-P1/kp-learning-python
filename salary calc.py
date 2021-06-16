"""
(Salary Calculator) Develop a program that will determine the gross pay for each of several
employees. The company pays “straight time” for the first 40 hours worked by each employee and
pays “time-and-a-half” for all hours worked in excess of 40 hours. You’re given a list of the employees
of the company, the number of hours each employee worked last week and the hourly rate of
each employee. Your program should input this information for each employee and should determine
and display the employee's gross pay.
"""
while True:   #Initially an infinite loop
    workedHours = int(input("Enter # of hours worked (-1 to end):  "))   #gets worked hours of a worker
    if workedHours == -1:
        breakpoint  #exit the program if -1 is entered as worked hour
    hourlyPay = float(input("Enter hourly rate of the worker ($00.00): "))   #gets hourly pay of worker

    if workedHours <= 40:   #Handles salary for worked hour below or equal to 40
        salary = hourlyPay * workedHours
    else:       #Handles salary for worked hours labove 40
        extra = workedHours - 40
        salary = hourlyPay * 40 + (extra * 1.5 * hourlyPay)
    print(f"Worker's salary is ${salary}")
