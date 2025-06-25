import tkinter as tk
from tkinter import ttk, messagebox, colorchooser
import math

# === Formula dictionaries ===
FORMULAS = {
    "Math": {
        "Circle Area": {
            'vars': ['r', 'A'],
            'inverses': {
                'A': lambda r: 3.1416 * r**2,
                'r': lambda A: (A / 3.1416) ** 0.5,
            }
        },
        "Triangle Area": {
            'vars': ['b', 'h', 'A'],
            'inverses': {
                'A': lambda b, h: 0.5 * b * h,
                'b': lambda A, h: (2 * A) / h,
                'h': lambda A, b: (2 * A) / b,
            }
        },
    },
    "Physics": {
        "Density": {
            'vars': ['m', 'V', 'ρ'],
            'inverses': {
                'ρ': lambda m, V: m / V,
                'm': lambda ρ, V: ρ * V,
                'V': lambda m, ρ: m / ρ,
            }
        },
    }
}

# === More formulas added ===
MORE_FORMULAS_BATCH = {
    "Math": {
        "Square Area": {
            'vars': ['s', 'A'],
            'inverses': {
                'A': lambda s: s**2,
                's': lambda A: A**0.5,
            }
        },
        "Rectangle Area": {
            'vars': ['l', 'w', 'A'],
            'inverses': {
                'A': lambda l, w: l * w,
                'l': lambda A, w: A / w,
                'w': lambda A, l: A / l,
            }
        },
        "Volume of Sphere": {
            'vars': ['r', 'V'],
            'inverses': {
                'V': lambda r: (4/3) * 3.1416 * r**3,
                'r': lambda V: ((3 * V) / (4 * 3.1416)) ** (1/3),
            }
        },
        "Simple Interest": {
            'vars': ['P', 'r', 't', 'I'],
            'inverses': {
                'I': lambda P, r, t: P * r * t,
                'P': lambda I, r, t: I / (r * t),
                'r': lambda I, P, t: I / (P * t),
                't': lambda I, P, r: I / (P * r),
            }
        },
        "Pythagorean Theorem": {
            'vars': ['a', 'b', 'c'],
            'inverses': {
                'c': lambda a, b: (a**2 + b**2) ** 0.5,
                'a': lambda c, b: (c**2 - b**2) ** 0.5,
                'b': lambda c, a: (c**2 - a**2) ** 0.5,
            }
        },
    },
    "Physics": {
        "Force": {
            'vars': ['m', 'a', 'F'],
            'inverses': {
                'F': lambda m, a: m * a,
                'm': lambda F, a: F / a,
                'a': lambda F, m: F / m,
            }
        },
        "Ohm's Law": {
            'vars': ['V', 'I', 'R'],
            'inverses': {
                'V': lambda I, R: I * R,
                'I': lambda V, R: V / R,
                'R': lambda V, I: V / I,
            }
        },
        "Pressure": {
            'vars': ['F', 'A', 'P'],
            'inverses': {
                'P': lambda F, A: F / A,
                'F': lambda P, A: P * A,
                'A': lambda F, P: F / P,
            }
        },
        "Hooke's Law": {
            'vars': ['k', 'x', 'F'],
            'inverses': {
                'F': lambda k, x: k * x,
                'k': lambda F, x: F / x,
                'x': lambda F, k: F / k,
            }
        },
    }
}

for category, formulas in MORE_FORMULAS_BATCH.items():
    FORMULAS.setdefault(category, {}).update(formulas)

# === GUI Class ===
class FormulaSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Formula Solver")
        self.root.geometry("650x520")
        self.root.configure(bg="white")

        self.cat_var = tk.StringVar()
        self.formula_var = tk.StringVar()

        # Category
        ttk.Label(root, text="Category").pack(pady=5)
        self.cat_cb = ttk.Combobox(root, textvariable=self.cat_var, values=list(FORMULAS.keys()), state="readonly")
        self.cat_cb.pack()

        # Formula selection
        ttk.Label(root, text="Formula").pack(pady=5)
        self.formula_cb = ttk.Combobox(root, textvariable=self.formula_var, state="readonly")
        self.formula_cb.pack()

        self.cat_var.trace_add("write", self.update_formulas)
        self.formula_var.trace_add("write", self.prepare_inputs)

        self.input_frame = ttk.Frame(root)
        self.input_frame.pack(pady=10, fill="x")
        self.entries = {}

        ttk.Button(root, text="Solve", command=self.solve).pack(pady=10)
        self.output_label = ttk.Label(root, text="", font=("Arial", 14))
        self.output_label.pack(pady=10)

        # Settings button
        ttk.Button(root, text="Settings", command=self.open_settings).pack(pady=5)

    def update_formulas(self, *_):
        cat = self.cat_var.get()
        if cat in FORMULAS:
            self.formula_cb['values'] = list(FORMULAS[cat].keys())
        else:
            self.formula_cb['values'] = []
        self.formula_var.set('')
        self.clear_inputs()
        self.output_label.config(text="")

    def prepare_inputs(self, *_):
        self.clear_inputs()
        cat = self.cat_var.get()
        formula = self.formula_var.get()
        if not cat or not formula:
            return
        formula_data = FORMULAS[cat][formula]
        for var in formula_data['vars']:
            frame = ttk.Frame(self.input_frame)
            frame.pack(fill="x", pady=2)
            ttk.Label(frame, text=f"{var} = ").pack(side="left")
            entry = ttk.Entry(frame)
            entry.pack(side="left", fill="x", expand=True)
            self.entries[var] = entry
        self.output_label.config(text="")

    def clear_inputs(self):
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        self.entries.clear()

    def solve(self):
        cat = self.cat_var.get()
        formula = self.formula_var.get()
        if not cat or not formula:
            messagebox.showerror("Error", "Please select a category and formula.")
            return

        formula_data = FORMULAS[cat][formula]
        vars_ = formula_data['vars']
        inverses = formula_data['inverses']

        inputs = {}
        empty_vars = []

        for var in vars_:
            val = self.entries[var].get().strip()
            if val == '':
                empty_vars.append(var)
            else:
                try:
                    inputs[var] = float(val)
                except ValueError:
                    messagebox.showerror("Error", f"Invalid value for {var}")
                    return

        if len(empty_vars) != 1:
            messagebox.showerror("Error", "Leave exactly one variable empty.")
            return

        unknown_var = empty_vars[0]
        if unknown_var not in inverses:
            messagebox.showerror("Error", f"Can't solve for '{unknown_var}' in this formula.")
            return

        try:
            args = [inputs[v] for v in vars_ if v != unknown_var]
            result = inverses[unknown_var](*args)
            self.output_label.config(text=f"{unknown_var} = {result:.6g}")
            self.entries[unknown_var].delete(0, tk.END)
            self.entries[unknown_var].insert(0, f"{result:.6g}")
        except Exception as e:
            messagebox.showerror("Error", f"Calculation error: {e}")

    def open_settings(self):
        color = colorchooser.askcolor(title="Select Background Color")[1]
        if color:
            self.root.configure(bg=color)

# === Run the app ===
if __name__ == "__main__":
    root = tk.Tk()
    app = FormulaSolverApp(root)
    root.mainloop()
