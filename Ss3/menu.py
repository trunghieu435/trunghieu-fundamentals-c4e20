menu = ["Cơm","Cá","Thịt Bò","Ghẹ","Pizza","Gà ở TDH"]
# print(*menu, sep=", ")
# menu.append("Ghẹ")
# print(*menu, sep=", ")
# n = len(menu)
# for i in range(n):
#     print(menu[i])
for index, item in enumerate(menu): 
    print("{}.{}".format(index + 1, item))
# for item in menu : 
#     print(item)
menu[4]="Tôm Hùm"
print(menu)