l = [34, 45, 23, 678]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

# This can be simplified by suing enumerate function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")