#Seconds Converter
#Converts Inputted Seconds into Minutes, Hours, Days, Weeks, Months, and Years.

ChiuSeconds = float(input("Input Amount of Seconds you want to Convert: "))

ChiuMinutes = ChiuSeconds / 60
ChiuHours = ChiuSeconds / 3600
ChiuDays = ChiuSeconds / 86400
ChiuWeeks = ChiuSeconds / 604800
ChiuMonths = ChiuSeconds / 2628000
ChiuYears = ChiuSeconds / 31540000

print("-------------------------------")
print(f"Seconds: {ChiuSeconds:.2f}")
print("-------------------------------")
print(f"Minutes: {ChiuMinutes:.2f}")
print("Hours: ",ChiuHours)
print("Days: ",ChiuDays)
print("Weeks: ",ChiuWeeks)
print("Months: ",ChiuMonths)
print("Years: ",ChiuYears)



