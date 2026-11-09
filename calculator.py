
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x420")
root.resizable(False, False)

# Input display
entry = tk.Entry(
    root,
    font=("Arial", 22),
    justify="right",
    bd=10
)
entry.pack(fill="x", padx=10, pady=20)


# Button click function
def click(value):
    entry.insert(tk.END, value)


# Clear function
def clear():
    entry.delete(0, tk.END)


# Calculate function
def calculate():
    try:
        result = eval(entry.get())

        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Cannot divide by zero")

    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Input")


# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for item in row:
        if item == "=":
            btn = tk.Button(
                frame,
                text=item,
                font=("Arial", 18),
                command=calculate
            )
        else:
            btn = tk.Button(
                frame,
                text=item,
                font=("Arial", 18),
                command=lambda x=item: click(x)
            )

        btn.pack(side="left", expand=True, fill="both")


# Clear button
clear_btn = tk.Button(
    root,
    text="CLEAR",
    font=("Arial", 16),
    bg="red",
    fg="white",
    command=clear
)
clear_btn.pack(fill="both", padx=10, pady=10)

# Run application
root.mainloop()
