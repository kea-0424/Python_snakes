# a = int(input("Enter your first number: "))
# b = int(input("Enter your second number: "))
# c = int(input("Enter your third number: "))
# d = int(input("Enter your fourth number: "))

# def calculate_average(a, b, c, d):
#     average = (a + b + c + d) / 4
#     print("Average:", average)
#     return average

# calculate_average(a, b, c, d)

def caculate_average():
 a = int(input("Enter your first number: "))
 b = int(input("Enter your second number: "))
 c = int(input("Enter your third number: ")) 
 d = int(input("Enter your fourth number: "))

 
 average =(a + b + c + d) / 4 
 print(f"Your Average marks is {average}")
 return average

caculate_average()