"""
Author: Noa Kirschbaum
Assignment / Part: HW2 - Q2
Date due: 2022-06-08
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

# input: two strings.
# first is modified, second has two values with a space between

original_str = input("Enter a string to modify: ")

replace_str = input("Enter an index value and a character: ")

new_str = ""

for char in original_str:
    if char != replace_str[0]:
        new_str += char
    else:
        new_str += replace_str[2]

print("Your modified string is: {}".format(new_str))
