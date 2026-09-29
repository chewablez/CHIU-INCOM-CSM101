ChiuName = input("Enter Name: ")
ChiuMonth = int(input("Input Month Number (1-12): "))
ChiuNameTitle = ChiuName.title()
print(f"\nName: {ChiuNameTitle}\nSelected Month: {ChiuMonth}")
if ChiuMonth <= 3 and ChiuMonth >= 1:
    print(f"\nTravel Season:\nRainy = Not a good month to travel due to flooding in many areas.")
elif ChiuMonth >= 4 and ChiuMonth <= 5:
    print(f"\nTravel Season:\nSummer = A good time to travel.")
elif ChiuMonth >= 6 and ChiuMonth <= 8:
    print(f"\nTravel Season:\nMixed Weather Condition = Typhoon may come and the country may experience typhoon in good weather.")
elif ChiuMonth >= 9 and ChiuMonth <= 12:
    print(f"\nTravel Season:\nChristmas Vibe = Still a mixed weather but mostly sunny and cold breeze. Stores & Tourist Destinations offer a lot of discounts.")
else:
    print("\nInvalid Month Number. Please Input 1-12.")

