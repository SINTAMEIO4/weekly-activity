def supermarket_inventory():
    #Create a dictionary named inventory with five products and quantities
    inventory = {
        "Milk": 40,
        "Bread": 25,
        "Sugar": 60,
        "Rice": 80,
        "Cooking Oil": 30
    }
    #Display the quantity of a specified product
    product = "Sugar"
    print("Quantity of", product + ":", inventory[product])

    #Add a new product to the dictionary
    inventory["Eggs"] = 100
    print("After adding Eggs:", inventory)

    #Update the quantity of an existing product
    inventory["Milk"] = 55
    print("After updating Milk:", inventory)

    #Remove one product from the dictionary
    del inventory["Bread"]

    #Display the final inventory
    print("Final Inventory:", inventory)

supermarket_inventory()
