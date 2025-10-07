import random

def number_guessing_game():
    y = random.randint(1, 10)
    x = 0
    guesses = []
    while x != y:
        x = int(input("Guess a number 1 to 10"))
        guesses.append(x)
        if x < y:
            print("Too low")
        elif x > y:
            print("Too high")
        else:
            print("You guessed the number!")
            print(guesses)

number_guessing_game()

















def lang(x):
    t = 0
    s = 0
    for char in x:
        print(char)
        if char == "t" or char == "T":
            t += 1
        elif char == "s" or char == "S":
            s += 1
    if t > s:
        print("English")
    else:
        print("French")
lang("One Two three")

def spaces(y,t):
    for char in y:
        if char in t:
spaces("CCC..", ".C.C.C")