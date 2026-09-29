people = {
    "Carl": 85,
    "Arcl": 90,
    "Ralc": 78,
    "Larc": 95
}
print("STUDENT GRADES")


people["Osas"] = 88
people["Carl"] = 89
people["Arcl"] = 91

name1 = input("Enter Student Name: ")
grade1 = int(input("Enter Student Grade: "))
people[name1] = grade1
print(people)

for name, grade in people.items():
    print(name, ":", grade)

search = input("\nEnter Student Name to search: ")
if search in people:
    print(search, "has a grade of", people[search])
else:
    print("Student not found.")