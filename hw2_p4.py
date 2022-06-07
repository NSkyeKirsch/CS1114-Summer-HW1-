"""
Author: Noa Kirschbaum
Assignment / Part: HW2 - Q4
Date due: 2022-06-08
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

in_str = "The quick brown fox jumps over the lazy dog"
the_str = in_str.upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for char in the_str:
    if char.isalpha():
        index = alphabet.find(char)
        if index > -1:
            alphabet = alphabet.replace(alphabet[index], "")

print("missing characters: {}".format(alphabet) if len(alphabet) > 0 else True)
