'''Create a list of:
"APPLE costs ₹50"
But only for items where price > 30.'''

data = [("apple", 50), ("banana", 20), ("mango", 100), ("grapes", 40)]

new_data = [
    f"{item.upper()} costs ₹{price}"
    for item, price in data 
    if price > 30
    
]

print(list(new_data))