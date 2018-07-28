menu =["One Piece","Photo","Travel"]
print('*'*20)
print("There are something I love :")
for index, item in enumerate(menu):
    print(index+1, item)
print('*'*20)
n = int(input("Position you want to replace?"))
m = input("What you want to repalce?")
menu[n-1] = m
print('*'*20)
print("The new list is :")
for index, item in enumerate(menu):
    print(index+1, item)
  
print('*'*20)