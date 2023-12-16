# Converter

**Description:**

Converter is a Python program that functions as a converter application, allowing the user to perform various conversions between binary, denary (decimal), hexadecimal, and octal number systems. The program provides a menu with different conversion options and includes input validation checks to ensure the user provides valid inputs for the chosen conversion. (It is an improvement on the previous Bin2Dec Project).

**Usage:**

1. **Initialization:**
   The `initializing` function initializes variables used throughout the program, providing a clear structure for managing different types of inputs and outputs.

2. **Menu Display:**
   The `print_menu` function displays the main menu with conversion options from 1 to 13, and "13. Exit" to quit the program.

3. **Input Validation:**
   The functions `presence_check`, `validity_check`, `binary_input_validity`, `denary_input_validity`, `hexadecimal_input_validity`, and `octal_input_validity` perform checks to ensure that the user's input is valid for the chosen conversion.

4. **Conversion Functions:**
   - **Binary to Denary (`binary_to_denary`):**
     Converts binary input to denary.

   - **Denary to Binary (`denary_to_binary`):**
     Converts denary input to binary.

   - **Binary to Hexadecimal (`binary_to_hexadecimal`):**
     Converts binary input to hexadecimal.

   - **Hexadecimal to Binary (`hexadecimal_to_binary`):**
     Converts hexadecimal input to binary.

   - **Binary to Octal (`binary_to_octal`):**
     Converts binary input to octal.

   - **Octal to Binary (`octal_to_binary`):**
     Converts octal input to binary.

   - **Denary to Hexadecimal (`denary_to_hexadecimal`):**
     Converts denary input to hexadecimal.

   - **Hexadecimal to Denary (`hexadecimal_to_denary`):**
     Converts hexadecimal input to denary.

   - **Denary to Octal (`denary_to_octal`):**
     Converts denary input to octal.

   - **Octal to Denary (`octal_to_denary`):**
     Converts octal input to denary.

   - **Octal to Hexadecimal (`octal_to_hexadecimal`):**
     Converts octal input to hexadecimal.

   - **Hexadecimal to Octal (`hexadecimal_to_octal`):**
     Converts hexadecimal input to octal.

5. **Helper Functions:**
   - **`convert_to_array_and_array_size`:**
     Converts user input to an array and returns the array along with its size.

   - **`convert_to_type`:**
     Converts user input to a specified data type (int or str).

   - **`multiply_by_position`:**
     Multiplies each digit by its positional notation.

   - **`continuous_division`:**
     Performs continuous division of a number by a specified conversion type.

   - **`zero_padding`:**
     Adds zero padding to the input array to ensure it is a multiple of a specified conversion type.

   - **`dec_to_hex_lookup_table` and `hex_to_dec_lookup_table`:**
     Lookup tables for converting between denary and hexadecimal.

**Libraries:**
The code does not use any external libraries beyond the built-in Python libraries. Click on the link to download Python: [Installation of python](https://www.python.org/downloads/)

**Note:**
The usage assumes that additional functions like `dec_to_hex_lookup_table`, `hex_to_dec_lookup_table`, and `continuous_division` are implemented elsewhere in the code, as they are referenced in the conversion functions.

**Usage:**

To run the code on terminal (without any GUI), execute converter.py. It will run the program.

To edit any parts of the program, the code are located in converter.py.

You can use Python IDLE to run any of the files, or any IDE of your choice that supports Python.

**Support:**

You could just call 911 should you run into errors because the developer is busy with life.

Just kidding, please contact me if you have any queries.

**Roadmap:**

Even though the game is developed, there is room for improvement. Expanding the app to a web application/ mobile application or even to improve space and time complexities of the algorithms used are explorable possibilities.

**Project Status:**

Currently, the project is completed.
