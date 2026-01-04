def modify_list(items):
    items.append(42) # Modifies the original list object in-place
    print("Inside function: items =", items)

my_list = [1, 2, 3]
modify_list(my_list)
print("Outside function: my_list = ",my_list)
