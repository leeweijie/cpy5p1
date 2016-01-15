from math import pi

def verify_input(radius, length):
    try:
        float(radius)
        float(length)
        return True
    except ValueError:
        return False

radius = input("Enter radius: ")
length = input("Enter length: ")
if verify_input(radius, length):
    radius = float(radius)
    length = float (length)
    volume = (radius**2)*pi*length
    print ("Volume is: {0:.2f}".format(volume))
else:
    print("Invalid input")
