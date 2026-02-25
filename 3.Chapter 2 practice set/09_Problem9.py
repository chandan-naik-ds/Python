# Assign one variable to another and prove (using id()) whether they point to the same memory location.

call = 100

sent = call

print(id(call))
print(id(sent))
