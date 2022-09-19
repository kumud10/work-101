#7) swap 2 numbers
print("\n")
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print("\n")

print("Number before swapping are: ")
print(f"Number 1: {num1}")
print(f"Number 2: {num2}")

# Using third Variable
temp = num1
num1 = num2
num2 = temp

print("Number after swapping are: ")
print(f"Number 1: {num1}")
print(f"Number 2: {num2}")
