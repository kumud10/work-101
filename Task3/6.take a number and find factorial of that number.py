#6) Take a number and find factorial of that number
num = int(input("Enter Number: "))

def fact(num):
    if num == 1:
        return 1
    else:
        return num*fact(num-1)
print(f"Factorial of {num} is {fact(num)}")
