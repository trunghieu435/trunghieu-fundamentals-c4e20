Username = "c4e"
Password = "codethechange"

import getpass
print("Hi there, this is a superuser gateway")
n = input("Username:")

if n == Username:
    m = getpass.getpass()
    if m == Password:
        print("Welcome to Techkids")
    else:
        print("This is not Password")
else : 
    print("Username is incorrect")