# Create a dictionary
student = {
    "id": 101,
    "name": "Sowmya",
    "department": "CSE",
    "marks": 90
}

# Value to search
search_value = input("Enter value to search: ")

# Reverse lookup
found = False
for key, value in student.items():
    if str(value) == search_value:
        print("Key for the given value is:", key)
        found = True
        break

if not found:
    print("Value not found in dictionary")
