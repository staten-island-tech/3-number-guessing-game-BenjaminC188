def NumberGuessingGame():
    import random
    imput = y
    x = random (1 - 10)
    y = int(input("Guess a number between 1 and 10: "))
    for i in range(3):
        if x == y:
            print("You've won!")
        elif x > y:
            print("Too low!")
        elif x < y:
            print("Too high!")