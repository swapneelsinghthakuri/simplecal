import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")
window.resizable(False, False)

# Variable to store the current calculation
calculation = ""

# Function to update the display when buttons are clicked
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# Function to evaluate the calculation when = is pressed
def evaluate_calculation():
    global calculation
    try:
        # Replace × and ÷ with * and / for Python to understand
        calculation = calculation.replace("×", "*").replace("÷", "/")
        result = str(eval(calculation))
        calculation = result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

# Function to clear the display
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

# Create the display screen
text_result = tk.Text(window, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=4, padx=10, pady=10)

# Create number buttons (0-9)
button_1 = tk.Button(window, text="1", command=lambda: add_to_calculation(1), width=5, height=2, font=("Arial", 14))
button_1.grid(row=2, column=0, padx=5, pady=5)

button_2 = tk.Button(window, text="2", command=lambda: add_to_calculation(2), width=5, height=2, font=("Arial", 14))
button_2.grid(row=2, column=1, padx=5, pady=5)

button_3 = tk.Button(window, text="3", command=lambda: add_to_calculation(3), width=5, height=2, font=("Arial", 14))
button_3.grid(row=2, column=2, padx=5, pady=5)

button_4 = tk.Button(window, text="4", command=lambda: add_to_calculation(4), width=5, height=2, font=("Arial", 14))
button_4.grid(row=3, column=0, padx=5, pady=5)

button_5 = tk.Button(window, text="5", command=lambda: add_to_calculation(5), width=5, height=2, font=("Arial", 14))
button_5.grid(row=3, column=1, padx=5, pady=5)

button_6 = tk.Button(window, text="6", command=lambda: add_to_calculation(6), width=5, height=2, font=("Arial", 14))
button_6.grid(row=3, column=2, padx=5, pady=5)

button_7 = tk.Button(window, text="7", command=lambda: add_to_calculation(7), width=5, height=2, font=("Arial", 14))
button_7.grid(row=4, column=0, padx=5, pady=5)

button_8 = tk.Button(window, text="8", command=lambda: add_to_calculation(8), width=5, height=2, font=("Arial", 14))
button_8.grid(row=4, column=1, padx=5, pady=5)

button_9 = tk.Button(window, text="9", command=lambda: add_to_calculation(9), width=5, height=2, font=("Arial", 14))
button_9.grid(row=4, column=2, padx=5, pady=5)

button_0 = tk.Button(window, text="0", command=lambda: add_to_calculation(0), width=5, height=2, font=("Arial", 14))
button_0.grid(row=5, column=1, padx=5, pady=5)

# Create operation buttons
button_plus = tk.Button(window, text="+", command=lambda: add_to_calculation("+"), width=5, height=2, font=("Arial", 14))
button_plus.grid(row=2, column=3, padx=5, pady=5)

button_minus = tk.Button(window, text="-", command=lambda: add_to_calculation("-"), width=5, height=2, font=("Arial", 14))
button_minus.grid(row=3, column=3, padx=5, pady=5)

button_multiply = tk.Button(window, text="×", command=lambda: add_to_calculation("×"), width=5, height=2, font=("Arial", 14))
button_multiply.grid(row=4, column=3, padx=5, pady=5)

button_divide = tk.Button(window, text="÷", command=lambda: add_to_calculation("÷"), width=5, height=2, font=("Arial", 14))
button_divide.grid(row=5, column=3, padx=5, pady=5)

# Create Clear and Equal buttons
button_clear = tk.Button(window, text="C", command=clear_field, width=5, height=2, font=("Arial", 14), bg="#ff9999")
button_clear.grid(row=5, column=0, padx=5, pady=5)

button_equals = tk.Button(window, text="=", command=evaluate_calculation, width=5, height=2, font=("Arial", 14), bg="#99ff99")
button_equals.grid(row=5, column=2, padx=5, pady=5)

# Start the application
window.mainloop()