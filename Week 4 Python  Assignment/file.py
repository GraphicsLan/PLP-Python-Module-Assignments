# Reading a txt file called aboutme.txt
with open('aboutme.txt', 'r') as file:
    data = file.read()
    print(data)
# mofifying data to uppercase)
modified_data = data.upper()

# Write the modified content to a new file
with open('modified_aboutme.txt', 'w') as new_file:
    new_file.write(modified_data)

print("Modified content has been written to 'modified_aboutme.txt'.")
