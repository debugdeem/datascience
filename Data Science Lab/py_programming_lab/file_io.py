# Write to a file
with open('file.txt', 'w') as f:
    f.write('This is a test to write to a file \nand this is a new line\n')

# Read from a file
with open('file.txt', 'r') as f:
    contents = f.read()

print(contents)
