"""
Author: Noa Kirschbaum
Assignment / Part: HW2 - Q6a
Date due: 2022-06-08
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

s_length = int(input("Please enter the length of the sequence: "))
print("Please enter your sequence: ")

f_product = 1
for i in range(s_length):
    num = int(input())
    f_product *= num

print("The geometric mean is: {0:.4f}".format(f_product**(1/s_length)))