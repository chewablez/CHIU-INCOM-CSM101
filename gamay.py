n, j, h = input("Name: ").title(), input("Job: ").title(), int(input("Hours: "))
s = {"Janitor": 20000, "Clerk": 25000, "Cashier": 28000, "Manager": 45000}.get(j)
if not s: print("Invalid Position")
else:
    g, a, o = (s / 4) * 1.05, max(0, 48 - h), max(0, h - 48)
    print(f"\nEmp: {n}\nJob: {j}\nHrs: {h}\nMon: {s}\nGross Wk: {g:.2f}\nRate: {g/48:.2f}\nAbs Hrs: {a}\nDed: {a*(g/48)*1.1:.2f}\nOT Hrs: {o}\nOT Pay: {o*(g/48)*1.5:.2f}\nNet Wk: {g - a*(g/48)*1.1 + o*(g/48)*1.5:.2f}")