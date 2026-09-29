# Pizza Pricing Inquiry System

ChiuFlavor = input("Enter pizza flavor (Hawaiian/Pepperoni/Cheese): ").lower()

match ChiuFlavor:
    case "hawaiian":
        print("You Selected Hawaiian")

        ChiuSize = input("\nEnter size (Small/Medium/Large): ").lower()

        if ChiuSize == "small":
            ChiuPrice = 250
        elif ChiuSize == "medium":
            ChiuPrice = 350
        elif ChiuSize == "large":
            ChiuPrice = 450
        else:
            price = 0
            print("Invalid Size")

    case "pepperoni":
        print("You Selected Pepperoni")

        ChiuSize = input("\nEnter size (Small/Medium/Large): ").lower()

        if ChiuSize == "small":
            ChiuPrice = 350
        elif ChiuSize == "medium":
            ChiuPrice = 550
        elif ChiuSize == "large":
            ChiuPrice = 1000
        else:
            price = 0
            print("Invalid Size")

    case "cheese":
        print("You Selected Cheese")

        ChiuSize = input("\nEnter size (Small/Medium/Large): ").lower()

        if ChiuSize == "small":
            ChiuPrice = 200
        elif ChiuSize == "medium":
            ChiuPrice = 400
        elif ChiuSize == "large":
            ChiuPrice = 550
        else:
            ChiuPrice = 0
            print("Invalid Size")

    case _:
        ChiuPrice = 0
        print("Invalid pizza flavor.")
if ChiuPrice > 0:
    print("Pizza Price: ",ChiuPrice)


