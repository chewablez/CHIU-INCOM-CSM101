patients = {
    "Ana": [80,50,150,90,140,170,1000],
    "Kirk": [130,140,135,90,140,200,230],
    "Liza": [90,100,95,90,140,210,220]
}

for name,reading in patients.items():
    tally = 0
    highestreading = 0
    print("\nPatient: ",name)
    print("==== BLOOD SUGAR SUMMARY ====")
    for item in reading:
        avg = sum(reading) / len(reading)
        diff = max(reading) - min(reading)
        if item > 120:
            print(f"{item}: High")
            tally = tally + 1
            highestreading = item
        else:
            print(f"{item}: Normal")
    print("=============================")
    print(f"Highest Reading: {highestreading}")
    print(f"Number of High Readings {tally}")
    print("Lowest Reading: ",min(reading))
    print("Higest Reading: ", max(reading))
    print(f"Average: {avg:.2f}")
    print("Difference: ",diff)










