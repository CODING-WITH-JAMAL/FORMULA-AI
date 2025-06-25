import tkinter as tk
from tkinter import messagebox
import re

# ---------------- Periodic Table ----------------
periodic_table = {
    "H": 1.008, "He": 4.0026, "Li": 6.94, "Be": 9.0122,
    "B": 10.81, "C": 12.01, "N": 14.01, "O": 16.00, "F": 19.00,
    "Ne": 20.18, "Na": 22.99, "Mg": 24.31, "Al": 26.98, "Si": 28.09,
    "P": 30.97, "S": 32.06, "Cl": 35.45, "Ar": 39.95, "K": 39.10,
    "Ca": 40.08, "Sc": 44.96, "Ti": 47.87, "V": 50.94, "Cr": 52.00,
    "Mn": 54.94, "Fe": 55.85, "Co": 58.93, "Ni": 58.69, "Cu": 63.55,
    "Zn": 65.38, "Ga": 69.72, "Ge": 72.63, "As": 74.92, "Se": 78.96,
    "Br": 79.90, "Kr": 83.80, "Rb": 85.47, "Sr": 87.62, "Y": 88.91,
    "Zr": 91.22, "Nb": 92.91, "Mo": 95.95, "Ru": 101.07, "Rh": 102.91,
    "Pd": 106.42, "Ag": 107.87, "Cd": 112.41, "In": 114.82, "Sn": 118.71,
    "Sb": 121.76, "I": 126.90, "Te": 127.60, "Xe": 131.29, "Cs": 132.91,
    "Ba": 137.33, "La": 138.91, "Ce": 140.12, "Pr": 140.91, "Nd": 144.24,
    "Sm": 150.36, "Eu": 151.96, "Gd": 157.25, "Tb": 158.93, "Dy": 162.50,
    "Ho": 164.93, "Er": 167.26, "Tm": 168.93, "Yb": 173.05, "Lu": 174.97,
    "Hf": 178.49, "Ta": 180.95, "W": 183.84, "Re": 186.21, "Os": 190.23,
    "Ir": 192.22, "Pt": 195.08, "Au": 196.97, "Hg": 200.59, "Tl": 204.38,
    "Pb": 207.2, "Bi": 208.98
}

# ---------------- Chemistry Parser ----------------
def compute_molar_mass(formula):
    def parse(tokens):
        stack = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == '(':
                # Handle group in parentheses
                sub_expr = []
                i += 1
                depth = 1
                while i < len(tokens) and depth > 0:
                    if tokens[i] == '(':
                        depth += 1
                    elif tokens[i] == ')':
                        depth -= 1
                    if depth > 0:
                        sub_expr.append(tokens[i])
                    i += 1
                multiplier = 1
                if i < len(tokens) and tokens[i].isdigit():
                    multiplier = int(tokens[i])
                    i += 1
                stack.append(parse(sub_expr) * multiplier)
            elif re.match(r'[A-Z][a-z]?', token):
                # Handle single element
                element = token
                i += 1
                count = 1
                if i < len(tokens) and tokens[i].isdigit():
                    count = int(tokens[i])
                    i += 1
                if element not in periodic_table:
                    raise ValueError(f"Unknown element: {element}")
                stack.append(periodic_table[element] * count)
            elif token == '·':
                i += 1  # Skip hydration dot
            else:
                i += 1
        return sum(stack)

    # Handle hydrates (e.g., CuSO4·5H2O)
    formula = formula.replace("·", "·")
    parts = formula.split("·")
    total_mass = 0
    for part in parts:
        tokens = re.findall(r'[A-Z][a-z]?|\d+|\(|\)|·', part)
        total_mass += parse(tokens)
    return total_mass

# ---------------- GUI Logic ----------------
def calculate():
    formula = entry.get()
    if not formula.strip():
        messagebox.showwarning("Input Error", "Please enter a chemical formula.")
        return
    try:
        mass = compute_molar_mass(formula)
        result_label.config(text=f"Molar Mass: {mass:.3f} g/mol")
    except Exception as e:
        result_label.config(text="")
        messagebox.showerror("Error", f"Invalid formula:\n{e}")

def clear():
    entry.delete(0, tk.END)
    result_label.config(text="")

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("Chemical Formula Solver")
root.geometry("460x250")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Enter Chemical Formula:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(frame, font=("Arial", 16), width=30)
entry.pack()

btn_frame = tk.Frame(frame)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Calculate", font=("Arial", 12), width=12, command=calculate).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Clear", font=("Arial", 12), width=8, command=clear).pack(side=tk.LEFT, padx=5)

result_label = tk.Label(frame, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

root.mainloop()
