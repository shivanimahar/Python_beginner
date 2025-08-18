# 5. Write a program to find the maximum of the numbers in a list using the reduce function. 

from functools import reduce
l = [1, 2, 3434, 5656, 34355533, 123456789098765, 974238, 54235, 5443295, 53243446]

def greater(a, b):
    if (a>b):
        return a
    return b

print(reduce(greater, l))

 