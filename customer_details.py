def customer_details():
    # Create a tuple containing customer information
    customer = ("Judith", "C001", "0712345678", "judith@gmail.com")

    # Display the complete tuple
    print("Customer Details:", customer)

    # Access customer's name and telephone number
    print("Customer Name:", customer[0])
    print("Telephone Number:", customer[2])

    # Display the number of items
    print("Number of Items:", len(customer))

    # Attempt to modify the telephone number
    try:
        customer[2] = "0798765432"
    except TypeError:
        print("The telephone number cannot be modified.")

    # Explanation
    print("Reason: A tuple cannot be changed after it has been created.")


customer_details()
