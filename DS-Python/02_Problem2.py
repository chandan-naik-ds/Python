'''You have data = ["apple", "banana", "cherry", "date", "elderberry", "fig"].
Create a new list containing only fruits whose name length is even and starts 
with a vowel (a/e/i/o/u),converted to uppercase.Use one comprehension'''

data = ["apple", "banana", "cherry", "date", "elderberry", "fig"]

result = [fruit.upper() for fruit in data 
          if len(fruit)% 2 == 0 and fruit[0].lower() in "aeiou"]

print(result)
