# Check the data type of all your variables using type() built-in function

# Using the len() built-in function, find the length of your first name
first_name = "rahul" 
print(len(first_name))
# Compare the length of your first name and your last name
last_name = "Singh"
print(len(first_name) == len(last_name))

# Declare 5 as num_one and 4 as num_two
# Add num_one and num_two and assign the value to a variable total
num_one = 5
num_two = 4
total = num_one + num_two
print(total)
# Subtract num_two from num_one and assign the value to a variable diff
sub= num_one - num_two
print(sub)
# Multiply num_two and num_one and assign the value to a variable product
mul = num_one*num_two
print(mul)
# Divide num_one by num_two and assign the value to a variable division
div = num_one/num_two
print(div)
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
mod = num_one%num_two
print(mod)
# Calculate num_one to the power of num_two and assign the value to a variable exp
power = pow(num_one, num_two)
print(power)
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_div = num_one//num_two
print(floor_div)
# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area. 
radius = int(input("Enter radius: "))
area_of_circle = 3.14*radius*radius
print(area_of_circle)
circum_of_circle = 2*3.14*radius
print(circum_of_circle)
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
country = input("Enter country: ")
age = input("Enter age: ")
print(first_name, last_name, country, age)
help("keywords")