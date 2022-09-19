#9) check if number is <100, if yes check if its even or odd
print("\n")

num = int(input("Enter Number: "))

if num<100:
    if num % 2 !=0:
        print(f"Number ({num}) is Odd")
    else:
        print(f"Number ({num}) is not Odd")
else:
    print("Number Greater Than 100")


print("\n")
