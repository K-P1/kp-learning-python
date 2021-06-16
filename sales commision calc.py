"""
(Sales-Commission Calculator) One large chemical company pays its salespeople on a commission
basis. The salespeople receive $200 per week plus 9% of their gross sales for that week. For
example, a salesperson who sells $5000 worth of chemicals in a week receives $200 plus 9% of
$5000, or a total of $650. Develop a program that will input each salesperson’s gross sales for last
week and will calculate and display that salesperson’s earnings. Process one salesperson's figures at a
time.
"""

while True:
    sales = float(input("Enter sales in dollars (-1 to end):  "))
    salary = round(200 + (0.09 * sales), 2)
    if sales == -1:
        break
    print(f"Your salary is ${salary}")
