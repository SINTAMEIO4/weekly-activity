def supermarket_discount():
    # Ask the user to enter purchase amount
    purchase_amount = float(input("Enter total purchase amount: "))

    # Check if customer qualifies for discount
    if purchase_amount >= 10000:
        discount = 0.15 * purchase_amount
    else:
        discount = 0

    # Calculate final amount
    final_amount = purchase_amount - discount

    # Display results
    print("\n--- Purchase Details ---")
    print("Purchase Amount:", purchase_amount)
    print("Discount:", discount)
    print("Final Amount:", final_amount)


supermarket_discount()
