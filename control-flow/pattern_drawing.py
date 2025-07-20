size =int(input("Enter the size of the pattern: "))

for i in range(size):
    for j in range(size):
        print("*", end="")
    print()  # Move to a new line after each row
