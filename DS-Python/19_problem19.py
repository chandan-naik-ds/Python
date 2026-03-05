# Create a dictionary where:
# key   = department
# value = average salary of that department


employees = [
("Alice", "HR", 50000),
("Bob", "Engineering", 90000),
("Charlie", "HR", 60000),
("David", "Finance", 75000),
("Eve", "Engineering", 95000),
("Frank", "Finance", 80000)
]

result = {
    dept: sum(s for _, d, s in employees if d == dept) /
          len([1 for _, d, _ in employees if d == dept])
          for dept in (d for _, d,_ in employees)
}

print(result)