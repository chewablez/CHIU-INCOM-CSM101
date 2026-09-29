students = {
    "Ana": [90,85,83],
    "Kirk": [87,76,91],
    "Liza": [69,68,67]
}
highest = 100
namehighest = ""
tally = 0

for name,grade in students.items():
    average = sum(grade) / len(grade)
    print(name, *grade, f"Average: {average:.2f}")
    if average < highest:
        highest = average
        namehighest = name
    for g in grade:
        if g > 75:
            tally = tally + 1

print(f"Student {namehighest} got the lowest average: {highest}")
print(f"There are {tally} grades which are above 75.")