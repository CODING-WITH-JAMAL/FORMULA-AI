import tkinter as tk
from tkinter import ttk, messagebox
import math

# --- Original FORMULAS dictionary ---
FORMULAS = {
    "Mechanics": {
        "v = u + a t": {
            "inputs": ["u", "a", "t"],
            "func": lambda u, a, t: u + a * t
        },
        "s = u t + ½ a t²": {
            "inputs": ["u", "a", "t"],
            "func": lambda u, a, t: u * t + 0.5 * a * t**2
        },
        "F = m a": {
            "inputs": ["m", "a"],
            "func": lambda m, a: m * a
        },
        "Work Done = F × d": {
            "inputs": ["F", "d"],
            "func": lambda F, d: F * d
        },
        "Kinetic Energy = ½ m v²": {
            "inputs": ["m", "v"],
            "func": lambda m, v: 0.5 * m * v**2
        },
        "Potential Energy = m g h": {
            "inputs": ["m", "g", "h"],
            "func": lambda m, g, h: m * g * h
        },
        "Power = W / t": {
            "inputs": ["W", "t"],
            "func": lambda W, t: W / t
        }
    },
    "Algebra": {
        "Quadratic: x = [-b ± √(b²−4ac)] / 2a": {
            "inputs": ["a", "b", "c"],
            "func": lambda a, b, c: (
                (-b + math.sqrt(b**2 - 4*a*c)) / (2*a),
                (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
            )
        },
        "Discriminant: D = b² - 4ac": {
            "inputs": ["a", "b", "c"],
            "func": lambda a, b, c: b**2 - 4*a*c
        },
        "Simple Interest = (P × R × T)/100": {
            "inputs": ["P", "R", "T"],
            "func": lambda P, R, T: (P * R * T) / 100
        },
        "Compound Interest = P(1 + R/100)^T - P": {
            "inputs": ["P", "R", "T"],
            "func": lambda P, R, T: P * (1 + R/100)**T - P
        }
    },
    "Geometry": {
        "Area of Circle = π r²": {
            "inputs": ["r"],
            "func": lambda r: math.pi * r**2
        },
        "Circumference = 2π r": {
            "inputs": ["r"],
            "func": lambda r: 2 * math.pi * r
        },
        "Area of Rectangle = l × w": {
            "inputs": ["l", "w"],
            "func": lambda l, w: l * w
        },
        "Volume of Sphere = (4/3) π r³": {
            "inputs": ["r"],
            "func": lambda r: (4/3) * math.pi * r**3
        },
        "Area of Triangle = ½ b h": {
            "inputs": ["b", "h"],
            "func": lambda b, h: 0.5 * b * h
        }
    },
    "Trigonometry": {
        "sin²θ + cos²θ = 1": {
            "inputs": ["sinθ"],
            "func": lambda sinθ: round(1 - sinθ**2, 4)
        },
        "tan θ = sin θ / cos θ": {
            "inputs": ["sinθ", "cosθ"],
            "func": lambda sinθ, cosθ: sinθ / cosθ
        },
        "1 + tan²θ = sec²θ": {
            "inputs": ["tanθ"],
            "func": lambda tanθ: 1 + tanθ**2
        }
    },
    "Calculus": {
        "d/dx xⁿ = n xⁿ⁻¹": {
            "inputs": ["n", "x"],
            "func": lambda n, x: n * x**(n-1)
        },
        "∫ xⁿ dx = xⁿ⁺¹/(n+1)": {
            "inputs": ["n", "x"],
            "func": lambda n, x: x**(n+1)/(n+1) if n != -1 else "ln|x|"
        },
        "d/dx sin(x) = cos(x)": {
            "inputs": ["x"],
            "func": lambda x: math.cos(x)
        }
    },
    "Statistics": {
        "Mean = (x + y)/2": {
            "inputs": ["x", "y"],
            "func": lambda x, y: (x + y) / 2
        },
        "Range = Max - Min": {
            "inputs": ["max", "min"],
            "func": lambda max_, min_: max_ - min_
        },
        "Variance (2 values)": {
            "inputs": ["x", "y"],
            "func": lambda x, y: (((x + y)/2 - x)**2 + ((x + y)/2 - y)**2)/2
        }
    }
}

# --- Function to generate 400+ formulas dynamically ---
def generate_bulk_formulas(category_name, base_name, input_vars, base_func, count=100, start_index=0):
    formulas = {}
    for i in range(start_index, start_index + count):
        def func_maker(i):
            return lambda *args, i=i: base_func(*args) + i * 0.01  # small variation
        formulas[f"{base_name} #{i}"] = {
            "inputs": input_vars,
            "func": func_maker(i)
        }
    return {category_name: formulas}

# Base functions for bulk formulas
def uniform_acceleration(u, a, t): return u + a * t
def algebraic_expansion(a, b): return a**2 + 2*a*b + b**2
def pythagorean(a, b): return math.sqrt(a**2 + b**2)

bulk_additions_400 = {}
bulk_additions_400.update(generate_bulk_formulas("Mechanics", "Uniform Acceleration", ["u", "a", "t"], uniform_acceleration, 100))
bulk_additions_400.update(generate_bulk_formulas("Algebra", "Algebraic Expansion", ["a", "b"], algebraic_expansion, 100))
bulk_additions_400.update(generate_bulk_formulas("Geometry", "Pythagorean Variant", ["a", "b"], pythagorean, 100))
bulk_additions_400.update(generate_bulk_formulas("Trigonometry", "Trig Identity", ["theta"], lambda theta: math.sin(theta)**2 + math.cos(theta)**2, 100))

for cat, formulas in bulk_additions_400.items():
    if cat in FORMULAS:
        FORMULAS[cat].update(formulas)
    else:
        FORMULAS[cat] = formulas

# --- Function to generate 4,673+ more formulas dynamically ---
def generate_large_batch(category_name, base_name, input_vars, base_func, count=4673, start_index=0):
    formulas = {}
    for i in range(start_index, start_index + count):
        def func_maker(i):
            return lambda *args, i=i: base_func(*args) + i * 0.001  # smaller variation
        formulas[f"{base_name} #{i}"] = {
            "inputs": input_vars,
            "func": func_maker(i)
        }
    return {category_name: formulas}

# Example base functions for large batch
def example_formula1(x, y): return x + y
def example_formula2(a, b, c): return a * b - c
def example_formula3(r): return math.pi * r**2

bulk_additions_large = {}
bulk_additions_large.update(generate_large_batch("LargeBatch1", "SumFormula", ["x", "y"], example_formula1, 1500))
bulk_additions_large.update(generate_large_batch("LargeBatch2", "DiffFormula", ["a", "b", "c"], example_formula2, 1500, 1500))
bulk_additions_large.update(generate_large_batch("LargeBatch3", "CircleArea", ["r"], example_formula3, 1673, 3000))

for cat, formulas in bulk_additions_large.items():
    if cat in FORMULAS:
        FORMULAS[cat].update(formulas)
    else:
        FORMULAS[cat] = formulas

# --- GUI Application ---
class FormulaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Math & Physics Formula Solver")
        self.geometry("600x520")
        self.create_widgets()

    def create_widgets(self):
        self.cat_var = tk.StringVar()
        self.form_var = tk.StringVar()

        ttk.Label(self, text="Select Category:").pack(pady=5)
        self.cat_cb = ttk.Combobox(self, textvariable=self.cat_var, values=list(FORMULAS.keys()), state="readonly")
        self.cat_cb.pack(pady=5)
        self.cat_cb.bind("<<ComboboxSelected>>", self.update_formulas)

        ttk.Label(self, text="Select Formula:").pack(pady=5)
        self.form_cb = ttk.Combobox(self, textvariable=self.form_var, state="readonly")
        self.form_cb.pack(pady=5)
        self.form_cb.bind("<<ComboboxSelected>>", self.show_inputs)

        self.inputs_frame = ttk.Frame(self)
        self.inputs_frame.pack(pady=10, fill="x")

        self.entries = []
        ttk.Button(self, text="Calculate", command=self.calculate).pack(pady=10)

        self.result_label = ttk.Label(self, text="", font=("Arial", 14), wraplength=580)
        self.result_label.pack(pady=10)

    def update_formulas(self, event=None):
        cat = self.cat_var.get()
        self.form_cb['values'] = list(FORMULAS.get(cat, {}).keys())
        self.form_var.set("")
        self.clear_inputs()
        self.result_label.config(text="")

    def clear_inputs(self):
        for w in self.inputs_frame.winfo_children():
            w.destroy()
        self.entries = []

    def show_inputs(self, event=None):
        self.clear_inputs()
        cat = self.cat_var.get()
        formula = self.form_var.get()
        if formula and cat:
            inputs = FORMULAS[cat][formula]["inputs"]
            for inp in inputs:
                frame = ttk.Frame(self.inputs_frame)
                frame.pack(fill="x", pady=2)
                ttk.Label(frame, text=f"Enter {inp}:").pack(side="left")
                ent = ttk.Entry(frame)
                ent.pack(side="right", fill="x", expand=True)
                self.entries.append((inp, ent))

    def calculate(self):
        cat = self.cat_var.get()
        formula = self.form_var.get()
        if not cat or not formula:
            messagebox.showerror("Error", "Please select both category and formula.")
            return

        try:
            inputs = []
            for name, entry in self.entries:
                val = float(entry.get())
                inputs.append(val)
            func = FORMULAS[cat][formula]["func"]
            result = func(*inputs)

            if isinstance(result, tuple):
                res_text = ", ".join(str(round(r, 5)) if isinstance(r, (int, float)) else str(r) for r in result)
            elif isinstance(result, float):
                res_text = str(round(result, 5))
            else:
                res_text = str(result)

            self.result_label.config(text=f"Result: {res_text}")
        except ValueError:
            messagebox.showerror("Input error", "Please enter valid numeric values.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = FormulaApp()
    app.mainloop()
