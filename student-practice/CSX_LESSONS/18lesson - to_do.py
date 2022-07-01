"""
ToDo for 18_access_modifiers
"""

# TODO: Section 4

# Define a class called "User" that has the public instance attribute "username" and the private
# instance attribute "password". Then define a method within the "User" class called
# "check_password()" that will take an input with the question reading "What is the password?: ".
# The method should compare the input to the password defined in the instantiation of the "User"
# class. If the passwords match, then the method should print "The password entered is correct."
# If the passwords do not match, the method should print the statement "The password entered is
# incorrect."


class User:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
    

    def check_password(self):
        password = input("What is the password? ")
        if password == self.password:
            print("The password entered is correct.")
        else:
            print("The password entered is incorrect.")

user1 = User("cool_coder", "abcd1234")
user1.check_password()

print(user1.password)

# Next define an instantiation of the "User" class with "username" equal to "cool_coder" and
# password equal to "abcd1234!" and store it in the variable "user_1". Then call the
# "check_password()" method.

 

# Lastly, try to print the "password" variable directly. If you receive an error, consider the
# reasoning behind this output.


