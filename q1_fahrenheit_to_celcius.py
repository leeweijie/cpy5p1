def verify_input (input):
    try:
        float(input)
        return True
    except ValueError:
        return False

fahrenheit = input("Enter temperature in Fahrenheit: ")
if verify_input(fahrenheit):
    fahrenheit = float(fahrenheit)
    celcius = (5/9)*(fahrenheit - 32)
    print("Temperature in Celcius {0:.1f}".format(celcius))
else:
    print("Invalid input")
