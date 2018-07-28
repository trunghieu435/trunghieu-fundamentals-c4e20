flock =[5,7,300,90,24,50,75] 
print("Hello, My name is Hieu and these are my sheeps size ")
print(flock)
n=max(flock)
print("Now my biggest sheep has size",n, "let's shear it")
flock.remove(n) 
flock.append(8)
print("After shearing, here is my flock")
print(flock)
flock =[x+50 for x in flock]
print("One month has passed, now here is my flock")
print(flock)
