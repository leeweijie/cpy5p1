def verify_input (input):
    try:
        int(input)
        return True
    except ValueError:
        return False

ascii_code = input("Enter ASCII code: ")
if verify_input(ascii_code):
    ascii_code=int(ascii_code)
    print(chr(ascii_code))