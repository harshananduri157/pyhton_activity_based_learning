# Case Study 49: Tuple-Based Product Catalogue Audit
# Heading: Check Product Stock and Calculate Inventory Value

products = [
    ("P101", "Notebook", 45.0, 20),
    ("P102", "Pen", 10.0, 50),
    ("P103", "Bag", 650.0, 4),
    ("P104", "Pencil", 5.0, 0)
]

print("Product Catalogue")
print("-----------------")

total_value = 0

for product in products:
    product_id, name, price, stock = product

    value = price * stock
    total_value += value

    print(f"\nProduct ID: {product_id}")
    print(f"Product Name: {name}")
    print(f"Price: Rs. {price:.2f}")
    print(f"Stock: {stock}")
    print(f"Inventory Value: Rs. {value:.2f}")

    if price < 0 or stock < 0:
        print("Warning: Invalid price or stock.")

    elif stock < 5:
        print("Replenishment required.")

print(f"\nTotal inventory value: Rs. {total_value:.2f}")
