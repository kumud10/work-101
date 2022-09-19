#1) Average of 5 Numbers
sum = 0 
for i in range(5):
    n = int(input(f"Enter {i+1} Number: "))
    sum += n


average = sum/5
print("The Average is: ",average)
