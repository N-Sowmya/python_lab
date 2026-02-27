import random

# Writing 20 random numbers to the file
with open("random_numbers.txt", "w") as file:
    for _ in range(20):
        num = random.randint(1, 100)
        file.write(f"{num}\n")

print("20 random numbers written to random_numbers.txt")

# Reading the numbers from the file
with open("random_numbers.txt", "r") as file:
    print("Reading the 20 random numbers from random_numbers.txt file:")
    print(file.read())