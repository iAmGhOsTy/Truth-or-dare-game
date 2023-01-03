import random


x= open("dares.txt","r")
x = x.read().splitlines()

def getDare():
    return random.choice(x)
print(getDare())