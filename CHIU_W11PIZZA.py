pizza = [('Hawaiian', 'Small', 250),
        ('Hawaiian', 'Medium', 350),
        ('Hawaiian', 'Large', 450),
        ('Pepperoni', 'Small', 350),
        ('Pepperoni', 'Medium', 550),
        ('Pepperoni', 'Large', 1000),
        ('Cheese', 'Small', 200),
        ('Cheese', 'Medium', 400),
        ('Cheese', 'Large', 550)]

decision = input("Enter Flavor: ").title()
decisionsize = input("Enter Size: ").title()

found = False

for x in pizza:
    if x[0] == decision and x[1] == decisionsize:
        print("\nPizza Flavor and Size:", decision, decisionsize)
        print(f"Price: {x[2]}")
        found = True
        break
if not found:
        print("Flavor or Size Unavailable")