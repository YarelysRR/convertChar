def char_to_ascii(char):
    return ord(char)

def ascii_to_char(ascii_value):
    return chr(ascii_value)

def ascii_to_binary(ascii_value):
    return bin(ascii_value)[2:]  # Removing the '0b' prefix

def binary_to_ascii(binary_value):
    return chr(int(binary_value, 2))

def char_to_binary(char):
    return bin(ord(char))[2:]

while True:
    print("*** Welcome to ConvertChar! ***")
    print("\nOptions:")
    print("1. Convert character(s) to ASCII")
    print("2. Convert ASCII to character(s)")
    print("3. Convert ASCII to binary")
    print("4. Convert binary to ASCII")
    print("5. Convert character(s) to binary")
    print("6. Exit")

    choice = input("\nEnter your choice (1, 2, 3, 4, 5, or 6): ")

    if choice.lower() == 'exit' or choice == '6':
        print("Thanks for using ConvertChar! Goodbye!")
        break

    print("(Type 'exit' to quit at any time)\n")

    if choice == '1':
        user_input = input("Enter a character or a word: ")
        if user_input.lower() == 'exit':
            break
        for char in user_input:
            print(f"ASCII value of '{char}' is {char_to_ascii(char)}")

    elif choice == '2':
        user_input = input("Enter ASCII value(s) separated by commas (,): ")
        if user_input.lower() == 'exit':
            break
        ascii_values = user_input.split(',')
        for ascii_value in ascii_values:
            try:
                ascii_value = int(ascii_value)
                print(f"Character(s) corresponding to ASCII value {ascii_value}: {ascii_to_char(ascii_value)}")
            except ValueError:
                print(f"Invalid input: {ascii_value}")

    elif choice == '3':
        user_input = input("Enter ASCII value(s) separated by commas (,): ")
        if user_input.lower() == 'exit':
            break
        ascii_values = user_input.split(',')
        for ascii_value in ascii_values:
            try:
                ascii_value = int(ascii_value)
                print(f"Binary representation of ASCII value {ascii_value}: {ascii_to_binary(ascii_value)}")
            except ValueError:
                print(f"Invalid input: {ascii_value}")

    elif choice == '4':
        user_input = input("Enter binary value(s) separated by commas (,): ")
        if user_input.lower() == 'exit':
            break
        binary_values = user_input.split(',')
        for binary_value in binary_values:
            try:
                print(f"ASCII value(s) of binary {binary_value}: {binary_to_ascii(binary_value)}")
            except ValueError:
                print(f"Invalid input: {binary_value}")

    elif choice == '5':
        user_input = input("Enter a character or a word: ")
        if user_input.lower() == 'exit':
            break
        for char in user_input:
            print(f"Binary representation of '{char}' is {char_to_binary(char)}")

    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
