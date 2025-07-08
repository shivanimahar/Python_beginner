f = open("file.txt")
print(f.read())
f.close()

# The same can be written using (with statement) like this, without the use of f.close():
with open("file.txt") as f:
    print(f.read())

# you dont have to explicitly close the file