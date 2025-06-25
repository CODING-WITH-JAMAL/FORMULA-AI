from tkinter import *
from subprocess import call

# --- Function Definitions ---
def interest(): call(["python", "interest.py"])
def physics(): call(["python", "physics.py"])
def calc(): call(["python", "calc.py"])
def base(): call(["python", "base.py"])
def density(): call(["python", "density.py"])
def custom(): call(["python", "custom.py"])
def volume(): call(["python", "volume graphical.py"])
def pt(): call(["python", "pythagorean theorem.py"])
def physics_two_function(): call(["python", "Physics pro.py"])
def math_two_function(): call(["python", "math pro.py"])
def multiple_one_function(): call(["python", "multiple one.py"])
def multiple_two_function(): call(["python", "multiple two.py"])
def si_one_function(): call(["python", "conversions_file.py"])
def si_two_function(): call(["python", "si units.py"])

# --- Main Window Setup ---
help_window = Tk()
help_window.geometry("400x720")
help_window.title("📘 HELP MENU")
help_window.configure(bg="#1e1e2f")

# --- Header ---
header = Frame(help_window, bg="#282846", pady=20)
header.pack(fill=X)
title = Label(header, text="Available Calculators", bg="#282846", fg="#ffffff",
              font=("Helvetica", 18, "bold"))
title.pack()

# --- Button Frame ---
button_frame = Frame(help_window, bg="#1e1e2f")
button_frame.pack(pady=15)

# Button style settings
btn_font = ("Segoe UI", 10, "bold")
btn_config = {
    "width": 40,
    "font": btn_font,
    "bg": "#2f2f4f",
    "fg": "white",
    "activebackground": "#40e0d0",
    "activeforeground": "#1e1e2f",
    "relief": GROOVE,
    "bd": 2,
    "padx": 5,
    "pady": 4
}

# --- Buttons ---
buttons = [
    ("Interest", interest),
    ("Physics", physics),
    ("Calculator", calc),
    ("Base Conversions", base),
    ("Density, Mass & Volume", density),
    ("Custom Input", custom),
    ("Volume", volume),
    ("Pythagorean Theorem", pt),
    ("Advanced Physics", physics_two_function),
    ("Advanced Math", math_two_function),
    ("Multiple 1", multiple_one_function),
    ("SI Conversions 1", si_one_function),
    ("SI Conversions 2", si_two_function),
    ("Multiple 2", multiple_two_function),
    ("Chemistry", si_two_function)  # Adjust this if it's a different script
]

# --- Place Buttons Dynamically ---
for text, cmd in buttons:
    Button(button_frame, text=text, command=cmd, **btn_config).pack(pady=4)

# --- Footer ---
footer = Label(help_window, text="Enhanced UI • Powered by Tkinter", bg="#1e1e2f", fg="#888",
               font=("Courier", 9))
footer.pack(side=BOTTOM, pady=10)

help_window.mainloop()
