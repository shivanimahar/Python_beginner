import os

# Specify the directory path
directory = '/New folder'

# Get the list of files and directories in the specified directory
entries = os.listdir(directory)

# Iterate over the entries and print each one
for entry in entries:
    print(entry)
