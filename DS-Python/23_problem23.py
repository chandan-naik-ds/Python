'''products = {
"laptop": 80000,
"phone": 40000,
"tablet": 30000,
"monitor": 20000,
"keyboard": 1500
}

Create a new dictionary where

price > 30000 → apply 10% discount
price ≤ 30000 → apply 5% discount

Example output

{
'laptop':72000,
'phone':36000,
'tablet':28500,
'monitor':19000,
'keyboard':1425
}

Constraint:
Use single dictionary comprehension.'''

products = {
"laptop": 80000,
"phone": 40000,
"tablet": 30000,
"monitor": 20000,
"keyboard": 1500
}
new_dict = {
    
    device: price*0.9 if price>30000 else price*0.95
    for device , price in products.items()
}

print(new_dict)