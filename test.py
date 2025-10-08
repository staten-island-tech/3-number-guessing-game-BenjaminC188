import random
x = 0  
def number_guessing_game():
    y = random.randint(1, 10)
    guesses = []
    while x != y:
        x = int(input("Guess a number between 1 and 10"))
        guesses.append(x)
        if x < y:
            print("Too low")
            print(guesses)
        elif x > y:
            print("Too high")
            print(guesses)
        else:
            print("You guessed the number!")
            print("guesses:")
            for guess in guesses:
                print(guess)

number_guessing_game()


















"""def lang(x):
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
lang("One Two three")"""







def spaces(y,t):
    a = (".")
    b = ("C")
    for char in y,t:
        print(char)
        if b == a:
            occupied + 0
        elif b == b:
            occupied += 1
            print(occupied)

spaces("CCC..", ".C.C.C")