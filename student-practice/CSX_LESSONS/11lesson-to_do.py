"""
Working with functions and scope
"""

# TODO: Section 1
# Define a function called "double()" that sets a parameter of "x". The function should double "x"
# and print the product. Call the function and pass it the below variable as an argument.
double_this = 7



def double(x):
    x = double_this*2
    print(x)
    return(x)
double(double_this)

# After completing the above, define a function called "printer()" that sets no parameter.
# The function should just print the "double_this" variable. Then call the function.

def printer():
    print(double_this)
printer()


####################################################################################################

# TODO: Section 2
# Copy your "double()" function from above to this block of code. Change the function to use a
# return value, store that return value in a variable, and print the product.
double_this = 38


def double(x):
    x = double_this*2
    print(x)
    return(x)
double(double_this)

 

####################################################################################################

# TODO: Section 3
# Write a function that takes an input statement of an integer and store it in a variable called
# "num". and then tests if the integer is even or odd. If the input is even, print "[num] is even."
# Otherwise print the statement "[num] is odd." Lastly call the function.



def user_input(num):
    
    if num % 2 == 0:
        num = f'{num} is even.'
    else: 
        num = f"{num} is odd."

    return num


def inquire_num():
    user_num = int(input(f"Enter a number: "))

    user_msg = user_input(user_num)
    print(user_msg)


inquire_num()




####################################################################################################

# TODO: Section 4
# Define a function that takes a dictionary as a parameter, loops through the dictionary, and
# returns the iteration number, key, and value in the following format:
# "Iteration number [1] returns the key [key] and the value [value]." Lastly call the function.

# Here is an example dictionary:
EXAMPLE_DICTIONARY = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}


def dict_reader(dict):

    for key in dict:
        print (f"{key} returns {dict[key]}.")
    
    for value in dict:
        print (f"{value} returns {dict[key]}")
    
    print(f"iteration number {4} returns the key {key} and the value {value}.")

dict_reader(EXAMPLE_DICTIONARY)

print()