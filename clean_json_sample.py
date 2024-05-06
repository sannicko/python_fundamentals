import json

# Input and output file paths
input_file = '/Users/sannicko/Downloads/acronyms.json'
output_file = '/Users/sannicko/Downloads/clean.json'

# Read the JSON data
with open(input_file, 'r') as file:
    data = json.load(file)

# Remove the 'Example' key from each entry
for entry in data:
    if 'Example' in entry:
        del entry['Example']

# Write the updated data to the new JSON file or an empty list if no data is present
with open(output_file, 'w') as file:
    json.dump(data, file, indent=4)

print("Updated data has been written to file name :", output_file)
