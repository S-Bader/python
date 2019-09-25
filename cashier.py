print()
name = input("Item (If finished enter \"done\") : ")



item_list = []



while name != "done":
    
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    
    item = {}
    item["name"] = name
    item["price"] = price
    item["quantity"] = quantity

    item_list.append(item)
    name = input("Item (If finished enter \"done\") : ")

    

print()
print("------------------------")
print("receipt")
print("------------------------")


total= 0


for product in item_list:
    print("%d %s %.3f KWD" % (product["quantity"], product["name"], (product["price"] * product["quantity"])))
    total += (product["price"] * product["quantity"])

print("-------------------------")

print("Total Price: %.3f KWD" % total)

print()





# -------------------
# receipt
# -------------------
# 4 apples 0.800KD
# 1 carrot 0.100KD
# 2 flour 2.600KD
# 10 water bottles 0.500KD
# -------------------
# Total Price: 4.000KD













# A while loop that checks the users input. The loop ends if the user types "done" for the item name.
# Save the user's input (the item's name, price, quantity) in a dictionary. Append this dictionary to a list of items. This list of items is a list of dictionaries, where each dictionary represents an item.
# In the example above, the list of items looks like this:
# [ { "name": "apples", "price": .2, "quantity": 4 }, { "name": "carrot", "price": .1, "quantity": 1 }, { "name": "flour", "price": 1.3, "quantity": 2 }, { "name": "water bottles", "price": .05, "quantity": 10 }, ]
# Using a for loop, go through the list and print the receipt.
# Push your code.


# Item (enter "done" when finished): apples
# Price: .2
# Quantity: 4
# Item (enter "done" when finished): carrot
# Price: .1
# Quantity: 1
# Item (enter "done" when finished): flour
# Price: 1.3
# Quantity: 2
# Item (enter "done" when finished): water bottles
# Price: .05
# Quantity: 10
# Item (enter "done" when finished): done