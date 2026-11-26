
print("==============================")
print(" MINI SHOP MANAGEMENT SYSTEM")
print("==============================")

products = []

while True:
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Search Product")
    print("6. Generate Bill")
    print("7. Sales Report")
    print("8. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))

        products.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })

        print("Product added successfully!")

    elif choice == 2:
        print("===== PRODUCT LIST =====")

        if not products:
            print("No products available!")
        else:
            for product in products:
                print("Name:", product["name"])
                print("Price:₹", product["price"])
                print("Quantity:", product["quantity"])
                print("--------------------")
    elif choice == 3:
        if not products:
            print("No products available!")
        else:
            for index, product in enumerate(products):
                print(index+1,".",product["name"],"-",product["price"],"-",product["quantity"])
            edit_index = int(input("Choose an option to Edit: "))-1
            if 0<=edit_index<len(products):
                product = products[edit_index]
                print("1. Edit Product")
                print("2. Edit Price")
                print("3. Edit Quantity")
                edit_choice = int(input("Choose an option: "))
                if edit_choice == 1:
                    product["name"] = input("Enter product name: ")
                    print("Updated Sucessfully!")
                elif edit_choice == 2:
                    product["price"] = input("Enter product price: ")
                    print("Updated Sucessfully!")
                elif edit_choice == 3:
                    product["quantity"] = input("Enter product quantity: ")
                    print("Updated Sucessfully!")
                else:
                    print("Invalid option!")
            else:
                print("Invalid product number!")
    elif choice == 4:
        if not products:
            print("No products available to delete!")
        else:
            for index, product in enumerate(products):
                print(index+1,".",product["name"],"-",product["price"],"-",product["quantity"])
            delete_index = int(input("Choose an option to Delete: "))-1
            if 0<=delete_index<len(products):
                deleted_product = products.pop(delete_index)
                print("--------------------")
                print(deleted_product["name"],"- Deleted successfully!")
                print("--------------------")
            else:
                print("Invalid product number!")
    elif choice == 5:
        search_name = input("Enter product name: ")
        found=False
        for product in products:
            if product["name"].lower()== search_name.lower():
                print("Product found!")
                print("Name:", product["name"])
                print("Price: ₹", product["price"])
                print("Quantity:", product["quantity"])
                found = True
                break
        if not found:
            print("Product not found!")
    elif choice == 6:
        if not products:
            print("No products available!")
        else:
            total = 0
            while True:
                print("\n===== PRODUCT LIST =====")

                for index, product in enumerate(products):
                    print(index + 1, product["name"],
                          "- ₹", product["price"],
                          "- Stock:", product["quantity"])
                product_number = int(input("Enter product number (0 to finish): "))
                if product_number == 0:
                    break
                product_index = product_number - 1
                if 0 <= product_index < len(products):
                    product = products[product_index]
                    quantity = int(input("Enter quantity: "))
                    if 0 < quantity <= product["quantity"]:
                        amount = product["price"] * quantity
                        total += amount
                        product["quantity"] -= quantity
                        print(product["name"], "x", quantity, "= ₹", amount)
                    else:
                        print("Invalid quantity or insufficient stock!")
                else:
                    print("Invalid product number!")

            print("\n===== FINAL BILL =====")
            print("Total Amount: ₹", total)
            print("Thank you for shopping!")


    elif choice == 8:
        print("Thank you for using Mini Shop!")
        break

    else:
        print("This feature is coming soon!")
