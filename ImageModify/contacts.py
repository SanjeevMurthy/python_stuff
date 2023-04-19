import vobject

# Specify the path of the .vcf file
vcf_file_path = "txt/new_contacts.vcf"  # Replace with your .vcf file path

# Load the .vcf file
with open(vcf_file_path, 'r') as file:
    vcard_data = file.read()

# Parse the .vcf file
vcards = vobject.readComponents(vcard_data)

# Extract contact names from the .vcf file
contact_names = []
for vcard in vcards:
    if 'fn' in vcard.contents:
        fn = vcard.fn.value
        contact_names.append(fn)

# Print the contact names
print("Contact names from the .vcf file:")
for name in contact_names:
    print(name)
with open("txt/new_contact_names.txt", 'w') as file:
    # Write each string from the list to a new line in the text file
    for string in contact_names:
        file.write(string + '\n')

