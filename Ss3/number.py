n = int(input(" Your number = "))
count = 0 
loop = True
while loop :
    if n > 1 :
        n = n/10
        count +=1
    else :
        print(count)
        break
