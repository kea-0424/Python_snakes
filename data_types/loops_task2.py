
numbers =[ 2, 67, 3
, 213, 56, 87, 25, 73]


largest = numbers[0]


for num in numbers:
    if num > largest:
        largest = num

print(f"The largest number in the list is: {largest}")