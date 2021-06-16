# Write a program that calculates discount on a purchase such that if total purchase > 5000,
# discount = 10%, if purchase > 10000, discount = 12%, if purchase > 20000, discount = 15%
#and if purchase > 50000, discount = 20%. The program should remove the discount from the
# purchase and display the amount the customer has to pay.

purchase = int(input("Enter total amount of provisions purchased\t"))
discount = 0

if purchase > 50000:
    discount = (20/100) * purchase
elif purchase < 50000 and purchase > 20000:
    discount = (15/100) * purchase
elif purchase < 20000 and purchase > 10000:
    discount = (12/100) * purchase
elif purchase < 10000 and purchase > 5000:
    discount = (10/100) * purchase
else:
    discount = 0

print(f"The discount you will get on the total purchase of ${purchase} = ${discount}")

#Write a simple user registration and login system containing username and password only








