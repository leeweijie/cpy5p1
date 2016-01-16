# Check if input is a number and within range and convert it to an integer
def process_input ():
    global number
    try:
        number = int(number)
        if number>0 and number<1000:
            return True
        else:
            return False
    except ValueError:
        return False

# Get user input
number = input("Enter a number between 0 and 1000: ")

if process_input():

    result = 0
    for i in range(len(str(number))):
        result += number%10 # Get last digit of input and add it to result
        number = number//10 # Remove the last digit of input

    # Print result
    print(result)
else:
    print("Invalid input")
