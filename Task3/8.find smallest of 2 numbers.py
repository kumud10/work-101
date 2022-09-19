#8) find smallest of 2 numbers
print("\n")
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if num1 == num2:
    print("Both Number are Equal")
else:
    if num1<num2:
        print(f"{num1} is Smaller! ")
    else:
        print(f"{num2} is Smaller! ")

print("\n")
