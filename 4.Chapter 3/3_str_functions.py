name = "Chandan naik"

print(len(name))

print(name.endswith("dan"))

print(name.startswith("Cha")) #case sensitive

print(name.capitalize())

print(name.upper())

print(name.lower())

print(name.title())

print(name.strip())

print(name.replace("Chandan","chandu"))

print(name.find("n"))

print(name.count("n"))

print(name.split())  #splits string into list

print("-".join(name))

print(name.isalpha())

print(name.isnumeric())

print(name.isnumeric())

print(name.isdigit())

print(name.isalnum)

print(name.swapcase())

print(name.isspace())

print(name.center(3,"-"))

name = "Chandan"
print("Hello, {}".format(name))   # Using format()
print(f"Hello, {name}")           # Using f-string