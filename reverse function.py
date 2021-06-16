
word = input("enter a word: ")
"""number = len(word) - 1
while(number >= 0): # base condition
    print(word[number], end = "")
    number -=1
"""

def reverse(word, num):
    print(word[num], end = "")
    if len(word) == 1:
        return 
    else:
        word = word[:-1]
        return reverse(word, len(word) - 1)
reverse(word, len(word) - 1)
