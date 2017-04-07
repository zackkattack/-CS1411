# Calculate the area and the circumfrence of a circle from its radius.
# Step 1: Prompt for radius.
# Step 2: Apply the formulas.
# Step 3: Print out the result.

import math

# Step 1
radius_str = input("Enter the radius of the circle: ")
radius_int = int(radius_str) # Convert radius_str into a integer 

# Step 2
circumfrence = 2*math.pi*radius_int
area = (math.pi)*(radius_int**2)

# Step 3
print
print "The area of the circle is:", area
print "The circumfrence of the circle is:" , circumfrence
