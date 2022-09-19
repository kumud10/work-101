#14) swap two numbers without third variable
print("\n")

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))


print("Number before swapping are: ")
print(f"Number 1: {num1}")
print(f"Number 2: {num2}")

num1, num2 = num2, num1

print("Number after swapping are: ")
print(f"Number 1: {num1}")
print(f"Number 2: {num2}")

print("\n")
