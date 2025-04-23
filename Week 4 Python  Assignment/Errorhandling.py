# Ask the user for the filename
filename = input("Enter the name of the file to read: ")

try:
    # Attempt to open and read the file
    with open(filename, 'r') as file:
        data = file.read()
        print(data)
     #Error handling for file not found
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
finally:
    file.close()