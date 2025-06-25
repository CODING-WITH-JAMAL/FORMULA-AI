# Formula Solver with Tkinter GUI, Animation, Keyboard, and Themes
import tkinter as tk
from tkinter import ttk
import math

# Define some formulas for demonstration
FORMULAS = {
    'Area of Circle (πr²)': lambda r: math.pi * r**2,
    'Circumference of Circle (2πr)': lambda r: 2 * math.pi * r,
    'Area of Rectangle (l×w)': lambda l, w: l * w,
    'Speed = Distance / Time': lambda d, t: d / t,
    'Force = Mass × Acceleration': lambda m, a: m * a,
    'Density = Mass / Volume': lambda m, v: m / v,
    'Kinetic Energy = 0.5mv²': lambda m, v: 0.5 * m * v**2,
    'Potential Energy = mgh': lambda m, g, h: m * g * h,
    'Ohm\'s Law (V = IR)': lambda i, r: i * r,
    'Work = Force × Distance': lambda f, d: f * d,
    # Add more to reach 100 as needed
}

# Define themes
THEMES = {
    'Light': {'bg': '#ffffff', 'fg': '#000000'},
    'Dark': {'bg': '#2e2e2e', 'fg': '#ffffff'},
    'Blue': {'bg': '#e6f0ff', 'fg': '#003366'}
}

class FormulaSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math & Physics Formula Solver")
        self.root.geometry("800x600")
        self.theme = 'Light'
        self.build_ui()
        self.set_theme(self.theme)
        self.bind_keys()

    def build_ui(self):
        self.style = ttk.Style(self.root)
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill='both', expand=True, padx=20, pady=20)

        self.instructions = tk.Label(self.frame, text="Select a formula and input required values below:", font=('Arial', 12, 'italic'))
        self.instructions.pack(pady=5)

        self.formula_var = tk.StringVar()
        self.formula_dropdown = ttk.Combobox(self.frame, textvariable=self.formula_var, width=50)
        self.formula_dropdown['values'] = list(FORMULAS.keys())
        self.formula_dropdown.current(0)
        self.formula_dropdown.pack(pady=10)

        self.entry_frame = tk.Frame(self.frame)
        self.entry_frame.pack()

        self.input_vars = []
        self.input_entries = []
        self.update_input_fields()
        self.formula_var.trace('w', lambda *args: self.update_input_fields())

        self.result_label = tk.Label(self.frame, text="Result: ", font=('Arial', 14))
        self.result_label.pack(pady=10)

        self.calc_button = ttk.Button(self.frame, text="Solve", command=self.calculate_result)
        self.calc_button.pack()

        self.theme_menu = ttk.Combobox(self.frame, values=list(THEMES.keys()))
        self.theme_menu.set(self.theme)
        self.theme_menu.pack(pady=10)
        self.theme_menu.bind("<<ComboboxSelected>>", self.change_theme)

        self.canvas = tk.Canvas(self.frame, width=600, height=250, bg='white')
        self.canvas.pack(pady=10)

        self.hint_label = tk.Label(self.frame, text="Keyboard Shortcuts: Press Enter to Calculate, F1–F3 to Change Theme", font=('Arial', 10))
        self.hint_label.pack(pady=5)

    def update_input_fields(self):
        for entry in self.input_entries:
            entry.destroy()
        self.input_entries.clear()
        self.input_vars.clear()

        formula_name = self.formula_var.get()
        func = FORMULAS.get(formula_name)
        arg_count = func.__code__.co_argcount

        for i in range(arg_count):
            var = tk.StringVar()
            self.input_vars.append(var)
            entry = ttk.Entry(self.entry_frame, textvariable=var, width=15)
            entry.grid(row=0, column=i, padx=5)
            entry.insert(0, f"Input {i+1}")
            self.input_entries.append(entry)

    def calculate_result(self):
        formula_name = self.formula_var.get()
        try:
            args = [float(var.get()) for var in self.input_vars]
            result = FORMULAS[formula_name](*args)
            self.result_label.config(text=f"Result: {result:.3f}")
            self.animate_result(result)
        except Exception as e:
            self.result_label.config(text="Error: Invalid input")

    def animate_result(self, result):
        self.canvas.delete("all")
        height = 200
        max_val = 500
        bar_len = min(result, max_val)
        color = 'green' if result < max_val else 'red'
        self.canvas.create_rectangle(50, height - 20, 50 + bar_len, height - 80, fill=color)
        self.canvas.create_text(300, height - 100, text=f"Visual Output = {result:.2f}", font=('Arial', 14))

        self.canvas.create_oval(550, 50, 580, 80, fill='blue')  # Extra graphic
        self.canvas.create_text(565, 90, text='✔', font=('Arial', 10))

    def change_theme(self, event=None):
        selected = self.theme_menu.get()
        self.set_theme(selected)

    def set_theme(self, theme_name):
        colors = THEMES[theme_name]
        self.frame.config(bg=colors['bg'])
        self.canvas.config(bg=colors['bg'])
        self.result_label.config(bg=colors['bg'], fg=colors['fg'])
        self.instructions.config(bg=colors['bg'], fg=colors['fg'])
        self.hint_label.config(bg=colors['bg'], fg=colors['fg'])
        self.theme = theme_name

    def bind_keys(self):
        self.root.bind('<Return>', lambda e: self.calculate_result())
        self.root.bind('<F1>', lambda e: self.theme_menu.set('Light') or self.set_theme('Light'))
        self.root.bind('<F2>', lambda e: self.theme_menu.set('Dark') or self.set_theme('Dark'))
        self.root.bind('<F3>', lambda e: self.theme_menu.set('Blue') or self.set_theme('Blue'))


if __name__ == '__main__':
    root = tk.Tk()
    app = FormulaSolverApp(root)
    root.mainloop()
