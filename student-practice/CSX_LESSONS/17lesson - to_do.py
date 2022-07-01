"""
Classes ToDo
"""

# TODO: Section 1

# Create a class for an "Employee" that includes the instance attributes: "first_name", "last_name",
# "salary", and "title".

from ctypes.wintypes import LANGID
from smtplib import SMTPRecipientsRefused
from turtle import color


class Employee: 
  def __init__(self,first_name, last_name, salary, title):
    self.firstname = first_name
    self.lastname = last_name
    self.salary = salary
    self.title = title
    

# Next, within the "Employee" class, create a method called "printer()" that prints the statement,
# "[first_name] [last_name] works as a [title] and makes $[salary] per year."
# IMPORTANT: Use f shorthand to fosrmat your print statement.

  def printer(self):
    print(f"{employee1.firstname} {employee1.lastname} works as {employee1.title} and makes ${employee1.salary} per year.")



# Then, define a new instantion of "Employee" with "first_name" equal to "Spongebob", "last_name"
# equal to "Squarepants", "salary" equal to "50000" and "title" equal to "Fry Cook"

employee1 = Employee("Spongebob", "Squarepnats", "50000", "Fry cook")


# Lastly, call the "printer()" method to print your formatted statement.


employee1.printer()



####################################################################################################

# TODO: Section 2

# Below is the class "SuperHero" with the instance attributes "name" and "powers". Within the class,
# write a method called "add_power()" that adds a new superpower to the "powers" list.

class SuperHero:
  def __init__(self, name):
    self.name = name
    self.powers = []

  # FIXME: Write your method here.
  def add_power(self,power):
    self.powers.append(power)


# Then, define a new instantiation of "SuperHero" with the "name" equal to "Superman" and store it
# in a variable called "super".

supers = SuperHero("Superman")

# Next, call the "add_power()" method three times to add the superpowers: "heat vision",
# "super strength", and "invincibility".

supers.add_power("heat vision")
supers.add_power("super strength")
supers.add_power("invincibility")

# Lastly, print the list of Superman's superpowers.

print(f"{supers.name}'s list of powers: {supers.powers}")

####################################################################################################

# TODO: Section 3

# Create a class named "Animal" with the instnace attributes "num_legs" and "weight".

class Animal:
  def __init__(self, num_legs, weight):
    self.num_legs = num_legs
    self.weight = weight


# Then create a child class derived from "Animal" named "Mammal". Define the class attribute
# "habitat" equal to "land" for "Mammal". Define "species" and "color" as new instance attributes in
# the "Mammal" class.
# HINT: Use the "super()" function.

class Mammal(Animal):
  def __init__(self, habitat, species, color):
    super().__init__(species, color)
   
    self.habitat = habitat
    self.species = species
    self.color = color
    

# Define a method in the "Mammal" class called "printer()" that prints the statement "The [species]
# is [weight] pounds and lives on [habitat]".


# Define an instantion of the "Mammal" class with "num_legs" eqaul to 4, "weight" equal to
# "700", "species" equal to "black bear", and "color" equal to "black" stored in the variable
# "bear".

animal1 = Animal("4", "700")
mammal1 = Mammal("land", "black bear", "black")

print(f"The {mammal1.species} is {animal1.weight} pounds and lives on {mammal1.habitat}.")

# Lastly, call the "printer()" method.

print(printer)
