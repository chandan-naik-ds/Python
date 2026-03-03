''''Given sales = [120, 340, 89, 560, 210, 45, 780, 320, 150, 900],create a new 
list high_sales containing only values > 300, but squared (i.e., value ** 2).
Use a single list comprehension '''

sales = [120, 340, 89, 560, 210, 45, 780, 320, 150, 900]

high_list = [i*i for i in sales if i > 300]

print(list(high_list))