myList = [1, 2, 4, 5, 6, 7, 8]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

#This can be done my list comprehension(squaredList)

squaredList = [i*i for i in myList]

print(squaredList)