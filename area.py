
print("Enter the length: ")
length = float(input())  # Convert input to a float (decimal) number

print("Enter the width: ")
width = float(input())  # Convert input to a float (decimal) number

print("Enter the height: ")
height = float(input())  # Convert input to a float (decimal) number

# Calculate the volume and surface area
volume = length * width * height
surface_area = 2 * (length * width + length * height + width * height)

# Print the results
print(f"Your {length} X {width} X {height} cuboid has a volume of {volume} cubic feet and a surface area of {surface_area} square feet.")




price = float(input("Enter the price of the food:"))
priceTaxIncluded = price * 0.18 + price
print("This is the price tax included:" , priceTaxIncludedl)