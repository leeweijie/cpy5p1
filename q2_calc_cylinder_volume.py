from math import pi


# Check if inputs are numbers and convert them to floats
def process_input():
    global radius, length
    try:
        radius = float(radius)
        length = float(length)
        return True
    except ValueError:
        return False

# Get user input
radius = input("Enter radius: ")
length = input("Enter length: ")

if process_input():
    # Calculate volume
    volume = (radius**2)*pi*length

    # Print volume to 2 d.p.
    print ("Volume is: {0:.2f}".format(volume))
else:
    print("Invalid input")
