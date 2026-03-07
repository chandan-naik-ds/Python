'''You have messy phone numbers:
phones = ["+91-9876543210", "987 654 3210", "(91) 98765-43210", "91 9876543210"]
Create a list of clean 10-digit strings (just digits, remove everything else) using 
a comprehension + string methods/slicing.'''

phones = ["+91-9876543210", "987 654 3210", "(91) 98765-43210", "91 9876543210"]

new_list = [''.join (ch for ch in phone if ch.isdigit())[-10:] for phone in phones]

print(new_list)

