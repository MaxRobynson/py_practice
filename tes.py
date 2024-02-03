import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_add():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_divide():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
    if math_operation == "addition":
        entry.insert(0, f_num + float(second_number))
    elif math_operation == "subtraction":
        entry.insert(0, f_num - float(second_number))
    elif math_operation == "multiplication":
        entry.insert(0, f_num * float(second_number))
    elif math_operation == "division":
        entry.insert(0, f_num / float(second_number))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the input and result
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Create buttons and place them on the grid
for button_text, row, col in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20, command=lambda text=button_text: button_click(text) if text != "C" and text != "=" else button_clear() if text == "C" else button_equal())
    button.grid(row=row, column=col)

# Start the main loop
root.mainloop()
