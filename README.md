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

   - **`continuous_division`:**
     Performs continuous division of a number by a specified conversion type.

   - **`zero_padding`:**
     Adds zero padding to the input array to ensure it is a multiple of a specified conversion type.

   - **`dec_to_hex_lookup_table` and `hex_to_dec_lookup_table`:**
     Lookup tables for converting between denary and hexadecimal.

**Note:**
The usage assumes that additional functions like `dec_to_hex_lookup_table`, `hex_to_dec_lookup_table`, and `continuous_division` are implemented elsewhere in the code, as they are referenced in the conversion functions.

**Usage:**

To help you better, I'll need more information about the specific `converter.py` script you're referring to. In general, running a Python script involves using the Python interpreter in your terminal or command prompt. Here are the general steps:

1. **Install Python:**
   Make sure you have Python installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/). Follow the installation instructions for your operating system.

2. **Open a Terminal or Command Prompt:**
   Open a terminal (Linux/macOS) or command prompt (Windows).

3. **Navigate to the Script's Directory:**
   Use the `cd` command to navigate to the directory where the `converter.py` script is located. For example:
   ```bash
   cd path/to/your/script
   ```

4. **Run the Script:**
   Once you're in the correct directory, run the script using the `python` command (or `python3` on some systems):
   ```bash
   python converter.py
   ```
   If the script requires command-line arguments, provide them after the script name. For example:
   ```bash
   python converter.py arg1 arg2
   ```

   If the script is executable and has a shebang line (`#!/usr/bin/env python` or similar) at the beginning, you might be able to run it directly:
   ```bash
   ./converter.py
   ```

   On Windows, you might need to use `python` explicitly:
   ```bash
   python converter.py
   ```

5. **Follow any Instructions:**
   The script may have prompts or require certain inputs. Follow any on-screen instructions or provide any necessary information.

Keep in mind that the specific steps may vary depending on the script's requirements, your operating system, and the version of Python you have installed. If there are specific instructions or documentation provided with the `converter.py` script, be sure to review that information.

**How to use it with the GUI:**

To run `converter_gui.py`, you can follow these steps:

1. **Ensure Python is Installed:**
   Make sure you have Python installed on your system. If not, you can download and install it from the official [Python website](https://www.python.org/downloads/).

2. **Download or Create Necessary Files:**
   Ensure that you have the following files in the same directory:
   - `converter_gui.py`: The main script containing the GUI code.
   - `converter.py`: The module containing conversion functions.

3. **Open a Terminal or Command Prompt:**
   Open a terminal or command prompt in the directory where the `converter_gui.py` file is located.

4. **Run the Script:**
   Type the following command and press Enter to run the script:

   ```bash
   python converter_gui.py
   ```

   If you are using Python 3, you might need to use `python3` instead:

   ```bash
   python3 converter_gui.py
   ```

5. **GUI Application:**
   After running the command, the GUI application should open. You'll see the main window with conversion options. You can interact with the GUI to perform various conversions.

Please note that the instructions assume that your system's PATH variable includes the path to the Python interpreter. If you encounter any issues, ensure that Python is correctly installed and that the `python` command is recognized in your terminal or command prompt.

**Roadmap:**

Even though the game is developed, there is room for improvement. Expanding the app to a web application/ mobile application or even to improve space and time complexities of the algorithms used are explorable possibilities.

**Project Status:**

Currently, the application is complete!
