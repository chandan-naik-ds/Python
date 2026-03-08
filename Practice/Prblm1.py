from pprint import pprint
'''Your Task
Write a Python program that:
Removes all non-digit characters
Extracts the last 10 digits
Returns a clean list of phone numbers
Expected output:
['9876543210',
 '9876543210',
 '9876543210',
 '9876543210',
 '9876543210',
 '9876543210']'''


phones = [
    "+91-9876543210",
    "987 654 3210",
    "(91) 98765-43210",
    "91 9876543210",
    "9876543210",
    "+91 98765 43210"
]


new_list =  [''.join (ch for ch in phone if ch.isdigit())[-10:] for phone in phones ]

pprint(new_list)