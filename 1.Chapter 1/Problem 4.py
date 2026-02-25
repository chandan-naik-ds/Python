import os

# Specify the path of the directory
directory_path = '/'  # '.' means current directory

# Check if the path is a valid directory
if os.path.isdir(directory_path):
    print(f"Contents of directory '{directory_path}':")
    for item in os.listdir(directory_path):
        print(item)
else:
    print(f"The path '{directory_path}' is not a valid directory.")
