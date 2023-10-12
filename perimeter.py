def calculate_perimeter(length,width):
    perimeter = 2 * (length + width)
    return perimeter

# Taking user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate and print the perimeter
perimeter = calculate_perimeter(length, width)
print("The perimeter of the rectangle is:", perimeter)
