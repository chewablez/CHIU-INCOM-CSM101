studentsL = {
    "Ana": [95,82,83],
    "Ben": [100,95,84] }
studentsT = {
    "Ana": [95,82,83],
    "Ben": [100,95,84] }

for name,grade in studentsL.items():
    print(name, *grade)

