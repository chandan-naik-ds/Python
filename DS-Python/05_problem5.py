# Create a list containing cubes of numbers that are divisible by 3.

nums = [5, 12, 7, 18, 3, 20, 9]

new_list = [i*i*i for  i in nums if i % 3==0]

print(new_list)