def skip_multiples_of_seven():
    for num in range(1, 51):
        if num % 7 == 0:  
            continue  
        print(num)

skip_multiples_of_seven()
