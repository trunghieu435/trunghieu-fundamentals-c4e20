
from random import randint 
bingo = randint(0,100)
n = 0
loop = True
while loop :
    num = int(input("Input A Number (0-100) = "))
    if num < bingo :
        print("It's to small")
        n+=1 
    elif num > bingo :
        print("It's to big")
        n+=1 
    elif n == bingo :
        print("Bingo")
        loop = False
   
    if n==7:
        print("You lose")
        break