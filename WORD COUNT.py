"""
Write a program that asks the user to enter a sentence
then print the number of words
in the sentence.
Ask the user to enter a word or character and tell if the word
or character are present in the typed sentence.
"""
'''
line =input("Enter a sentece:  ")
spaceCount = line.count(" ")
wordsCount = spaceCount + 1
print(f"Number of spaces: {spaceCount}\nNumber of words:\
{wordsCount}")
'''

line = input("Enter a sentence:  ")
splt = line.split()
wordsCount = len(splt)
print(f"Number of spaces: {wordsCount - 1}\nNumber of words:\
{wordsCount}")


test = input("Enter a char/word:  ")
result = test in line
print(f"The char/word \"{test}\" is present: {result}")















