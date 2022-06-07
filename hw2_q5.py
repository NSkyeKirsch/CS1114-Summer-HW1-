"""
Author: Noa Kirschbaum
Assignment / Part: HW2 - Q5
Date due: 2022-06-08
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

max_value = int(input("Please input a positive integer: "))

for num in range(1, max_value + 1):
    even_count = 0
    odd_count = 0
    if len(str(num)) < 2:
        if num % 2 == 0:
            print(num, end=" ")
    else:
        for char in str(num):
            if int(char) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        if even_count > odd_count:
            print(num, end=" ")