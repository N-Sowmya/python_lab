n = int(input("Enter number of elements: "))
total = 0

for i in range(n):
    val = input("Enter element: ")
    
    
    if val.replace('.', '', 1).isdigit():
        total += float(val)

print("Sum of numeric elements:", total)
