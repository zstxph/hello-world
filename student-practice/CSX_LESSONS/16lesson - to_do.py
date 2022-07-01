"""
Todo for 16_advanced_lists_and_dicts
"""

# TODO: Section 2

import enum
from tabnanny import check


stringy = "supercalifragilisticexpialidocious"

# Given the variable "stringy", use list comprehension to create a new list that includes all
# characters except for the letter "s".
# TIP: Conditions can be added to the end of list comprehensions.

x = [s for s in stringy if s != "s"]
#
listy = list(stringy)

#
print(x)

####################################################################################################

# TODO: Section 3

nums = [35, 47, 624, 19, 754, 90, 10]

# Given the list "nums", use a "for loop" and the "enumerate()" function to iterate through the
# list. Print the current iteration's number if the number is even OR if the index is even.
# TIP: Use the % operator to check if a number is even.


for index, num in enumerate(nums):
    if num % 2 == 0: 
        print(f"{num} is even at index {index}")
    else:
        print(f"{num} is odd at index {index}")

####################################################################################################

# TODO: Section 4.1

cities = {"Madrid": "Spain", "Seoul": "South Korea", "Boston": "United States", "Toronto": "Canada"}
check_cities1 = ["New York", "Boston", "Toronto"]
# Given the dictionary "cities", use a membership operator to check if the cities in the
# "check_cities1" list exist as keys in the cities dictionary. When a key exists, print the
# statement: "The city [city] exists in the dictionary." When a key does not exist, print the
# statement: "The city [city] does not exist in the dictionary."
# TIP: Loop through "check_cities1" to more easily test your condition.


for c in check_cities1:
    if c in cities:
        print(f"the city {c} exists in the dictionary.")
    else:
        print(F"the city {c} does not exist in the dictionary.")



# TODO: Section 4.2
check_cities2 = ["Rome", "Paris"]

# Using the same dictionary, use a different membership operator to check if the listed cities in
# "check_cities2" do not exist in the "cities" dictionary. If the city does not exist, print the
# statement: "This city does not exist in the dictionary."


for c in check_cities2:
    if c not in cities:
        print(f"The city {c} does not exist in the dictionary.")
