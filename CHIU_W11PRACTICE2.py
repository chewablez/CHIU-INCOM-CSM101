months = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Satudary", "Sunday")

for x in months:
    print(x)

print("\n")

for i in days:
    print(i)

MachineLearning = [('Supervised', 'Decision Tree'),
                   ('Supervised', 'Random Forest'),
                   ('Unsupervised', 'K-Means'),
                   ('Unsupervised', 'Gawssian Mixture Model')
                   ]
print("\n\nLearning Type:", MachineLearning[0][0])
for item in MachineLearning:
    if item[0] == "Supervised":
        print(item[1])


print("\nLearning Type:", MachineLearning[2][0])
for t in MachineLearning:
    if t[0] == "Unsupervised":
        print(t[1])
