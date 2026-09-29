while True:
    ChiuName = input("Enter your name: ").title()
    ChiuJob = input("Enter Job Position (Janitor, Clerk, Cashier, or Manager): ").title()


    ChiuJanitor = 18000
    ChiuClerk = 22000
    ChiuCashier = 24000
    ChiuManager = 40000
    ChiuTotalHours = 88


    ChiuJBHMS = ChiuJanitor / 2
    ChiuCLBHMS = ChiuClerk / 2
    ChiuCHBHMS = ChiuCashier / 2
    ChiuMBHMS = ChiuManager / 2



    match ChiuJob:
            case "Janitor":
                ChiuHours = int(input("Enter Hours Worked: "))
                ChiuAbsentHours = 88 - ChiuHours
                ChiuOvertimeHours = ChiuHours - 88
                ChiuHourlyRate = ChiuJBHMS / 88
                print("\nEmployee Name: ", ChiuName)
                print("Job Position: ", ChiuJob)
                print("Actual Hours Worked: ", ChiuHours)
                print("Monthly Salary: ", ChiuJanitor)
                print(f"Basic/Gross Half-Month Salary: {ChiuJBHMS:.2f}")
                print(f"Hourly Rate: {ChiuHourlyRate:.2f}")
                if ChiuHours < 88:
                    ChiuAbsentDeduction = ChiuAbsentHours * ChiuHourlyRate
                    ChiuOvertimeHours = 0
                    ChiuOvertimePay = 0
                    ChiuNMS = ChiuJBHMS - ChiuAbsentDeduction + ChiuOvertimePay
                    print(f"Absent Hours: {ChiuAbsentHours}")
                    print(f"Absence Deduction: {ChiuAbsentDeduction:.2f}")
                    print(f"Overtime Hours: {ChiuOvertimeHours:}")
                    print(f"Overtime Pay: {ChiuOvertimePay:}")
                    print(f"Net Half-Month Salary: {ChiuNMS:.2f}")
                else:
                    ChiuOvertimeRate = ChiuHourlyRate * 1.25
                    ChiuOvertimePay = ChiuOvertimeRate * ChiuOvertimeHours
                    ChiuAbsentHours = 0
                    ChiuAbsentDeduction = 0
                    ChiuNMS = ChiuJBHMS - ChiuAbsentDeduction + ChiuOvertimePay
                    print(f"Absent Hours: {ChiuAbsentHours:}")
                    print(f"Absence Deduction: {ChiuAbsentDeduction:}")
                    print(f"Overtime Hours: {ChiuOvertimeHours:}")
                    print(f"Overtime Pay: {ChiuOvertimePay:.2f}")
                    print(f"Net Half-Month Salary: {ChiuNMS:.2f}")
            case "Clerk":
                ChiuHours = int(input("Enter Hours Worked: "))
                ChiuAbsentHours = 88 - ChiuHours
                ChiuOvertimeHours = ChiuHours - 88
                ChiuHourlyRate = ChiuCLBHMS / 88
                print("\nEmployee Name: ", ChiuName)
                print("Job Position: ", ChiuJob)
                print("Actual Hours Worked: ", ChiuHours)
                print("Monthly Salary: ", ChiuJanitor)
                print(f"Basic/Gross Half-Month Salary: {ChiuCLBHMS:.2f}")
                print(f"Hourly Rate: {ChiuHourlyRate:.2f}")
                if ChiuHours < 88:
                    ChiuAbsentDeduction = ChiuAbsentHours * ChiuHourlyRate
                    ChiuOvertimeHours = 0
                    ChiuOvertimePay = 0
                    ChiuNMS = ChiuCLBHMS - ChiuAbsentDeduction + ChiuOvertimePay
                    print(f"Absent Hours: {ChiuAbsentHours}")
                    print(f"Absence Deduction: {ChiuAbsentDeduction:.2f}")
                    print(f"Overtime Hours: {ChiuOvertimeHours:}")
                    print(f"Overtime Pay: {ChiuOvertimePay:}")
                    print(f"Net Half-Month Salary: {ChiuNMS:.2f}")
                else:
                    ChiuOvertimeRate = ChiuHourlyRate * 1.25
                    ChiuOvertimePay = ChiuOvertimeRate * ChiuOvertimeHours
                    ChiuAbsentHours = 0
                    ChiuAbsentDeduction = 0
                    ChiuNMS = ChiuCLBHMS - ChiuAbsentDeduction + ChiuOvertimePay
                    print(f"Absent Hours: {ChiuAbsentHours:}")
                    print(f"Absence Deduction: {ChiuAbsentDeduction:}")
                    print(f"Overtime Hours: {ChiuOvertimeHours:}")
                    print(f"Overtime Pay: {ChiuOvertimePay:.2f}")
                    print(f"Net Half-Month Salary: {ChiuNMS:.2f}")
            case "Cashier":
                ChiuHours = int(input("Enter Hours Worked: "))
                ChiuAbsentHours = 88 - ChiuHours
                ChiuOvertimeHours = ChiuHours - 88
                ChiuHourlyRate = ChiuCHBHMS / 88
                print("\nEmployee Name: ", ChiuName)
                print("Job Position: ", ChiuJob)
                print("Actual Hours Worked: ", ChiuHours)
                print("Monthly Salary: ", ChiuJanitor)
                print(f"Basic/Gross Half-Month Salary: {ChiuCHBHMS:.2f}")
                print(f"Hourly Rate: {ChiuHourlyRate:.2f}")
                if ChiuHours < 88:
                    ChiuAbsentDeduction = ChiuAbsentHours * ChiuHourlyRate
                    ChiuOvertimeHours = 0
                    ChiuOvertimePay = 0
                    ChiuNMS = ChiuCHBHMS - ChiuAbsentDeduction + ChiuOvertimePay
                    print(f"Absent Hours: {ChiuAbsentHours}")
                    print(f"Absence Deduction: {ChiuAbsentDeduction:.2f}")
                    print(f"Overtime Hours: {ChiuOvertimeHours:}")
                    print(f"Overtime Pay: {ChiuOvertimePay:}")
                    print(f"Net Half-Month Salary: {ChiuNMS:.2f}")
                else:
                    ChiuOvertimeRate = ChiuHourlyRate * 1.25
                    ChiuOvertimePay = ChiuOvertimeRate * ChiuOvertimeHours
                    ChiuAbsentHours = 0
                    ChiuAbsentDeduction = 0
                    ChiuNMS = ChiuJBHMS - ChiuAbsentDeduction + ChiuOvertimePay
                    print(f"Absent Hours: {ChiuAbsentHours:}")
                    print(f"Absence Deduction: {ChiuAbsentDeduction:}")
                    print(f"Overtime Hours: {ChiuOvertimeHours:}")
                    print(f"Overtime Pay: {ChiuOvertimePay:.2f}")
                    print(f"Net Half-Month Salary: {ChiuNMS:.2f}")
            case "Manager":
                ChiuHours = int(input("Enter Hours Worked: "))
                ChiuAbsentHours = 88 - ChiuHours
                ChiuOvertimeHours = ChiuHours - 88
                ChiuHourlyRate = ChiuMBHMS / 88
                print("\nEmployee Name: ", ChiuName)
                print("Job Position: ", ChiuJob)
                print("Actual Hours Worked: ", ChiuHours)
                print("Monthly Salary: ", ChiuJanitor)
                print(f"Basic/Gross Half-Month Salary: {ChiuMBHMS:.2f}")
                print(f"Hourly Rate: {ChiuHourlyRate:.2f}")
                if ChiuHours < 88:
                    ChiuAbsentDeduction = ChiuAbsentHours * ChiuHourlyRate
                    ChiuOvertimeHours = 0
                    ChiuOvertimePay = 0
                    ChiuNMS = ChiuMBHMS - ChiuAbsentDeduction + ChiuOvertimePay
                    print(f"Absent Hours: {ChiuAbsentHours}")
                    print(f"Absence Deduction: {ChiuAbsentDeduction:.2f}")
                    print(f"Overtime Hours: {ChiuOvertimeHours:}")
                    print(f"Overtime Pay: {ChiuOvertimePay:}")
                    print(f"Net Half-Month Salary: {ChiuNMS:.2f}")
                else:
                    ChiuOvertimeRate = ChiuHourlyRate * 1.25
                    ChiuOvertimePay = ChiuOvertimeRate * ChiuOvertimeHours
                    ChiuAbsentHours = 0
                    ChiuAbsentDeduction = 0
                    ChiuNMS = ChiuMBHMS - ChiuAbsentDeduction + ChiuOvertimePay
                    print(f"Absent Hours: {ChiuAbsentHours:}")
                    print(f"Absence Deduction: {ChiuAbsentDeduction:}")
                    print(f"Overtime Hours: {ChiuOvertimeHours:}")
                    print(f"Overtime Pay: {ChiuOvertimePay:.2f}")
                    print(f"Net Half-Month Salary: {ChiuNMS:.2f}")
            case _:
                print("Invalid Position")

    again = input("\nDo you want to enter again? (Y/N): ").upper()

    if again.upper() != "Y":
        print("Thank you!")
        break









