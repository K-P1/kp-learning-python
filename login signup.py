#Write a simple user registration and login system containing username and password only
print("Welcome to the user registration page")
username = input("Enter preferred username\t")
password = input("Enter preferred Password\t")
print("You can now login to your Dashboard")
username_entry = input("Enter your username\t")
password_entry = input("Enter your password\t")

if username_entry == username and password_entry == password:
    print("Login Successful")
else:
    print("Login Failed.\nIncorrect Username or Password")
