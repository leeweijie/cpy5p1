# Check if input is a number and convert it to float
def process_input ():
    global miles
    try:
        miles = float(miles)
        return True
    except ValueError:
        return False

# Conversion constant
miles_in_kilometres = 1.60934

# Get user input
miles = input("Enter miles: ")
if process_input():

    # Convert miles to kilometres
    kilometres = miles*miles_in_kilometres

    # Print distance is kilometres to 2 d.p.
    print("Kilometres is: {0:.2f}".format(kilometres))
else:
    print("Invalid input")
