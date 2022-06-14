"""
Using methods on lists and dictionaries
"""

# TODO: Section 1.1:
sweet_foods = ["ice cream", "skittles", "broccoli", "strawberries", "oreos", "asparagus"]

# Remove "broccoli" from the sweet_foods list using the .remove() function.


sweet_foods.remove("broccoli")
print(sweet_foods)


# TODO: Section 1.2:
# Remove the last item in the list using the .pop() method. Do not set it equal to a variable.

sweet_foods.pop()


# TODO: Section 1.3:
# Use the .pop() method again on the list. This time, use it to remove the first item in the list.
# Set it equal to a variable called "first_item", then print that variable.

first_item = sweet_foods.pop(0)
print(first_item)

# TODO: Section 1.4:
# Append the "first_item" to the "sweet_foods" list.

sweet_foods.append(first_item)


# TODO: Section 1.5:
# Print the sweet_foods list. Your output should be:
# ['skittles', 'strawberries', 'oreos', 'ice cream']

print(sweet_foods)

####################################################################################################

# TODO: Section 2:
values = [1, 2, 3, 4, 5, 6]

# Segment the items in the list "values" to include only the even numbers.
# Save this slice as the variable "even". Then, print the "even" variable.
# HINT: What argument can be passed in a slice to skip every other item in a list?


even = values[1::2]
print(even)

####################################################################################################

# TODO: Section 3.1:
my_car = {"make": "Tesla", "model": "Cybertruck", "year": "2022"}

# Use the .get() method on the "my_car" dictionary to search for the "car_type" key. Set it equal
# to a variable called "c_type". If that key doesn't exist, have the .get() method return
# "type doesn't exist". Finally, print c_type's value.


c_type = my_car.get("car_type","Does not exist")
print(c_type)

# TODO: Section 3.2:
# Next add a key/value pair of "car_type": "Electric" to the above "my_car" dictionary

my_car['car_type'] = "Electric"
print(my_car)

# TODO: Section 3.3:
# Use the .pop() method to remove the "year" key/value pair from the "my_car" dict and set it equal
# to a variable called "year". Print the "year" variable and print the "my_car" dictionary.

year = my_car.pop("year")
print(my_car)
print(year)


# TODO: Section 3.4:
automobile_attributes = ['color', 'engine', 'door count']


# First, append the string "make" to the "automobile_attributes" list. Then set a variable called
# "car_make" equal to the last item in the newly updated list.


car_make = automobile_attributes.append("make")


# Next use "car_make" to find the value of the key/value pair in the "my_car" dictionary using the
# format "dict[key]".


car_make = automobile_attributes[3]
car_make_value = my_car.get(car_make)
print(my_car[car_make])

# Finally, print the output of "car_make" to access that value. (Ex: print(dict_name[var_with_key]))

