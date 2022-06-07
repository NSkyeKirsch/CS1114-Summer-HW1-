"""
Author: Noa Kirschbaum
Assignment / Part: HW2 - Q3
Date due: 2022-06-08
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

import math

print("Please enter the lengths of a triangle's sides")

side_a = float(input("Length of the first side: "))
side_b = float(input("Length of the second side: "))
side_c = float(input("Length of the third side: "))

side_ab = False
side_bc = False
side_ac = False

if side_a > side_b:
    if side_a - side_b < 0.00001:
        side_ab = True
else:
    if side_b - side_a < 0.00001:
        side_ab = True

if side_b > side_c:
    if side_b - side_c < 0.00001:
        side_bc = True
else:
    if side_c - side_b < 0.00001:
        side_bc = True

if side_a > side_c:
    if side_a - side_c < 0.00001:
        side_ac = True
else:
    if side_c - side_a < 0.00001:
        side_ac = True

if side_ab and side_bc and side_ac:
    print("Equilateral triangle")

elif side_ab:
    if side_c == side_a * math.sqrt(2.0):
        print("Right Isosceles")
    else:
        print("Isosceles (not right)")
elif side_bc:
    if side_a == side_b * math.sqrt(2.0):
        print("Right Isosceles")
    else:
        print("Isosceles (not right)")
elif side_ac:
    if side_a == side_b * math.sqrt(2.0):
        print("Right Isosceles")
    else:
        print("Isosceles (Not right)")
else:
    print("Other triangle")