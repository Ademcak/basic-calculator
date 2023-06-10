import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, str(current) + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    expression = display.get()
    result = eval(expression)
    display.delete(0, tk.END)
    display.insert(tk.END, result)

# Create the GUI window
window = tk.Tk()
window.title("Calculator")

# Create the display widget
display = tk.Entry(window, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Define the buttons
buttons = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
    ('0', 3, 0), ('+', 3, 1), ('-', 3, 2),
    ('*', 4, 0), ('/', 4, 1), ('=', 4, 2),
    ('C', 5, 0)
]

# Create the buttons
for button_text, row, column in buttons:
    button = tk.Button(window, text=button_text, padx=30, pady=20,
                       command=lambda text=button_text: button_click(text))
    button.grid(row=row+1, column=column)

# Create the clear button
clear_button = tk.Button(window, text="C", padx=30, pady=20, command=button_clear)
clear_button.grid(row=5, column=0, columnspan=2)

# Create the equal button
equal_button = tk.Button(window, text="=", padx=30, pady=20, command=button_equal)
equal_button.grid(row=5, column=2)

# Start the main event loop
window.mainloop()
