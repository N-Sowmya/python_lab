s = input("Enter a string: ")

largest = s[0]
smallest = s[0]

for ch in s:
    if ch > largest:
        largest = ch
    if ch < smallest:
        smallest = ch

print("Largest character:", largest)
print("Smallest character:", smallest)
