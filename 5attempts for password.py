#5 attempts
attempt=0
# password=123
while attempt<=5:
    password=int(input("Enter the password:"))
    if password==123:
        print("Login successful")
        break
    else:
        print("wrong password")
        attempt+=1
if attempt==5:
    print("limit reached")

