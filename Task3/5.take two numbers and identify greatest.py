#5) take two numbers and identify greatest
print("\n")
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if num1 == num2:
    print("Both Number are Equal")
else:
    if num1<num2:
        print(f"{num2} is Greater! ")
    else:
        print(f"{num1} is Greater! ")

print("\n")
