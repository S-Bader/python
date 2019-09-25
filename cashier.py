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

