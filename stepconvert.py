# Read the JavaScript-like object from the export.js file
with open('export.js', 'r') as file:
    javascript_object = file.read()

# Define the start and end markers
start_marker = '//---START---//'
end_marker = '//---END---//'

# Split the JavaScript object into sections using the end marker
sections = javascript_object.split(end_marker)

# Initialize a list to store JavaScript objects
javascript_objects = []

# Process each section
for section in sections:
    # Find the start marker in the section
    start_index = section.find(start_marker)
    if start_index != -1:
        # Extract the content between the markers
        content_between_markers = section[start_index + len(start_marker):].strip()

        # Remove leading whitespace and split lines
        lines = content_between_markers.split('\n')

        # Create a JavaScript object with the extracted content
        js_object = "export default {\n"
        for line in lines:
            key, value = map(str.strip, line.split(':', 1))
            js_object += f'  {key}: \'{value}\',\n'
        js_object += '}'

        # Add the JavaScript object to the list
        javascript_objects.append(js_object)

# Print and write each JavaScript object to separate files
for i, js_object in enumerate(javascript_objects):
    print(f"JavaScript Object {i + 1}:")
    print(js_object)

    # Write the JavaScript object to separate files (en1.js, en2.js, ...)
    with open(f'en{i + 1}.js', 'w') as export_file:
        export_file.write(js_object)

print(f"Found {len(javascript_objects)} instances of the markers.")

