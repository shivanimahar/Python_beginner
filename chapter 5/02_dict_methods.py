marks = {
    "Harry" : 100,
    "Shubam" : 56,
    "Rohan" : 23,
    0: "Harry"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry": 99, "Renu": 100})
# print(marks)

print(marks.get("Harry2")) # Prints None
print(marks["Harry2"]) # Returns an error