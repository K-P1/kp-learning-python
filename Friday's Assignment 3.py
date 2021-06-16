from random import randint

number = randint(1, 50)

guess = 0

tries = 0

print("Hello! What is your name?")
name = input()

print("Well, " + name + ", I am thinking of a number between 1 and 50.")

while guess != number:
    print("Take a guess.")

    guess = int(input())

    tries += 1

    if guess > number:
        print("Your guess is too high")
    elif guess < number:
        print("Your guess is too low")
    else: #guess == number
        print("Good job, " + name + "! You guessed my number in " + str(tries) + " guesses!")

if tries <= 6:
    print("You win")
else:
    print("You don't win")
        
