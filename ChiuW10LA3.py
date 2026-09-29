school = ["NU", "ADDU", "MMCM", "UM", "UIC", "USEP", "SPC", "DMSF", "DDC", "HCDC", "UPM", "ACD", "PWC", "LPU", "BC", "DCC", "DMMA", "OLFA", "JMC", "CCD", "CCSA"]
while True:
    SearchSchool = input("Search for a University in Davao City: ")


    found = False

    for search in school:
        if search.lower() == SearchSchool.lower():
            found = True
            break

    if found:
        print("University Available")
        code = SearchSchool.upper()
        if SearchSchool.upper() == "NU":
            print("National University of Davao")
        elif SearchSchool.upper() == "ADDU":
            print("Ateneo de Davao University")
        elif code == "MMCM":
            print("Mapua Malayan Colleges Mindanao")
        elif code == "UM":
            print("University of Mindanao")
        elif code == "UIC":
            print("University of the Immaculate Conception")
        elif code == "USEP":
            print("University of Southeastern Philippines")
        elif code == "SPC":
            print("San Pedro College")
        elif code == "DMSF":
            print("Davao Medical School Foundation")
        elif code == "DDC":
            print("Davao Doctors College")
        elif code == "HCDC":
            print("Holy Cross of Davao College")
        elif code == "UPM":
            print("University of the Philippines Mindanao")
        elif code == "ACD":
            print("Assumption College of Davao")
        elif code == "PWC":
            print("Philippine Women's College of Davao")
        elif code == "LPU":
            print("Lyceum of the Philippines University - Davao")
        elif code == "BC":
            print("Brokenshire College")
        elif code == "DCC":
            print("Davao Central College")
        elif code == "DMMA":
            print("DMMA College of Southern Philippines")
        elif code == "OLFA":
            print("Our Lady of Fatima Academy")
        elif code == "JMC":
            print("Jose Maria College")
        elif code == "CCD":
            print("City College of Davao")
        elif code == "CCSA":
            print("Christian Colleges of Southeast Asia")

    else:
        print("University not Available")

    again = input("\nTry Again? (Y/N): ")

    if again.upper() != "Y":
        print("Thank you!")
        break