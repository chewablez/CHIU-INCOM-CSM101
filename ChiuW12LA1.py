Chiu_Classrecord = {"Clark": {"StudID": "S001", "Grade": [90,85,86,82,93,59,97]},
                    "Cark": {"StudID": "S002", "Grade": [91,86,87,83,94,95,98]}}

search = input("Enter a student name to search: ").title()
found = False
for name, info in Chiu_Classrecord.items():
    if name == search:
        id = info['StudID']
        grades = info['Grade']
        print("Student Found!",name)
        print(f"Student ID: {id}")
        print(f"Grades: {grades}")
        avg = sum(grades) / len(grades)
        print(f"Average: {avg:.2f}")
        print(f"Highest Grade: {max(grades)}")
        print(f"Lowest: {min(grades)}")
        for g in grades:
            if g < 60:
                print(f"{name} has a Grade below 60. Canditate for Intervention!")
        found = True
        break
if not found:
    print("Student not Found")






