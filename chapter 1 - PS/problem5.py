# 5. Label the program written in problem 4 with comments. import os
import os

# Select the directory whose content you want to list 
directory = '/'

# use the os module to list the directory content
entries = os.listdir(directory)

# print the contents of the directory
for entry in entries:
    print(entry)
