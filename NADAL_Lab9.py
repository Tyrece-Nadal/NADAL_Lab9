# Get user input for the number of rows
num_rows = int(input("Enter the number of rows for the triangle: "))

# Initialize a counter
counter = 1

# Print the triangle
for i in range(1, num_rows + 1):
    for j in range(i):
        print(counter, end=' ')
        counter += 1
    print()  # Move to the next line after each row