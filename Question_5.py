# Question 5.1
# Question 5.2
# Question 5.3


def calculate_circle_area(radius):

    import math
    return math.pi * (radius ** 2)
radius= float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is: {area}")
