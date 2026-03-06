'''Nested Sales Aggregation
Dataset
Create dictionary
store → total sales
Expected
{
'store1':3800,
'store2':6000,
'store3':2550
}
Constraint
Use dict comprehension'''

sales = {
"store1": [1200, 1500, 1100],
"store2": [2000, 2100, 1900],
"store3": [800, 900, 850]
}

new_sales = {
    store : sum(amt for amt in sell)
    for store,sell in sales.items()
}

print(new_sales)