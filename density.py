import tkinter as tk
from tkinter import ttk, messagebox

class PhysicsSolver(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Physics Solver")
        self.geometry("450x500")
        self.resizable(False, False)
        self.configure(bg="#222831")
        
        self.selected_formula = tk.StringVar(value="Density")
        
        # Dictionary for unit conversion to SI base units
        self.mass_units = {"kg":1, "g":0.001}
        self.volume_units = {"m³":1, "cm³":1e-6}
        self.distance_units = {"m":1, "cm":0.01, "km":1000}
        self.time_units = {"s":1, "min":60, "hr":3600}
        self.speed_units = {"m/s":1, "km/h":1000/3600}
        self.force_units = {"N":1, "kN":1000}
        self.density_units = {"kg/m³":1, "g/cm³":1000}
        self.acceleration_units = {"m/s²":1, "cm/s²":0.01}

        self.create_widgets()
        self.animate_wave()

    def create_widgets(self):
        # Title label
        self.title_label = tk.Label(self, text="Physics Formula Solver", font=("Helvetica", 18, "bold"), fg="#00adb5", bg="#222831")
        self.title_label.pack(pady=10)
        
        # Formula choice dropdown
        formula_options = ["Density", "Mass", "Volume", "Force", "Speed", "Distance", "Time"]
        formula_frame = tk.Frame(self, bg="#222831")
        formula_frame.pack(pady=5)
        tk.Label(formula_frame, text="Select quantity to solve for:", fg="white", bg="#222831", font=("Helvetica", 12)).pack(side="left")
        formula_menu = ttk.Combobox(formula_frame, textvariable=self.selected_formula, values=formula_options, state="readonly", width=10)
        formula_menu.pack(side="left", padx=5)
        formula_menu.bind("<<ComboboxSelected>>", lambda e: self.update_inputs())

        # Frame for inputs
        self.inputs_frame = tk.Frame(self, bg="#393e46")
        self.inputs_frame.pack(pady=10, fill="x", padx=20)

        # Result label
        self.result_label = tk.Label(self, text="", font=("Helvetica", 14, "bold"), fg="#00ff94", bg="#222831")
        self.result_label.pack(pady=10)

        # Solve button
        self.solve_button = tk.Button(self, text="Solve", command=self.solve, bg="#00adb5", fg="white", font=("Helvetica", 12, "bold"))
        self.solve_button.pack(pady=10)

        # Animation canvas at bottom
        self.canvas = tk.Canvas(self, width=450, height=80, bg="#222831", highlightthickness=0)
        self.canvas.pack(side="bottom", fill="x")

        self.update_inputs()

    def clear_inputs(self):
        for widget in self.inputs_frame.winfo_children():
            widget.destroy()

    def update_inputs(self):
        self.clear_inputs()
        solve_for = self.selected_formula.get()

        # We'll create entries for the required variables depending on the formula selected.
        # Each input: Label + Entry + Unit Combobox
        # We keep track of entries and unit selectors for later use.

        self.entries = {}
        self.unit_selectors = {}

        def add_input(name, units_dict):
            frame = tk.Frame(self.inputs_frame, bg="#393e46")
            frame.pack(pady=5, fill="x")
            lbl = tk.Label(frame, text=name+":", fg="white", bg="#393e46", font=("Helvetica", 12))
            lbl.pack(side="left")
            ent = tk.Entry(frame, font=("Helvetica", 12), width=10)
            ent.pack(side="left", padx=5)
            unit_var = tk.StringVar(value=list(units_dict.keys())[0])
            unit_menu = ttk.Combobox(frame, textvariable=unit_var, values=list(units_dict.keys()), state="readonly", width=6)
            unit_menu.pack(side="left")
            self.entries[name] = ent
            self.unit_selectors[name] = (unit_var, units_dict)

        # Depending on the quantity to solve for, add input fields:

        if solve_for == "Density":
            add_input("Mass", self.mass_units)
            add_input("Volume", self.volume_units)

        elif solve_for == "Mass":
            add_input("Density", self.density_units)
            add_input("Volume", self.volume_units)

        elif solve_for == "Volume":
            add_input("Mass", self.mass_units)
            add_input("Density", self.density_units)

        elif solve_for == "Force":
            add_input("Mass", self.mass_units)
            add_input("Acceleration", self.acceleration_units)

        elif solve_for == "Speed":
            add_input("Distance", self.distance_units)
            add_input("Time", self.time_units)

        elif solve_for == "Distance":
            add_input("Speed", self.speed_units)
            add_input("Time", self.time_units)

        elif solve_for == "Time":
            add_input("Distance", self.distance_units)
            add_input("Speed", self.speed_units)

        self.result_label.config(text="")
    
    def validate_and_get(self, name):
        entry = self.entries[name]
        unit_var, units_dict = self.unit_selectors[name]
        try:
            val = float(entry.get())
            if val < 0:
                raise ValueError
            val_SI = val * units_dict[unit_var.get()]
            return val_SI
        except ValueError:
            messagebox.showerror("Input error", f"Please enter a valid positive number for {name}.")
            return None

    def solve(self):
        solve_for = self.selected_formula.get()
        
        # Gather inputs, convert to SI
        inputs = {}
        for key in self.entries:
            val = self.validate_and_get(key)
            if val is None:
                return
            inputs[key] = val

        try:
            if solve_for == "Density":
                density = inputs["Mass"] / inputs["Volume"]
                unit = "kg/m³"
                display = f"Density = {density:.4f} {unit}"

            elif solve_for == "Mass":
                mass = inputs["Density"] * inputs["Volume"]
                unit = "kg"
                display = f"Mass = {mass:.4f} {unit}"

            elif solve_for == "Volume":
                volume = inputs["Mass"] / inputs["Density"]
                unit = "m³"
                display = f"Volume = {volume:.6f} {unit}"

            elif solve_for == "Force":
                force = inputs["Mass"] * inputs["Acceleration"]
                unit = "N"
                display = f"Force = {force:.4f} {unit}"

            elif solve_for == "Speed":
                speed = inputs["Distance"] / inputs["Time"]
                unit = "m/s"
                display = f"Speed = {speed:.4f} {unit}"

            elif solve_for == "Distance":
                distance = inputs["Speed"] * inputs["Time"]
                unit = "m"
                display = f"Distance = {distance:.4f} {unit}"

            elif solve_for == "Time":
                time = inputs["Distance"] / inputs["Speed"]
                unit = "s"
                display = f"Time = {time:.4f} {unit}"

            else:
                display = "Formula not recognized."
            
            self.result_label.config(text=display)
            self.animate_result()
        
        except ZeroDivisionError:
            messagebox.showerror("Math error", "Division by zero occurred in calculation.")

    def animate_wave(self):
        # A simple horizontal moving wave animation on the bottom canvas
        self.canvas.delete("all")
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        self.wave_points = []
        step = 10
        import math
        for x in range(0, width + step, step):
            y = height/2 + 10 * math.sin((x + getattr(self, 'wave_shift', 0))/20)
            self.wave_points.append((x, y))
        self.wave_shift = (getattr(self, 'wave_shift', 0) + 3) % 360

        points = []
        for x, y in self.wave_points:
            points.extend([x, y])
        self.canvas.create_line(points, fill="#00adb5", width=3, smooth=True)

        self.after(50, self.animate_wave)

    def animate_result(self):
        # Simple flash animation on result label
        def flash(count=0):
            colors = ["#00ff94", "#00adb5"]
            self.result_label.config(fg=colors[count % 2])
            if count < 6:
                self.after(300, flash, count+1)
            else:
                self.result_label.config(fg="#00ff94")
        flash()


if __name__ == "__main__":
    app = PhysicsSolver()
    app.mainloop()
