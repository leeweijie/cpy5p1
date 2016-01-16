# Get user input
user_string = input("Enter string: ")

# Difference between ASCII value of upper and lowercase alphabets
upper_to_lower=32

result = ""

for i in range(len(user_string)):

    # Get a character from string
    char = user_string[i]

    # Get ASCII value of character
    ascii_number = ord(char)

    if ascii_number>=65 and ascii_number<=90: # Check if character is a uppercase alphabet

        # Convert uppercase character to lowercase
        lowercase_char = chr(ascii_number+upper_to_lower)

        # Append converted character to result string
        result +=lowercase_char
    else:
        # Append unchanged character to result string
        result +=char

# Print result
print(result)