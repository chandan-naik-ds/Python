# Write a program to fill the name and date in a letter using replace

letter = '''Dear Name
            You are oppointed 
            Date'''

print(letter.replace("Name","Chandan").replace("Date","7th Nov 2025"))

# Write a program to fill the name and date in a letter using replace

letter = '''Dear <|Name|>
            You are oppointed 
            <|Date|>'''

print(letter.replace("<|Name|>","Chandan").replace("<|Date|>","7th Nov 2025"))