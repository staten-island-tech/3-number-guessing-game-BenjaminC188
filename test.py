import random
x = 0
def number_guessing_game():
    y = random.randint(1, 10)
    guesses = []
    x = 0
    while x != y:
        x = int(input("Guess a number between 1 and 10:"))
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
            print(guesses)
number_guessing_game()




















"""student = {
    'name': 'Cadee',
    'age' : 15,
    'grades' : (80,90,100)
}
print(student['name'])"""









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







"""def occupied(n,y,t):
    both = 0
    for i in range(n):
        if (y[i] == "C" and t[i] == "C"):
            both += 1 
    return both
print(occupied(5, "CCC..", "C.C.C"))"""