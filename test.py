"""x = 3
y = float(3)
print(x,y)

values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6])

"test"
["t","e","s","t"]

x = "this is a thing"
y = x.split( )
z = y[0]
print(y)
print(z)"""

#Using the "input" method in Python, ask a user to input a sentence. Then develop a function that accepts a the user input and will tell you how many words are in that string##

"""a = ("I am good")
def count_words(a):
    if a == "I am good":
        print(3)
    else:
        print("error")
count_words(a)"""
    

"""day_of_week = input("what day is it?")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")"""

"""x = "test"
print(f"hello {x}")
temp = 75
if temp > 68:
    print("warm")
elif temp == 68:
    print("perfect")
else:
    print("cold)"""

"""def oddoreven(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")"""

"""bill = 10

tip = "bad"
if tip == "bad":
     print(bill * 1)
elif tip == "okay":
     print(bill * 1.15)
elif tip == "good":
     print(bill * 1.20)
elif tip == "great":
     print(bill * 1.25)"""

"""def factors(x):
    if x == 0:
        print("None")
    for i in range(2, x ):
        if x % i == 0:
            print(i)
factors(120)"""



def GCF(x, y):
    if x == 0 or y == 0:
        print("No GCF")
    elif x == 1 or y == 1:
        print("1")
    for i in range(2, min(x, y)):
        if x % i == 0 and y % i == 0:
            print(i)
GCF(12,18)

