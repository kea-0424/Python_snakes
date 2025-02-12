# Exercise 2 shopping cart program

item = input("What are you going to buy?: ")
price = float(input("How much is it?:M ")) #typecasting
quantity = int(input("How many do you want?: "))
total = price * quantity 

print(f"You have bought {quantity} {item}/s")
print(f"Your total is: M{total}")