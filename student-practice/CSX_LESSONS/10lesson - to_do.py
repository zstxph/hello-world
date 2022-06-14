"""
Expanding on loops
"""

# TODO: Section 1.1:

# Write a program that takes a user input of an integer and store it in a variable called
# "user_int". If the integer is even, print the statement "[user_int] is even.". Otherwise, print
# the statement "[user_int] is odd."
# TIP: Remember modulo from the Basic Math lesson?
# TIP: Consider how that can help us identify odd/even numbers.

user_int = int(input("enter an integer: "))
if user_int % 2 == 0:
    print(f"{user_int} is even.")
else:
    print(f"{user_int} is odd.")


# note to self:
# #  A great way to use the modulo in context is to use it to test
#  whether for odd or even numbers. If a number can be divisible 
#  by 2 without a remainder, then by definition the number is even.
#  If the number is divided by 2 that equation yields a remainder, 
#  then the number must be odd. To put this concept into Python terms:  if (num % 2 == 0): --insert code to execute here
                                        #                               else: #num is odd --insert code to execute here
#  The code above basically states that if a the remainder of a number 
#  divided by 2 is equal to zero, the number is even. If not, the number 
#  is odd. This snippet can be used to execute a number of different 
#  functions based on whether or not the number in question is even or 
#  odd -- insert your functions where it says "insert code here" to add 
#  some functionality to the snippet.


####################################################################################################

# TODO: Section 2.1
# Write a while loop that iterates through the list "todos". For each iteration, remove an item
# using the ".pop()" method and append it to the list "finsihed_todos". Keep track of all of your
# finished todos by printing "finished_todos" in each iteration.

todos = ["exercise for fun", "eat food", "go to school", "write some code"]
finished_todos = []

while todos:
    finished_todos = todos.pop()
    print(f"you finished task: '{finished_todos}' and it was removed from your todo list.")
    print(f"your remaining items are: {todos}")

####################################################################################################

# TODO: Section 2.2

# Write a while loop that increases "var" by increments of 2 until "var" is greater than or equal to
# 21. Note the wording of this question and set the condition appropriately. Print "var" in each
# iteration.

var = 7

while var <=21:
    var +=2
    print(var)

####################################################################################################

# TODO: Section 2.3

# Write a program that takes a user input of an integer and store it in a variable called
# "user_int". Write a loop with this integer as the condition and test if "user_int" is even.
# If "user_int" is even, increment "user_int" by 1. Otherwise, decrement "user_int" by 3.
# Then print "user_int" for each iteration.

# Important:
# For the purpose of this exercise please input only POSITIVE integers.

user_int = int(input("enter an integer: "))
if user_int % 2 == 0:
    print(f"the number you inputed is incremented by 1 and is now {user_int + 1 }.")
else:
    print(f"the number you inputed is incremented by 3 and is now {user_int + 3}.")
