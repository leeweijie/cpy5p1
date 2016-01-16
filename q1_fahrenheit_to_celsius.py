# Check if input is a number and convert it to float
def process_input():
    global fahrenheit
    try:
        fahrenheit = float(fahrenheit)
        return True
    except ValueError:
        return False

# Get user input
fahrenheit = input("Enter temperature in Fahrenheit: ")

if process_input():

    # Convert Fahrenheit to Celsius
    celsius = (5 / 9) * (fahrenheit - 32)

    # Print temperature in Celsius to 1 d.p.
    print("Temperature in Celcius {0:.1f}".format(celsius))
else:
    print("Invalid input")
