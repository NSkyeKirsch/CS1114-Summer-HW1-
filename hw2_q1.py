"""
Author: Noa Kirschbaum
Assignment / Part: HW2 - Q1
Date due: 2022-06-08
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

weight = float(input("Please enter weight in kg: "))
height = float(input("Please enter height in meters: "))

BMI = weight/(height ** 2)

if BMI < 18.5:
    status = "Underweight"
elif BMI <= 24.9:
    status = "Normal"
elif BMI <= 29.9:
    status = "Overweight"
else:
    status = "Obese"

print('Your BMI is: {0:.7f} and your weight status is: "{1}".'.format(BMI, status))