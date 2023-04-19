# Specify the path of the text file
file_path = 'txt/contact_names.txt'  # Replace with your input file path

# Open the text file in read mode
with open(file_path, 'r') as file:
    # Read all lines from the file into a list
    lines = file.readlines()

# Remove newline characters from each line in the list
lines = [line.strip() for line in lines]

# Print the list of lines from the text file
print("List of lines from the text file:")
print(lines)
