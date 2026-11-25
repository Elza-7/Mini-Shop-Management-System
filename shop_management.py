print("==============================")
print(" MINI SHOP MANAGEMENT SYSTEM")
print("==============================")

products=[]
name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter product quantity: "))
products.append({
    "name": name,
    "price": price,
    "quantity": quantity
})

print("Product added successfully!")

print("1. Add Product")
print("2. View Products")
print("3. Update Product")
print("4. Delete Product")
print("5. Search Product")
print("6. Generate Bill")
print("7. Sales Report")
print("8. Exit")
print("\n===== PRODUCT LIST =====")

for product in products:
    print("Name:", product["name"])
    print("Price: ₹", product["price"])
    print("Quantity:", product["quantity"])
    print("--------------------")
