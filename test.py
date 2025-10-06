import random
x = 0
y = random.randint(1, 10)
def number_guessing_game(y):
    while x != y:
        x = int(input("Guess a number between 1 and 10."))
        if x < y:
            print("Too low")
        elif x > y:
            print("Too high")
        else:
            print("You guessed the number")


















"""def lang(x):
    for char in x:
        print(char)
        if t and T in char < s and S in char:
            print
lang("One Two three")"""

