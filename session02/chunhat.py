m = int(input(" So Hang = "))
for t in range(m+1):
    for i in range(m+1):
        if i < m - t :
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()

