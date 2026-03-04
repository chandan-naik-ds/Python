'''Given employees = [("Alice", 28, "HR"), ("Bob", 34, "Engineering"), ("Charlie", 25, "HR"), 
("David", 41, "Finance"), ("Eve", 30, "Engineering")], create a dictionary where 
key = department, value = list of names sorted alphabetically.
Use dict comprehension + grouping logic.'''


employees = [("Alice", 28, "HR"), ("Bob", 34, "Engineering"), ("Charlie", 25, "HR"), 
             ("David", 41, "Finance"), ("Eve", 30, "Engineering")]

result = {
    dept : sorted([name for name, age , d in employees if d == dept])
    for dept in {dept for _, _, dept in employees}
}