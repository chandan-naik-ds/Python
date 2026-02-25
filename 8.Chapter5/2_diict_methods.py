
marks = {
    "Vinayak": 91,
    "Ravi"  : 45,
    "Mahesh" : 34
}

print(marks,type(marks))

print(marks["Vinayak"])

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"Vinayak":90, "Renuka":100})
print(marks)  # The mutability of the dictionary is shown here

print(marks.get("Chandan")) #Prints none
print(marks.get("Vinayak")) 
# print(marks.get["Chandan"]) # Gives  error

# return_value = marks.pop("Vinayak")
# print(return_value) # pop up the the key and returns its value 
# print(marks)

# marks.popitem()
# print(marks)

# marks.clear()
# print(marks)

# marks.copy
# print(marks)

marks.setdefault("vinu",)
print(marks)

