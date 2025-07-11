class Employee:
    language = "Py" # This is a class attribute
    salary = 1200000


harry = Employee()
harry.language = "JavaScript" # this is an instance attribute
print(harry.language, harry.salary)

# instance attributes takes over class attributes