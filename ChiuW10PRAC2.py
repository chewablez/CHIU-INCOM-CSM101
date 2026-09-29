ChiuName = input("Enter your name: ").title()
ChiuJob = input("Enter Job Position (Janitor, Clerk, Cashier, or Manager): ").title()
ChiuHours = int(input("Enter Hours Worked: "))

ChiuJanitor = 20000
ChiuClerk = 25000
ChiuCashier = 28000
ChiuManager = 45000
ChiuTotalHours = 48
ChiuAbsentHours = 48 - ChiuHours
ChiuOvertimeHours = ChiuHours - 48
ChiuJWS = ChiuJanitor / 4
ChiuCLWS = ChiuClerk / 4
ChiuCHWS = ChiuCashier / 4
ChiuMWS = ChiuManager / 4
ChiuJA = ChiuJWS * 0.05
ChiuCLA = ChiuCLWS * 0.05
ChiuCHA = ChiuCHWS * 0.05
ChiuMWA = ChiuMWS * 0.05


match ChiuJob:
    case "Janitor":
        ChiuGBS = ChiuJWS + ChiuJA
        ChiuHourlyRate = ChiuGBS / 48
        print("\nEmployee Name: ", ChiuName)
        print("Job Position: ", ChiuJob)
        print("Actual Hours Worked: ", ChiuHours)
        print("Monthly Salary: ", ChiuJanitor)
        print(f"Basic/Gross Weekly Salary: {ChiuGBS:.2f}")
        print(f"Hourly Rate: {ChiuHourlyRate:.2f}")
        if ChiuHours < 48:
            ChiuAbsentDeduction = ChiuAbsentHours * ChiuHourlyRate * 1.10
            ChiuOvertimeHours = 0
            ChiuOvertimePay = 0
            ChiuNMS = ChiuGBS - ChiuAbsentDeduction + ChiuOvertimePay
            print(f"Absent Hours: {ChiuAbsentHours}")
            print(f"Absence Deduction: {ChiuAbsentDeduction:.2f}")
            print(f"Overtime Hours: {ChiuOvertimeHours:}")
            print(f"Overtime Pay: {ChiuOvertimePay:}")
            print(f"Net Weekly Salary: {ChiuNMS:.2f}")
        else:
            ChiuOvertimeRate = ChiuHourlyRate * 1.50
            ChiuOvertimePay = ChiuOvertimeRate * ChiuOvertimeHours
            ChiuAbsentHours = 0
            ChiuAbsentDeduction = 0
            ChiuNMS = ChiuGBS - ChiuAbsentDeduction + ChiuOvertimePay
            print(f"Absent Hours: {ChiuAbsentHours:}")
            print(f"Absence Deduction: {ChiuAbsentDeduction:}")
            print(f"Overtime Hours: {ChiuOvertimeHours:}")
            print(f"Overtime Pay: {ChiuOvertimePay:.2f}")
            print(f"Net Weekly Salary: {ChiuNMS:.2f}")
    case "Clerk":
        ChiuGBS = ChiuCLWS + ChiuCLA
        ChiuHourlyRate = ChiuGBS / 48
        print("\nEmployee Name: ", ChiuName)
        print("Job Position: ", ChiuJob)
        print("Actual Hours Worked: ", ChiuHours)
        print("Monthly Salary: ", ChiuClerk)
        print(f"Basic/Gross Weekly Salary: {ChiuGBS:.2f}")
        print(f"Hourly Rate: {ChiuHourlyRate:.2f}")
        if ChiuHours < 48:
            ChiuAbsentDeduction = ChiuAbsentHours * ChiuHourlyRate * 1.10
            ChiuOvertimeHours = 0
            ChiuOvertimePay = 0
            ChiuNMS = ChiuGBS - ChiuAbsentDeduction + ChiuOvertimePay
            print(f"Absent Hours: {ChiuAbsentHours}")
            print(f"Absence Deduction: {ChiuAbsentDeduction:.2f}")
            print(f"Overtime Hours: {ChiuOvertimeHours:}")
            print(f"Overtime Pay: {ChiuOvertimePay:}")
            print(f"Net Weekly Salary: {ChiuNMS:.2f}")
        else:
            ChiuOvertimeRate = ChiuHourlyRate * 1.50
            ChiuOvertimePay = ChiuOvertimeRate * ChiuOvertimeHours
            ChiuAbsentHours = 0
            ChiuAbsentDeduction = 0
            ChiuNMS = ChiuGBS - ChiuAbsentDeduction + ChiuOvertimePay
            print(f"Absent Hours: {ChiuAbsentHours:}")
            print(f"Absence Deduction: {ChiuAbsentDeduction:}")
            print(f"Overtime Hours: {ChiuOvertimeHours:}")
            print(f"Overtime Pay: {ChiuOvertimePay:.2f}")
            print(f"Net Weekly Salary: {ChiuNMS:.2f}")
    case "Cashier":
        ChiuGBS = ChiuCHWS + ChiuCHA
        ChiuHourlyRate = ChiuGBS / 48
        print("\nEmployee Name: ", ChiuName)
        print("Job Position: ", ChiuJob)
        print("Actual Hours Worked: ", ChiuHours)
        print("Monthly Salary: ", ChiuCashier)
        print(f"Basic/Gross Weekly Salary: {ChiuGBS:.2f}")
        print(f"Hourly Rate: {ChiuHourlyRate:.2f}")
        if ChiuHours < 48:
            ChiuAbsentDeduction = ChiuAbsentHours * ChiuHourlyRate * 1.10
            ChiuOvertimeHours = 0
            ChiuOvertimePay = 0
            ChiuNMS = ChiuGBS - ChiuAbsentDeduction + ChiuOvertimePay
            print(f"Absent Hours: {ChiuAbsentHours}")
            print(f"Absence Deduction: {ChiuAbsentDeduction:.2f}")
            print(f"Overtime Hours: {ChiuOvertimeHours:}")
            print(f"Overtime Pay: {ChiuOvertimePay:}")
            print(f"Net Weekly Salary: {ChiuNMS:.2f}")
        else:
            ChiuOvertimeRate = ChiuHourlyRate * 1.50
            ChiuOvertimePay = ChiuOvertimeRate * ChiuOvertimeHours
            ChiuAbsentHours = 0
            ChiuAbsentDeduction = 0
            ChiuNMS = ChiuGBS - ChiuAbsentDeduction + ChiuOvertimePay
            print(f"Absent Hours: {ChiuAbsentHours:}")
            print(f"Absence Deduction: {ChiuAbsentDeduction:}")
            print(f"Overtime Hours: {ChiuOvertimeHours:}")
            print(f"Overtime Pay: {ChiuOvertimePay:.2f}")
            print(f"Net Weekly Salary: {ChiuNMS:.2f}")
    case "Manager":
        ChiuGBS = ChiuMWS + ChiuMWA
        ChiuHourlyRate = ChiuGBS / 48
        print("\nEmployee Name: ", ChiuName)
        print("Job Position: ", ChiuJob)
        print("Actual Hours Worked: ", ChiuHours)
        print("Monthly Salary: ", ChiuManager)
        print(f"Basic/Gross Weekly Salary: {ChiuGBS:.2f}")
        print(f"Hourly Rate: {ChiuHourlyRate:.2f}")
        if ChiuHours < 48:
            ChiuAbsentDeduction = ChiuAbsentHours * ChiuHourlyRate * 1.10
            ChiuOvertimeHours = 0
            ChiuOvertimePay = 0
            ChiuNMS = ChiuGBS - ChiuAbsentDeduction + ChiuOvertimePay
            print(f"Absent Hours: {ChiuAbsentHours}")
            print(f"Absence Deduction: {ChiuAbsentDeduction:.2f}")
            print(f"Overtime Hours: {ChiuOvertimeHours:}")
            print(f"Overtime Pay: {ChiuOvertimePay:}")
            print(f"Net Weekly Salary: {ChiuNMS:.2f}")
        else:
            ChiuOvertimeRate = ChiuHourlyRate * 1.50
            ChiuOvertimePay = ChiuOvertimeRate * ChiuOvertimeHours
            ChiuAbsentHours = 0
            ChiuAbsentDeduction = 0
            ChiuNMS = ChiuGBS - ChiuAbsentDeduction + ChiuOvertimePay
            print(f"Absent Hours: {ChiuAbsentHours:}")
            print(f"Absence Deduction: {ChiuAbsentDeduction:}")
            print(f"Overtime Hours: {ChiuOvertimeHours:}")
            print(f"Overtime Pay: {ChiuOvertimePay:.2f}")
            print(f"Net Weekly Salary: {ChiuNMS:.2f}")
    case _:
        print("Invalid Position")










