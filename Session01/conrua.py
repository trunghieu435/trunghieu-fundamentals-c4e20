from turtle import *

speed(-1)
shape("turtle")
color("green")

n=int(input("Nhap So Canh Ban Muon Ve = "))
Scope= 360/n
for t in range(100):
    for i in range(n):
        forward(100-t)
        left(Scope)

mainloop()