
print("This Program keeps track of your financial budget")
print("please, enter the following: ")

income = float(input("\tYour Monthly Income:  "))
living = float(input("\tYour Budgeted living expenses:  "))
actual_living = float(input("\tYour actual living expenses:  "))
taxes = float(input("\tYour actual taxes withheld:  "))
tithe = float(input("\tYour actual tithe offerings:  "))
other = float(input("\tYour actual other expenses:  "))

print("The following is a report on your monthly expenses")
print("\tItem\t\t   Budget\t\t   Actual")
print("\t" + "="*15 + " " + "="*15 + " " + "=" * 15)
print(f"\tIncome\t\t  ${income}\t\t  ${income}")
print(f"\tTaxes\t\t  ${taxes}\t\t  ${taxes}")
print(f"\tTithing\t\t  ${tithe}\t\t  ${tithe}")
print(f"\tLiving\t\t  ${living}\t\t  ${actual_living}")
print(f"\tother\t\t  ${other}\t\t  ${income}")

