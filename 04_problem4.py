# 4. Write a program to filter a list of numbers which are divisible by 5. 

def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1, 2, 3434, 5656, 34355533, 974238, 54235, 5443295, 53243446]

f = list(filter(divisible5, a))
print(f)