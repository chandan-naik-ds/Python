all = ["Apple","Rohan", 23, 345.77, "Ramesh"]

# 1.append
all.append("Ravi")
print(all)

num = [1,34,87,859,46,92,57]
# 2.sort
num.sort()
print(num)

# 3.reverse
num.reverse()
print(num)

# 4.insert
num.insert(3,8)
print(num) # 8 is inserted at 3rd index

# pop
num.pop(2)
print(num)

#remove
num.remove(859)
print(num)

#clear
num1= [1,34,87,859,46,92,57]
num1.clear()
print(num1)

# Extend
num2 = [1,34,87,859,46,92,57]
num2.extend(num)  #All the elements of the num lists added to the num2 list
print(num2)

num2.extend([3,4,5,6,7])
print(num2)