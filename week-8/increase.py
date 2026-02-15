n = int(input("Enter number of tuples: "))
tuples_list = []

for i in range(n):
    a = int(input("Enter first element: "))
    b = int(input("Enter second element: "))
    tuples_list.append((a, b))

sorted_list = sorted(tuples_list, key=lambda x: x[-1])
print("Sorted list:", sorted_list)
