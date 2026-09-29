students = {}

number = int(input("Enter Number of Students: "))

for i in range(number):
    print("\nStudent:", i + 1)

    name = input("Enter a Student Name: ")

    grade1 = float(input("Enter Grade 1: "))
    grade2 = float(input("Enter Grade 2: "))
    grade3 = float(input("Enter Grade 3: "))

    students[name] = {grade1, grade2, grade3}

print("\n==========STUDENT GRADES==========")


highest = 0
namehighest = ""
tallyhighest = 0
lowest = 100
namelowest = ""
tallylowest = 0

for name,grade in students.items():
    average = sum(grade) / len(grade)

    print(name, *grade, f"Average: {average:.2f}", sep=", ")
    if average > highest:
        highest = average
        namehighest = name
    for g in grade:
        if g > 75:
            tallyhighest = tallyhighest + 1
    if average < lowest:
        lowest = average
        namelowest = name
    for h in grade:
        if g < 75:
            tallylowest = tallylowest + 1


print(f"\nStudent ({namehighest}) got the highest average of: {highest:.2f}")
print(f"There are {tallyhighest} grades which are below 75")

print(f"\nStudent ({namelowest}) got the lowest average of: {lowest:.2f}")
print(f"There are {tallylowest} grades which are above 75")

