# Check if input is a number and convert it to an integer
def process_input():
    global ascii_code
    try:
        ascii_code = int(ascii_code)
        return True
    except ValueError:
        return False
# Get user input
ascii_code = input("Enter ASCII code: ")
if process_input():
    # Get and print character that corresponds to the ascii value
    print(chr(ascii_code))
else:
    print("Invalid input")