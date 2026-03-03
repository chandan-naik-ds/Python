'''Given prices = [10.5, 20.0, 15.75, 8.99, 25.0], use slicing + a
comprehension to create a list of strings formatted as 
"Item X: ₹{price:.2f}" for every second item starting from index 1
 (i.e., indices 1,3,...).'''

prices = [10.5, 20.0, 15.75, 8.99, 25.0]

result = [
    f"Item {i}: ₹{price:.2f}"
    for i, price in enumerate(prices[1::2], start=1)
]

print(result)