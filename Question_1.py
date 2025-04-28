# Question 1.1

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
 958,743, 527 ]

even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    elif number == 237:
        break
print("\nEven numbers are: ", even_numbers)

# Question 1.2
even_numbers = [386, 462, 418, 344, 236, 566, 978, 328, 162, 758, 918]
tuple_numbers = tuple(even_numbers)
print("\nEven numbers as a tuple are: ", tuple_numbers)

# Question 1.3
sum_of_even_numbers = 0
for number in numbers:
    if number % 2 == 0:
        sum_of_even_numbers += number
print("\nSum of all even numbers is: ", sum_of_even_numbers)

# Question 1.4
sum_of_odd_numbers = 0
for number in numbers:
    if number % 2 != 0:
        sum_of_odd_numbers += number
print("\nSum of all odd numbers is: ", sum_of_odd_numbers)