#### Main Functions ####

# Initialising the variables
def initialising():
    total, user_input, binary_input_array, binary_output_array, binary_output_nibble, \
    hex_input_array, hex_output_array, octal_input_array, octal_output_array, \
    denary_input, denary_output, array_size, nibble_size, tribble_size, \
    character, number, remainder, quotient, hex_charcter, denary_number, digit, \
    octal_output, hex_output, binary_output, octal_output_to_user  = None, None, [], [], [], [], [], [], [], None, None, \
    None, None, None, None, None, None, None, None, None, None, None, None, None, None

# Displaying the Main Menu
def print_menu():
    print("Please choose from the following options: ")
    print("1. Binary to Denary")
    print("2. Denary to Binary")
    print("3. Binary to Hexadecimal")
    print("4. Hexadecimal to Binary")
    print("5. Binary to Octal")
    print("6. Octal to Binary")
    print("7. Denary to Hexadecimal")
    print("8. Hexadecimal to Denary")
    print("9. Denary to Octal")
    print("10. Octal to Denary")
    print("11. Octal to Hexadecimal")
    print("12. Hexadecimal to Octal")
    print("13. Exit")
     
# Presence Check
def presence_check(choice):
    while choice == "":
        print("The choice cannot be empty. Please choose a conversion method or to exit the application.")
        print_menu()
        choice = input("Please input a number between 1 and 13: ")
    return choice

# Validity Check
def validity_check(choice):
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" \
    and choice != "6" and choice != "7" and choice != "8" and choice != "9" and choice != "10" \
    and choice != "11" and choice != "12" and choice != "13":
        print("The choice is invalid. Please choose a conversion method or to exit the application.")
        print_menu()
        choice = input("Please input a number between 1 and 13: ")
    return choice

# Check if the input is binary
def binary_input_validity(user_input):
    while user_input == "":
        print("The input cannot be empty. Please input 0 or 1: ")
        user_input = input("Please input 1 or more binary digits: ")

    index = 0
    user_input_size = len(user_input)
    while index <= user_input_size - 1:
        if user_input[index] != "0" and user_input[index] != "1":
            print("This is not a binary digit! Please input 0 or 1: ")
            user_input = input("Please input 1 or more binary digits: ")
            user_input_size = len(user_input)
            index = 0
        else:
            index += 1

# Check if the input is denary            
def denary_input_validity(user_input):
    while user_input == "":
        print("The input cannot be empty. Please input 0, 1, 2, 3, 4, 5, 6, 7, 8 or 9: ")
        user_input = input("Please input 1 or more denary digits: ")
        
    index = 0
    user_input_size = len(user_input)
    while index <= user_input_size - 1:
        if user_input[index] != "0" and user_input[index] != "1" and user_input[index] != "2" \
        and user_input[index] != "3" and user_input[index] != "4" and user_input[index] != "5" \
        and user_input[index] != "6" and user_input[index] != "7" and user_input[index] != "8" \
        and user_input[index] != "9":
            print("This is not a denary digit! Please input 0, 1, 2, 3, 4, 5, 6, 7, 8 or 9: ")
            user_input = input("Please input 1 or more denary digits: ")
            user_input_size = len(user_input)
            index = 0
        else:
            index += 1
            
# Check if the input is hexadecimal
def hexadecimal_input_validity(user_input):
    while user_input == "":
        print("The input cannot be empty. Please input 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E or F: ")
        user_input = input("Please input 1 or more hexadecimal digits: ")
        
    index = 0
    user_input_size = len(user_input)
    while index <= user_input_size - 1:
        if user_input[index] != "0" and user_input[index] != "1" and user_input[index] != "2" \
        and user_input[index] != "3" and user_input[index] != "4" and user_input[index] != "5" \
        and user_input[index] != "6" and user_input[index] != "7" and user_input[index] != "8" \
        and user_input[index] != "9" and user_input[index] != "A" and user_input[index] != "B" \
        and user_input[index] != "C" and user_input[index] != "D" and user_input[index] != "E" \
        and user_input[index] != "F":
            print("This is not a hexadecimal digit! Please input 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E or F: ")
            user_input = input("Please input 1 or more hexadecimal digits: ")
            user_input_size = len(user_input)
            index = 0
        else:
            index += 1
            
# Check if the input is octal
def octal_input_validity(user_input):
    while user_input == "":
        print("The input cannot be empty. Please input 0, 1, 2, 3, 4, 5, 6, or 7: ")
        user_input = input("Please input 1 or more octal digits: ")
        
    index = 0
    user_input_size = len(user_input)
    while index <= user_input_size - 1:
        if user_input[index] != "0" and user_input[index] != "1" and user_input[index] != "2" \
        and user_input[index] != "3" and user_input[index] != "4" and user_input[index] != "5" \
        and user_input[index] != "6" and user_input[index] != "7":
            print("This is not an octal digit! Please input 0, 1, 2, 3, 4, 5, 6 or 7: ")
            user_input = input("Please input 1 or more octal digits: ")
            user_input_size = len(user_input)
            index = 0
        else:
            index += 1   

#### Other Functions #####

# Convert the user input into an array and returns the array +  the size of the array
def convert_to_array_and_array_size(user_input):
    array = list(user_input)
    array_size = len(array)
    return array, array_size

# Convert the user input into an integer
def convert_to_type(user_input, output_type):
    if output_type == "int":
        data = int(user_input)
    elif output_type == "str":
        data = ''.join(map(str, user_input))
    return data

# Continuous division
def continuous_division(number, conversion_type):
    output_array = []
    while number > 0:
        remainder = number % conversion_type
        number = number // conversion_type
        output_array.append(remainder)
    return output_array

# Conversion table for denary to hexadecimal
def dec_to_hex_lookup_table(number):
    if number == 10:
        character = "A"
    elif number == 11:
        character = "B"
    elif number == 12:
        character = "C"
    elif number == 13:
        character = "D"
    elif number == 14:
        character = "E"
    elif number == 15:
        character = "F"
    else:
        character = number
    return character

# Conversion table for hexadecimal to denary
def hex_to_dec_lookup_table(character):
    if character == "A":
        number = 10
    elif character == "B":
        number = 11
    elif character == "C":
        number = 12
    elif character == "D":
        number = 13
    elif character == "E":
        number = 14
    elif character == "F":
        number = 15
    else:
        number = int(character)
    return number
    
#### Conversion Functions ####

### Binary to Denary ###
def binary_to_denary(user_input): 
    binary_input_array, array_size = convert_to_array_and_array_size(user_input)

    # Flip the array
    binary_input_array.reverse()
    denary_output = 0
    for i in range(0, array_size):
        if binary_input_array[i] == '1':
            denary_output += 2**i
        else:
            denary_output += 0
    return denary_output

### Denary to Binary ###
def denary_to_binary(user_input): 
    denary_number = convert_to_type(user_input, "int")
    binary_output_array = continuous_division(denary_number, 2)
  
    # Flip the array
    binary_output_array.reverse()
    
    binary_output = convert_to_type(binary_output_array, "str")
    
    return binary_output
    
### Binary to Hexadecimal ###
def binary_to_hexadecimal(user_input):
    binary_input_array, array_size = convert_to_array_and_array_size(user_input)
    total = 0
    hex_output = ""
    hex_output_array = []

    # Make the array a multiple of 4
    binary_input_array = zero_padding(binary_input_array, array_size, 4)

    # Divide into 4 bits arrays
    for i in range(0, array_size, 4):
        nibble = binary_input_array[i:i+4]
        nibble.reverse()
        total = sum(int(bit) * 2**j for j, bit in enumerate(nibble))
        character = dec_to_hex_lookup_table(total)          
        hex_output_array.append(character)    
    
    hex_output = convert_to_type(hex_output_array, "str")
        
    return hex_output
    
### Hexadecimal to Binary ###
def hexadecimal_to_binary(user_input):
    hex_input_array, array_size = convert_to_array_and_array_size(user_input)
    binary_output_array = []
    
    for i in range(0, array_size):
        character = hex_input_array[i]
        number = hex_to_dec_lookup_table(character) 
        binary_output_nibble = continuous_division(number, 2)     
        binary_output_nibble.reverse()
        binary_output_array.append(convert_to_type(binary_output_nibble, "str"))
        
    binary_output = convert_to_type(binary_output_array, "str")
        
    return binary_output

### Binary to Octal ###
def binary_to_octal(user_input):
    binary_input_array, array_size = convert_to_array_and_array_size(user_input)
    octal_output_array = []

    # Check if the array is a multiple of 3
    if array_size % 3 != 0:
        while array_size % 3 != 0:
            binary_input_array.insert(0, 0)
            array_size += 1

    # Divide into 3 bits arrays
    for i in range(0, array_size, 3):
        tribble = binary_input_array[i:i+3]
        tribble.reverse()
        octal_output = sum(int(bit) * 2**j for j, bit in enumerate(tribble))
        octal_output_array.append(octal_output)
        
    octal_output_to_user = convert_to_type(octal_output_array, "str")
    
    return octal_output_to_user

### Octal to Binary ###
def octal_to_binary(user_input):
    binary_output_array = []
    
    for octal_digit in user_input:
        binary_output_array.append(bin(int(octal_digit, 8))[2:].zfill(3))

    binary_output = ''.join(binary_output_array)
    return binary_output

### Denary to Hexadecimal ###
def denary_to_hexadecimal(user_input):
    denary_input = convert_to_type(user_input, "int")
    hex_output_array = []

    # If denary is smaller than 16
    if denary_input < 16:
        hex_character = dec_to_hex_lookup_table(denary_input)
        hex_output_array.append(hex_character)
    else:
        while denary_input > 0:
            remainder = denary_input % 16
            hex_character = dec_to_hex_lookup_table(remainder)
            hex_output_array.insert(0, hex_character)
            denary_input //= 16
        
    hex_output = convert_to_type(hex_output_array, "str") 
    return hex_output

### Hexadecimal to Denary ###
def hexadecimal_to_denary(user_input):
    hex_input_array, array_size = convert_to_array_and_array_size(user_input)
    total = 0

    # Flip array
    hex_input_array.reverse()

    for i in range(0, array_size):
        character = hex_input_array[i]
        number = hex_to_dec_lookup_table(character)
        total += number * 16**i
        
    return total

### Denary to Octal ###
def denary_to_octal(user_input):
    denary_input = convert_to_type(user_input, "int")
    octal_output_array = continuous_division(denary_input, 8)
        
    # Flip the array
    octal_output_array.reverse()

    octal_output = convert_to_type(octal_output_array, "str")

    return octal_output

### Octal to Denary ###
def octal_to_denary(user_input):
    octal_input_array, array_size = convert_to_array_and_array_size(user_input)
    total = 0

    # Flip the array
    octal_input_array.reverse()

    for i in range(0, array_size):
        digit = int(octal_input_array[i])
        total += digit * 8**i
        
    return total
        
### Octal to Hexadecimal ###
def octal_to_hexadecimal(user_input):
    octal_input_array, array_size = convert_to_array_and_array_size(user_input)
    total = 0
    hex_output_array = []

    # Flip the array
    octal_input_array.reverse()

    for i in range(0, array_size):
        digit = int(octal_input_array[i])
        total += digit * 8**i
        
    hex_output_array = continuous_division(total, 16)
    
    # Correct hex_output_array to represent hexadecimal digits
    for i in range(len(hex_output_array)):
        hex_output_array[i] = dec_to_hex_lookup_table(int(hex_output_array[i]))
        
    hex_output_array.reverse()
    hex_output = convert_to_type(hex_output_array, "str")
    
    return hex_output
    
### Hexadecimal to Octal ###
def hexadecimal_to_octal(user_input):
    hex_input_array, array_size = convert_to_array_and_array_size(user_input)
    total = 0
    octal_output_array = []

    # Flip the array
    hex_input_array.reverse()

    for i in range(0, array_size):
        character = hex_input_array[i]
        number = hex_to_dec_lookup_table(character)
        total += number * 16**i
        
    octal_output_array = continuous_division(total, 8)
    octal_output_array.reverse()
    octal_output = convert_to_type(octal_output_array, "str")
    
    return octal_output
    
### Main module ###
if __name__ == "__main__":
    print("Welcome to the Converter Application!")
    while True:
        # Initialise the variables
        initialising()
        
        # Print Menu
        print_menu()
       
        # Take in choice input
        choice = input("Please enter only the number of your choice: ")
        
        # Validation Check
        presence_check(choice)
        validity_check(choice)
        
        if choice == "13":
            print("Exiting the Converter Application. Goodbye!")
            break

        # Perform the conversion based on the user's choice
        if choice == "1":
            print("You have chosen Binary to Denary.")
            user_input = input("Please input 1 or more binary digits: ")
            binary_input_validity(user_input)
            denary_output = binary_to_denary(user_input)
            print("The equivalent denary equivalent for", user_input, "is", denary_output)
            
        elif choice == "2":
            print("You have chosen Denary to Binary.")
            user_input = input("Please input 1 or more denary digits: ")
            denary_input_validity(user_input)
            denary_output_array = denary_to_binary(user_input)
            print("The equivalent binary equivalent for", user_input, "is", denary_output_array)
            
        elif choice == "3":
            print("You have chosen Binary to Hexadecimal.")
            user_input = input("Please input 1 or more binary digits: ")
            binary_input_validity(user_input)
            hex_output_array = binary_to_hexadecimal(user_input)
            print("The equivalent hexadecimal equivalent for", user_input, "is", hex_output_array)
            
        elif choice == "4":
            print("You have chosen Hexadecimal to Binary.")
            user_input = input("Please input 1 or more hexadecimal digits: ")
            hexadecimal_input_validity(user_input)
            hex_output_array = hexadecimal_to_binary(user_input)
            print("The equivalent binary equivalent for", user_input, "is", hex_output_array)
            
        elif choice == "5":
            print("You have chosen Binary to Octal.")
            user_input = input("Please input 1 or more binary digits: ")
            binary_input_validity(user_input)
            octal_output_array = binary_to_octal(user_input)
            print("The equivalent octal equivalent for", user_input, "is", octal_output_array)
            
        elif choice == "6":
            print("You have chosen Octal to Binary.")
            user_input = input("Please input 1 or more octal digits: ")
            octal_input_validity(user_input)
            binary_output_array = octal_to_binary(user_input)
            print("The equivalent binary equivalent for", user_input, "is", binary_output_array)
            
        elif choice == "7":
            print("You have chosen Denary to Hexadecimal.")
            user_input = input("Please input 1 or more denary digits: ")
            denary_input_validity(user_input)
            hex_output = denary_to_hexadecimal(user_input)
            print("The equivalent hexadecimal equivalent for", user_input, "is", hex_output)
        
        elif choice == "8":
            print("You have chosen Hexadecimal to Denary.")
            user_input = input("Please input 1 or more hexadecimal digits: ")
            hexadecimal_input_validity(user_input)
            denary_output = hexadecimal_to_denary(user_input)
            print("The equivalent denary equivalent for", user_input, "is", denary_output)
            
        elif choice == "9":
            print("You have chosen Denary to Octal.")
            user_input = input("Please input 1 or more denary digits: ")
            denary_input_validity(user_input)
            octal_output_array = denary_to_octal(user_input)
            print("The equivalent octal equivalent for", user_input, "is", octal_output_array)
            
        elif choice == "10":
            print("You have chosen Octal to Denary.")
            user_input = input("Please input 1 or more octal digits: ")
            octal_input_validity(user_input)
            denary_output = octal_to_denary(user_input)
            print("The equivalent denary equivalent for", user_input, "is", denary_output)
            
        elif choice == "11":
            print("You have chosen Octal to Hexadecimal.")
            user_input = input("Please input 1 or more octal digits: ")
            octal_input_validity(user_input)
            hexadecimal_output = octal_to_hexadecimal(user_input)
            print("The equivalent hexadecimal equivalent for", user_input, "is", hexadecimal_output)
            
        elif choice == "12":
            print("You have chosen Hexadecimal to Octal.")
            user_input = input("Please input 1 or more hexadecimal digits: ")
            hexadecimal_input_validity(user_input)
            octal_output_array = hexadecimal_to_octal(user_input)
            print("The equivalent octal equivalent for", user_input, "is", octal_output_array)

        # Pause the program until the user presses Enter
        input("Press Enter to continue...")
    
    exit()   
