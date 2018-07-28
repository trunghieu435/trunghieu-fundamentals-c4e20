store = ["T-shirt","Sweater"]

for i in range(4) :
    n = input("Welcome to our shop, what do you want(C, R, U, D)?") 
    if n == "r":
        print("Our items :", *store, sep=', ')
    elif n == "c":
        m = input("Enter New Item:")
        store.append(m)
        print("Our items :", *store,sep=', ')
    elif n =="u" :
        t = int(input("Update position : "))
        m = input("New Iteam ?")
        store[t-1]=m
        print("Our items :", *store,sep=', ')
    elif n =="d" :
        t =int(input("Delete position "))
        store.remove(store[t-1])
        print("Our items :", *store,sep=', ')

