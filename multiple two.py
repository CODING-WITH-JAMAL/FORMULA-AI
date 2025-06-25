import tkinter as tk
from tkinter import ttk
import math
import cmath

# Formula Definitions
formulas = {
    "Kinetic Energy": (lambda m, v: 0.5 * m * v ** 2, ["Mass (kg)", "Velocity (m/s)"]),
    "Potential Energy": (lambda m, g, h: m * g * h, ["Mass (kg)", "Gravity (m/s^2)", "Height (m)"]),
    "Momentum": (lambda m, v: m * v, ["Mass (kg)", "Velocity (m/s)"]),
    "Force": (lambda m, a: m * a, ["Mass (kg)", "Acceleration (m/s^2)"]),
    "Work": (lambda F, d, theta: F * d * math.cos(math.radians(theta)), ["Force (N)", "Distance (m)", "Angle (degrees)"]),
    "Power": (lambda W, t: W / t, ["Work (J)", "Time (s)"]),
    "Acceleration": (lambda F, m: F / m, ["Force (N)", "Mass (kg)"]),
    "Velocity": (lambda d, t: d / t, ["Distance (m)", "Time (s)"]),
    "Displacement": (lambda v_i, v_f, t: 0.5 * (v_i + v_f) * t, ["Initial Velocity (m/s)", "Final Velocity (m/s)", "Time (s)"]),
    "Ohm's Law (Voltage)": (lambda I, R: I * R, ["Current (A)", "Resistance (Ω)"]),
    "Ohm's Law (Current)": (lambda V, R: V / R, ["Voltage (V)", "Resistance (Ω)"]),
    "Ohm's Law (Resistance)": (lambda V, I: V / I, ["Voltage (V)", "Current (A)"])
    # You can expand this with more formulas from the previous list
}

class FormulaSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Formula Solver")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        self.theme = "light"
        self.setup_ui()

    def setup_ui(self):
        self.title_label = tk.Label(self.root, text="Physics & Math Formula Solver", font=("Helvetica", 20, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        self.combo_label = tk.Label(self.root, text="Select Formula:", bg="#f0f0f0")
        self.combo_label.pack()

        self.formula_combo = ttk.Combobox(self.root, values=list(formulas.keys()), state="readonly")
        self.formula_combo.pack(pady=5)
        self.formula_combo.bind("<<ComboboxSelected>>", self.display_inputs)

        self.inputs_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.inputs_frame.pack(pady=20)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="#f0f0f0")
        self.result_label.pack(pady=10)

        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate_result)
        self.calculate_button.pack(pady=5)

        self.theme_button = tk.Button(self.root, text="Switch Theme", command=self.toggle_theme)
        self.theme_button.pack(pady=10)

        self.input_entries = []

    def display_inputs(self, event):
        for widget in self.inputs_frame.winfo_children():
            widget.destroy()

        self.input_entries.clear()
        formula_name = self.formula_combo.get()
        _, labels = formulas[formula_name]

        for label in labels:
            lbl = tk.Label(self.inputs_frame, text=label + ":", bg=self.inputs_frame["bg"])
            lbl.pack()
            entry = tk.Entry(self.inputs_frame)
            entry.pack()
            self.input_entries.append(entry)

    def calculate_result(self):
        formula_name = self.formula_combo.get()
        func, _ = formulas[formula_name]
        try:
            values = [float(entry.get()) for entry in self.input_entries]
            result = func(*values)
            if isinstance(result, tuple):
                result_text = ", ".join(f"{x:.4f}" for x in result)
            else:
                result_text = f"Result: {result:.4f}"
            self.result_label.config(text=result_text)
        except Exception as e:
            self.result_label.config(text=f"Error: {e}")

    def toggle_theme(self):
        if self.theme == "light":
            self.theme = "dark"
            bg_color = "#222222"
            fg_color = "#ffffff"
        else:
            self.theme = "light"
            bg_color = "#f0f0f0"
            fg_color = "#000000"

        self.root.configure(bg=bg_color)
        self.title_label.config(bg=bg_color, fg=fg_color)
        self.combo_label.config(bg=bg_color, fg=fg_color)
        self.result_label.config(bg=bg_color, fg=fg_color)
        self.inputs_frame.config(bg=bg_color)
        for widget in self.inputs_frame.winfo_children():
            widget.config(bg=bg_color, fg=fg_color)

if __name__ == '__main__':
    root = tk.Tk()
    app = FormulaSolverApp(root)
    root.mainloop()
