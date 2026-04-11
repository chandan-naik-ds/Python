number = input("Enter a multi-digit number: ")

# Initialize frequency counter
freq = [0] * 10

# Count frequency of each digit
for ch in number:
    if ch.isdigit():
        freq[int(ch)] += 1

# Print the result
print("Digit : Frequency")
for digit in range(10):
    print(f"{digit} : {freq[digit]}")