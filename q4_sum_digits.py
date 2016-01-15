def verify_input (input):
    try:
        input = int(input)
        if input>0 and input<1000:
            return True
        else:
            return False
    except ValueError:
        return False

number = input("Enter a number between 0 and 1000: ")
if verify_input(number):
    number = int(number)
    result = 0
    for i in range(len(str(number))):
        result += number%10
        number = number//10
    print(result)
else:
    print("Invalid input")
