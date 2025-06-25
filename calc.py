import tkinter as tk
import math

# Setup main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.resizable(False, False)

# Themes
themes = {
    "dark": {"bg": "#1e1e2f", "fg": "white", "btn": "#3c3f58"},
    "light": {"bg": "#f1f2f6", "fg": "black", "btn": "#dcdde1"}
}
current_theme = "dark"

expression = ""

# Display
display = tk.Label(root, text="", anchor="e", font=("Consolas", 24), height=2)
display.pack(fill="both", padx=10, pady=10)

# Update theme
def apply_theme():
    colors = themes[current_theme]
    root.config(bg=colors["bg"])
    display.config(bg=colors["btn"], fg=colors["fg"])
    for widget in btn_frame.winfo_children():
        widget.config(bg=colors["btn"], fg=colors["fg"])

# Theme toggle
def toggle_theme():
    global current_theme
    current_theme = "light" if current_theme == "dark" else "dark"
    apply_theme()

# Evaluate expression
def evaluate_expression():
    global expression
    try:
        expression_eval = expression.replace("^", "**").replace("√", "sqrt")
        result = eval(expression_eval, {"__builtins__": None}, math.__dict__)
        display.config(text=str(result))
        expression = str(result)
    except:
        display.config(text="Error")
        expression = ""

# Update expression
def on_click(value):
    global expression
    expression += str(value)
    display.config(text=expression)

def clear():
    global expression
    expression = ""
    display.config(text="")

# Animate button press
def animate(btn):
    original_color = btn["bg"]
    btn.config(bg="#00aaff")
    root.update()
    root.after(100, lambda: btn.config(bg=original_color))

# Keyboard input
def key_handler(event):
    key = event.char
    if key in "0123456789.+-*/()^":
        on_click(key)
    elif key == "\r":  # Enter
        evaluate_expression()
    elif event.keysym == "BackSpace":
        backspace()
    elif key.lower() == "c":
        clear()

def backspace():
    global expression
    expression = expression[:-1]
    display.config(text=expression)

# Button builder
def create_button(frame, text, command, colspan=1):
    colors = themes[current_theme]
    btn = tk.Button(frame, text=text, font=("Arial", 14),
                    bg=colors["btn"], fg=colors["fg"], bd=0, relief="flat",
                    activebackground="#44475a",
                    command=lambda: [command(), animate(btn)])
    btn.grid(row=create_button.row, column=create_button.col, columnspan=colspan, sticky="nsew", padx=2, pady=2)
    create_button.col += colspan
    if create_button.col >= 4:
        create_button.col = 0
        create_button.row += 1
create_button.row = 0
create_button.col = 0

# Buttons Frame
btn_frame = tk.Frame(root)
btn_frame.pack(expand=True, fill="both", padx=10, pady=10)

# Configure grid
for i in range(6):
    btn_frame.grid_rowconfigure(i, weight=1)
    btn_frame.grid_columnconfigure(i % 4, weight=1)

# Define buttons
buttons = [
    ("7", lambda: on_click("7")), ("8", lambda: on_click("8")), ("9", lambda: on_click("9")), ("/", lambda: on_click("/")),
    ("4", lambda: on_click("4")), ("5", lambda: on_click("5")), ("6", lambda: on_click("6")), ("*", lambda: on_click("*")),
    ("1", lambda: on_click("1")), ("2", lambda: on_click("2")), ("3", lambda: on_click("3")), ("-", lambda: on_click("-")),
    ("0", lambda: on_click("0")), (".", lambda: on_click(".")), ("+", lambda: on_click("+")), ("^", lambda: on_click("^")),
    ("(", lambda: on_click("(")), (")", lambda: on_click(")")), ("√", lambda: on_click("sqrt(")), ("log", lambda: on_click("log(")),
    ("sin", lambda: on_click("sin(")), ("cos", lambda: on_click("cos(")), ("tan", lambda: on_click("tan(")), ("π", lambda: on_click(str(math.pi))),
    ("C", clear), ("←", backspace), ("=", evaluate_expression), ("Theme", toggle_theme)
]

# Create all buttons
for (text, cmd) in buttons:
    create_button(btn_frame, text, cmd)

# Key bindings
root.bind("<Key>", key_handler)

# Initial theme
apply_theme()

# Start the app
root.mainloop()
