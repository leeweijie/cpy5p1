user_string = raw_input("Enter string: ")
upper_to_lower=32
result = ""

for i in range(len(user_string)):
    char = user_string[i]
    ascii_number = ord(char)
    if ascii_number>=65 and ascii_number<=90:
        captial_char = chr(ascii_number+upper_to_lower)
        result +=captial_char
    else:
        result +=char

print(result)