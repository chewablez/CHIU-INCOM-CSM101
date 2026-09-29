while True:
    name = input("Enter Name: ")
    print("Hello, ",name)


    again = input("Do you want to enter again? (Y/N): ")

    if again.upper() != "Y":
        print("Program ended.")
        break