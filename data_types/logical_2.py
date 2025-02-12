#Logical operators2

num = int(input("Enter any number "))

if num == 0:
    print ("N/a")

elif num > 0 and num % 2 == 0:
    print(f"{num} is even and positive.")
    
elif num < 0 and num % 2 != 0:
    print(f"{num} is odd and negative.")

else:
    print("This number doesn't meet the conditions")