# Pizza Pricing Inquiry System
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




# ChiuFlavor = input("Enter pizza flavor (Hawaiian/Pepperoni/Cheese): ").lower()
# if ChiuFlavor == "hawaiian":
#     print("You Selected Hawaiian")
#
#     ChiuSize = input("\nEnter size (Small/Medium/Large): ").lower()
#
#     if ChiuSize == "small":
#         ChiuPrice = 250
#     elif ChiuSize == "medium":
#         ChiuPrice = 350
#     elif ChiuSize == "large":
#         ChiuPrice = 450
#     else:
#
#         price = 0
#         print("Invalid Size")
#
# elif ChiuFlavor == "pepperoni":
#     print("You Selected Pepperoni")
#
#     ChiuSize = input("\nEnter size (Small/Medium/Large): ").lower()
#
#     if ChiuSize == "small":
#         ChiuPrice = 350
#     elif ChiuSize == "medium":
#         ChiuPrice = 550
#     elif ChiuSize == "large":
#         ChiuPrice = 1000
#     else:
#         price = 0
#         print("Invalid Size")
#
# elif ChiuFlavor == "cheese":
#     print("You Selected Cheese")
#
#     ChiuSize = input("\nEnter size (Small/Medium/Large): ").lower()
#
#     if ChiuSize == "small":
#         ChiuPrice = 200
#     elif ChiuSize == "medium":
#         ChiuPrice = 400
#     elif ChiuSize == "large":
#         ChiuPrice = 550
#     else:
#         ChiuPrice = 0
#         print("Invalid Size")
# else:
#     ChiuPrice = 0
#     print("Invalid pizza flavor.")
# if ChiuPrice > 0:
#     print("Pizza Price: ",ChiuPrice)
#
#
