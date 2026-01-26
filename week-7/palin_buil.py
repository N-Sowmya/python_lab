s = input("Enter a string: ")

if list(s) == list(reversed(s)):
    print("Palindrome")
else:
    print("Not a Palindrome")
