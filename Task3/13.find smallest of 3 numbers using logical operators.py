#13) find smallest of 3 numbers using logical operators
print("\n")
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

if(num1 < num2 and num1<num3):
    print(f"{num1} is smallest")
elif(num2 < num1 and num2 < num3):
    print(f"{num2} is smallest")
else:
    print(f"{num3} is smallest")

print("\n")
