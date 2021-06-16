"""
Take Home Project

1. Write a program for an e-commerce store. The program must accept
at least 10 products on the first run. The storekeeper should be given
the option to Add a product, remove a product, empty the product
catalog and close the program.

2. Create a membership system that allows users to register and login
after registration.

3. Write a budget for the United states of America for any 20 states of
your choice in tabular form with the following columns, index, State,
Allocation, Population, allocation per head\
"""
#================ Number 1==================
"""
1. Write a program for an e-commerce store. The program must accept
at least 10 products on the first run. The storekeeper should be given
the option to Add a product, remove a product, empty the product
catalog and close the program.

Code for Number 1
print("Welcome to Lizzy Autos")
catalog = []
isMoreProduct = "yes"
for i in range(4):
    name_of_product = input("Enter Product:\t")
    catalog.append(name_of_product)

while isMoreProduct == "yes":
        isMoreProduct = input("Do you have more products to add?\t")
        isMoreProduct = isMoreProduct.lower()
        if isMoreProduct == "yes":
            name_of_product = input("Enter Product:\t")
            catalog.append(name_of_product)
        else:
            break
print("\n\nList of Products\n")

while True:
    for x in catalog:
        print(x)
    print("")
    print("1. Add a Product")
    print("2. Remove a Product")
    print("3. Clear The Catalog")
    print("4. Quit")
    print("")
    option = int(input("Choose an Option\t"))
    print("")
    if option == 1:
        name_of_product = input("Enter Product:\t")
        catalog.append(name_of_product)
    elif option == 2:
        product_to_remove = int(input("Enter Product index:\t"))
        catalog.pop(product_to_remove - 1)
    elif option == 3:
        catalog.clear()
    elif option == 4:
        break
    else:
        print("Invalid Input")
    
"""
    
#================ Number 2==================
"""
2. Create a membership system that allows users to register and login
after registration.
"""
#================Number 3================
"""
3. Write a budget for the United states of America for any 20 states of
your choice in tabular form with the following columns: State,
Allocation, Population, allocation per head\
"""

print("Welcome to the United States Data Center\n")
print("State\tAllocation($)\tPopulation(M)\tAllocation/Head($)\n")
print(f"California\t\t2\t\t3\t{round(2/3,3)}")




