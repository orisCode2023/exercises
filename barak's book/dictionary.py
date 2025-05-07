import random

prices = {"banana": 10, "apple": 8, "brad": 7, "cheese": 20, "juice": 15, "mango": 7}
shopping_cart = {}
total = 0
for product in prices:
     shopping_cart[product] = random.randint(1, 10)
     amount = int(shopping_cart.get(product))
     price  = int(prices.get(product))
     total += (amount * price)

print(f"The total of the shopping list is: {total} ")
if prices.get("mango") == None:
    print("the item dose not exist")
else:
    shopping_cart["mango"] = 7

