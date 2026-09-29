from MamicpicW11LA2 import students
from PATIENT import highest
from W8CHIU.prac3 import namehighest, average

students = {
    "Ana": [90,85,82],
    "kirk": [90,85,82],
    "Liza": [69,71,83],

}


highest = 0
namehighest = ""
tally = 0
name75 = []

for name , grade in students.items():
    average = sum(grade) / len(grade)
    print(name, * grade, "Average: " , round(average,2))
    if average > highest:
        highest = average
        namehighest = name
    for g in grade:
        if g < 75:
            tally = tally + 1
            name75.append(name)

print()
print("The Average is"), round (highest, 2)
print(f"Congratulations, {namehighest}!")
print(f"There are {tally} grades below 75, Owend by {','.join(name75)}")