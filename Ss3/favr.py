fav = ["OP","Photo","Film Making"]
print("Hi, there are some of my favorite things :")
print(*fav,sep=", ")
n = input("Name one thing you like ")
fav.append(n)
print(*fav,sep=", ")