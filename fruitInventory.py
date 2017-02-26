import test

def add_fruit(inventory, fruit, quantity=0):
    inventory['fruit'] = quantity


# make these tests work...
new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
test.Equal('strawberries' in new_inventory, True)
test.Equal(new_inventory['strawberries'], 10)
add_fruit(new_inventory, 'strawberries', 25)
test.Equal(new_inventory['strawberries'] , 25)
