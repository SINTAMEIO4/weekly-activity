def product_categories():
    # Create a set with product categories
    # Duplicate categories are automatically removed
    categories = {
        "Electronics",
        "Clothing",
        "Shoes",
        "Books",
        "Food",
        "Electronics",
        "Clothing"
    }

    # Display the set
    print("Product Categories:", categories)

    # Add a new category
    categories.add("Furniture")

    # Remove one category
    categories.remove("Books")

    # Display the final set
    print("Final Product Categories:", categories)

    # Explanation
    print("A set keeps only unique values, so duplicate product categories are automatically removed.")


product_categories()



