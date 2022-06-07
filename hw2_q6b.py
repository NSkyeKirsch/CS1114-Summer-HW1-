"""
Author: Noa Kirschbaum
Assignment / Part: HW2 - Q6b
Date due: 2022-06-08
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

s_length = 0
print("""Please enter a non-empty sequence of positive integers, 
each one on a separate line. End your sequence by typing done.""")

num = 0
f_product = 1
while num != "done":
    num = input()
    if num != "done":
        f_product *= int(num)
        s_length += 1

print()
print("The geometric mean is: {0:.4f}".format(f_product**(1/s_length)))