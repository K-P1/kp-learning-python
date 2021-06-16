"""write a program to ask the user for their name,  then ask the user to write a sentence that contains the word " I " (hint: i am a boy and i enjoy playing football). then replace the occurences of the letter " I " with their name"""
name = input("Enter your name:\t")
name = name + " "
statement = input("Make a statement:\t")
print(statement.replace("I ",name))
