# Take items at odd indices and format as:
# "Product {X}: <item>"


items = ["Pen", "Book", "Laptop", "Mouse", "Keyboard"]

new_items = [f"Product {i}: <item>"
            for i, item in enumerate(items)
            if i%2 != 0
             ]

print(new_items)