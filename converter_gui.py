import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from converter import *

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Converter App")
        self.create_first_window()

    def create_first_window(self):
        self.welcome_label = tk.Label(self.root, text="Welcome to the Converter Application!")
        self.welcome_label.pack(pady=10)

        self.tagline_label = tk.Label(self.root, text="Convert between binary, denary, hexadecimal, and octal.")
        self.tagline_label.pack(pady=5)

        frame = tk.Frame(self.root)
        frame.pack()

        self.create_conversion_buttons(frame)

    def create_conversion_buttons(self, frame):
        options = [
            "Binary to Denary",
            "Denary to Binary",
            "Binary to Hexadecimal",
            "Hexadecimal to Binary",
            "Binary to Octal",
            "Octal to Binary",
            "Denary to Hexadecimal",
            "Hexadecimal to Denary",
            "Denary to Octal",
            "Octal to Denary",
            "Octal to Hexadecimal",
            "Hexadecimal to Octal",
        ]

        row_count, col_count = 0, 0

        for i, option in enumerate(options, start=1):
            tk.Button(frame, text=option, command=lambda o=option, n=i: self.show_conversion_window(o, n)).grid(row=row_count, column=col_count, padx=10, pady=10)
            col_count += 1
            if col_count == 3:
                col_count = 0
                row_count += 1

    def show_conversion_window(self, option, number):
        choice = str(number)
        conversion_window = tk.Toplevel(self.root)
        conversion_window.title(f"Conversion Process: {option}")
        self.create_conversion_window(conversion_window, choice)


    def get_conversion_option_text(self, choice):
        conversion_options = {
            "1": "Binary to Denary",
            "2": "Denary to Binary",
            "3": "Binary to Hexadecimal",
            "4": "Hexadecimal to Binary",
            "5": "Binary to Octal",
            "6": "Octal to Binary",
            "7": "Denary to Hexadecimal",
            "8": "Hexadecimal to Denary",
            "9": "Denary to Octal",
            "10": "Octal to Denary",
            "11": "Octal to Hexadecimal",
            "12": "Hexadecimal to Octal",
        }
        return conversion_options.get(choice, "")

    def create_conversion_window(self, window, choice):
        self.current_window = window

        window.geometry("400x300")

        conversion_label = tk.Label(window, text=f"Conversion Process: {self.get_conversion_option_text(choice)}")
        conversion_label.pack(pady=10)

        self.input_label = tk.Label(window, text="Please enter the input:")
        self.input_label.pack(pady=5)

        self.input_var = tk.StringVar()
        self.input_entry = ttk.Entry(window, textvariable=self.input_var)
        self.input_entry.pack(pady=5)

        self.convert_button = ttk.Button(window, text="Convert", command=lambda: self.perform_conversion(choice))
        self.convert_button.pack(pady=10)

        self.result_label = tk.Label(window, text="")
        self.result_label.pack(pady=10)

        self.exit_button = ttk.Button(window, text="Exit", command=self.current_window.destroy)
        self.exit_button.pack(pady=5)

    def perform_conversion(self, choice):
        user_input = self.input_var.get()

        # Perform validation checks
        if not user_input.strip():
            messagebox.showerror("Error", "Input cannot be empty.")
            return

        if choice == "1":
            # Binary to Denary
            if not all(bit in "01" for bit in user_input):
                messagebox.showerror("Error", "Invalid binary input. Please input 0 or 1.")
                return
        elif choice == "2":
            # Denary to Binary
            if not user_input.isdigit():
                messagebox.showerror("Error", "Invalid denary input. Please input a valid positive integer.")
                return
        elif choice == "3":
            # Binary to Hexadecimal
            if not all(bit in "01" for bit in user_input):
                messagebox.showerror("Error", "Invalid binary input. Please input 0 or 1.")
                return
        elif choice == "4":
            # Hexadecimal to Binary
            if not all(bit in "0123456789ABCDEF" for bit in user_input):
                messagebox.showerror("Error", "Invalid hexadecimal input. Please input a valid hexadecimal number.")
                return
        elif choice == "5":
            # Binary to Octal
            if not all(bit in "01" for bit in user_input):
                messagebox.showerror("Error", "Invalid binary input. Please input 0 or 1.")
                return
        elif choice == "6":
            # Octal to Binary
            if not all(bit in "01234567" for bit in user_input):
                messagebox.showerror("Error", "Invalid octal input. Please input a valid octal number.")
                return
        elif choice == "7":
            # Denary to Hexadecimal
            if not user_input.isdigit():
                messagebox.showerror("Error", "Invalid denary input. Please input a valid positive integer.")
                return
        elif choice == "8":
            # Hexadecimal to Denary
            if not all(bit in "0123456789ABCDEF" for bit in user_input):
                messagebox.showerror("Error", "Invalid hexadecimal input. Please input a valid hexadecimal number.")
                return
        elif choice == "9":
            # Denary to Octal
            if not user_input.isdigit():
                messagebox.showerror("Error", "Invalid denary input. Please input a valid positive integer.")
                return
        elif choice == "10":
            # Octal to Denary
            if not all(bit in "01234567" for bit in user_input):
                messagebox.showerror("Error", "Invalid octal input. Please input a valid octal number.")
                return
        elif choice == "11":
            # Octal to Hexadecimal
            if not all(bit in "01234567" for bit in user_input):
                messagebox.showerror("Error", "Invalid octal input. Please input a valid octal number.")
                return
        elif choice == "12":
            # Hexadecimal to Octal
            if not all(bit in "0123456789ABCDEF" for bit in user_input):
                messagebox.showerror("Error", "Invalid hexadecimal input. Please input a valid hexadecimal number.")
                return

        result = self.calculate_conversion(choice, user_input)
        self.show_result(result)

    def calculate_conversion(self, choice, user_input):
        result = ""

        if choice == "1":
            result = binary_to_denary(user_input)
        elif choice == "2":
            result = denary_to_binary(user_input)
        elif choice == "3":
            result = binary_to_hexadecimal(user_input)
        elif choice == "4":
            result = hexadecimal_to_binary(user_input)
        elif choice == "5":
            result = binary_to_octal(user_input)
        elif choice == "6":
            result = octal_to_binary(user_input)
        elif choice == "7":
            result = denary_to_hexadecimal(user_input)
        elif choice == "8":
            result = hexadecimal_to_denary(user_input)
        elif choice == "9":
            result = denary_to_octal(user_input)
        elif choice == "10":
            result = octal_to_denary(user_input)
        elif choice == "11":
            result = octal_to_hexadecimal(user_input)
        elif choice == "12":
            result = hexadecimal_to_octal(user_input)

        return result

    def show_result(self, result):
        self.result_label.config(text=f"Result: {result}")
        self.result_label.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()