def verify_input (input):
    try:
        float(input)
        return True
    except ValueError:
        return False

miles_in_kilometres = 1.60934
miles = input("Enter miles: ")
if verify_input(miles):
    miles = float(miles)
    kilometres = miles*miles_in_kilometres
    print("Kilometres is: {0:.2f}".format(kilometres))
else:
    print("Invalid input")
