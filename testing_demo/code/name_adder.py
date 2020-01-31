"""
First, you need to import a unittest and the function you want to test, formatted_name() .
Then you create a class, for example NamesTestCase, that will contain tests for your formatted_name() function.
This class inherits from the class unittest.TestCase.
"""
from name_adder_use import formatted_name

print("Please enter the first and last names or enter x to E[x]it.")

while True:
    first_name = input("Please enter the first name: ")
    if first_name == "x":
        print("Good bye.")
        break

    last_name = input("Please enter the last name: ")
    if last_name == "x":
        print("Good bye.")
        break

    result = formatted_name(first_name, last_name)
    print("Formatted name is: " + result + ".")
