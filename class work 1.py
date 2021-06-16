"""write a program to prompt the user for a sentence then replace the spaces in the sentence with double asterisks and print out the result to the user.
with the same input they should print out the length of the sentence with spaces inclusive and spaces exclusive."""
sentence = input("Enter a sentence:\t")
print(sentence.replace(" ","**"))
print(len(sentence))
print(len(sentence.replace(" ","")))
