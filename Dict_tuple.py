inventory ={}
inventory['Apple'] = 7
inventory['Banana'] = 4

print("Before inventory update")
print(inventory)

inventory['Apple'] +=2
inventory['Banana'] -=3

print("After inventory update")
for item,quantity in inventory.items():
    print(item ,":", quantity)