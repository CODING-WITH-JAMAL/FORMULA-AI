import tkinter as tk
from tkinter import ttk, messagebox
from subprocess import call

# === MAIN WINDOW SETUP ===
main_window = tk.Tk()
main_window.title("MATH AI - Enhanced")
main_window.geometry("600x400")
main_window.configure(bg="#2b2b2b")



def base_function():
    class BaseConverterAI:
        def __init__(self):
            pass
    
        def validate_number(self, number_str, base):
            """Validate if the number_str is valid in the given base"""
            try:
                int(number_str, base)
                return True
            except ValueError:
                return False
    
        def convert(self, number_str, from_base, to_base):
            """
            Convert number_str from from_base to to_base.
            Supports bases from 2 to 36.
            """
            if not (2 <= from_base <= 36) or not (2 <= to_base <= 36):
                raise ValueError("Bases must be between 2 and 36 inclusive.")
    
            if not self.validate_number(number_str, from_base):
                raise ValueError(f"Invalid number '{number_str}' for base {from_base}.")
    
            # Convert from from_base to decimal
            decimal_value = int(number_str, from_base)
    
            # Convert from decimal to to_base
            if decimal_value == 0:
                return '0'
    
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result = ""
            num = decimal_value
            while num > 0:
                result = digits[num % to_base] + result
                num //= to_base
    
            return result
    
        def interactive(self):
            print("Welcome to BaseConverterAI!")
            print("Enter 'exit' to quit.")
            while True:
                number_str = input("Enter the number to convert: ").strip()
                if number_str.lower() == 'exit':
                    print("Goodbye!")
                    break
                from_base = input("Enter the base of the number (2-36): ").strip()
                to_base = input("Enter the base to convert to (2-36): ").strip()
    
                try:
                    from_base = int(from_base)
                    to_base = int(to_base)
                    converted = self.convert(number_str, from_base, to_base)
                    print(f"{number_str} (base {from_base}) = {converted} (base {to_base})")
                except ValueError as e:
                    print(f"Error: {e}")
    
    if __name__ == "__main__":
        ai = BaseConverterAI()
        ai.interactive()
    

def custom_function():
    call(["python", "custom2.py"])

    
def volume_function():
    
    call(["python", "volume graphical.py"])
    
def velocity_function():
    import math
    
    def calculate_velocity():
        print("Velocity Calculator")
        print("Choose a formula to calculate velocity:")
        print("1. Basic velocity (v = d/t)")
        print("2. Final velocity with acceleration (v = u + at)")
        print("3. Final velocity with displacement (vÂ² = uÂ² + 2as)")
        print("4. Average velocity (v_avg = (u + v)/2)")
        print("5. Circular motion velocity (v = 2�€r/T)")
        print("6. Escape velocity (v = âˆš(2GM/r))")
        print("7. Wave velocity (v = Î»f)")
        print("8. Velocity from kinetic energy (v = âˆš(2KE/m))")
        
        try:
            choice = int(input("Enter your choice (1-8): "))
            
            if choice == 1:
                # Basic velocity: v = d/t
                distance = float(input("Enter distance (meters): "))
                time = float(input("Enter time (seconds): "))
                velocity = distance / time
                print(f"Velocity: {velocity:.2f} m/s")
                
            elif choice == 2:
                # Final velocity with acceleration: v = u + at
                initial_velocity = float(input("Enter initial velocity (m/s): "))
                acceleration = float(input("Enter acceleration (m/sÂ²): "))
                time = float(input("Enter time (seconds): "))
                velocity = initial_velocity + (acceleration * time)
                print(f"Final velocity: {velocity:.2f} m/s")
                
            elif choice == 3:
                # Final velocity with displacement: vÂ² = uÂ² + 2as
                initial_velocity = float(input("Enter initial velocity (m/s): "))
                acceleration = float(input("Enter acceleration (m/sÂ²): "))
                displacement = float(input("Enter displacement (meters): "))
                velocity = math.sqrt(initial_velocity**2 + 2 * acceleration * displacement)
                print(f"Final velocity: {velocity:.2f} m/s")
                
            elif choice == 4:
                # Average velocity: v_avg = (u + v)/2
                initial_velocity = float(input("Enter initial velocity (m/s): "))
                final_velocity = float(input("Enter final velocity (m/s): "))
                velocity = (initial_velocity + final_velocity) / 2
                print(f"Average velocity: {velocity:.2f} m/s")
                
            elif choice == 5:
                # Circular motion velocity: v = 2�€r/T
                radius = float(input("Enter radius of circular path (meters): "))
                period = float(input("Enter period (seconds): "))
                velocity = (2 * math.pi * radius) / period
                print(f"Circular velocity: {velocity:.2f} m/s")
                
            elif choice == 6:
                # Escape velocity: v = âˆš(2GM/r)
                G = 6.67430e-11  # gravitational constant
                mass = float(input("Enter mass of the planet (kg): "))
                radius = float(input("Enter radius of the planet (meters): "))
                velocity = math.sqrt((2 * G * mass) / radius)
                print(f"Escape velocity: {velocity:.2f} m/s")
                
            elif choice == 7:
                # Wave velocity: v = Î»f
                wavelength = float(input("Enter wavelength (meters): "))
                frequency = float(input("Enter frequency (Hz): "))
                velocity = wavelength * frequency
                print(f"Wave velocity: {velocity:.2f} m/s")
                
            elif choice == 8:
                # Velocity from kinetic energy: v = âˆš(2KE/m)
                kinetic_energy = float(input("Enter kinetic energy (Joules): "))
                mass = float(input("Enter mass (kg): "))
                velocity = math.sqrt((2 * kinetic_energy) / mass)
                print(f"Velocity: {velocity:.2f} m/s")
                
            else:
                print("Invalid choice. Please select a number between 1 and 8.")
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if __name__ == "__main__":
        while True:
            calculate_velocity()
            another = input("\nCalculate another velocity? (y/n): ").lower()
            if another != 'y':
                print("Goodbye!")
                break
            
def pythagorean_theorem_function():
    import tkinter as tk
    import math
    
    def calculate():
        """Calculates the missing side of a right triangle."""
        try:
            side_a = float(entry_a.get()) if entry_a.get() else None
            side_b = float(entry_b.get()) if entry_b.get() else None
            side_c = float(entry_c.get()) if entry_c.get() else None
    
            if side_a is not None and side_b is not None:
                # Calculate hypotenuse (c)
                c = math.sqrt(side_a**2 + side_b**2)
                result_label.config(text=f"Hypotenuse (c): {c:.2f}")
            elif side_a is not None and side_c is not None:
                # Calculate side b
                if side_c <= side_a:
                    result_label.config(text="Error: Hypotenuse must be greater than side a")
                    return
                b = math.sqrt(side_c**2 - side_a**2)
                result_label.config(text=f"Side b: {b:.2f}")
            elif side_b is not None and side_c is not None:
                # Calculate side a
                if side_c <= side_b:
                    result_label.config(text="Error: Hypotenuse must be greater than side b")
                    return
                a = math.sqrt(side_c**2 - side_b**2)
                result_label.config(text=f"Side a: {a:.2f}")
            else:
                result_label.config(text="Enter at least two values to calculate")
    
        except ValueError:
            result_label.config(text="Error: Please enter valid numbers")
        except Exception as e:
            result_label.config(text=f"An error occurred: {e}")
    
    # Create the main window
    root = tk.Tk()
    root.title("Pythagorean Theorem Calculator")
    
    # Create labels and entry fields for side a, b, and c
    label_a = tk.Label(root, text="Side a:")
    label_a.grid(row=0, column=0, padx=5, pady=5)
    entry_a = tk.Entry(root)
    entry_a.grid(row=0, column=1, padx=5, pady=5)
    
    label_b = tk.Label(root, text="Side b:")
    label_b.grid(row=1, column=0, padx=5, pady=5)
    entry_b = tk.Entry(root)
    entry_b.grid(row=1, column=1, padx=5, pady=5)
    
    label_c = tk.Label(root, text="Hypotenuse (c):")
    label_c.grid(row=2, column=0, padx=5, pady=5)
    entry_c = tk.Entry(root)
    entry_c.grid(row=2, column=1, padx=5, pady=5)
    
    # Create a button to perform the calculation
    calculate_button = tk.Button(root, text="Calculate", command=calculate)
    calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
    
    # Create a label to display the result
    result_label = tk.Label(root, text="Result: ")
    result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    
    # Run the Tkinter event loop
    root.mainloop()

    
def density_function():
    import tkinter as tk
    from tkinter import ttk, messagebox
    import math
    
    # Define formula logic
    FORMULAS = {
        "Density (D = M / V)": {
            "variables": {
                "Density (D)": lambda M, V: float(M) / float(V),
                "Mass (M)": lambda D, V: float(D) * float(V),
                "Volume (V)": lambda M, D: float(M) / float(D)
            },
            "inputs": ["Density (D)", "Mass (M)", "Volume (V)"]
        },
        "Speed (S = D / T)": {
            "variables": {
                "Speed (S)": lambda D, T: float(D) / float(T),
                "Distance (D)": lambda S, T: float(S) * float(T),
                "Time (T)": lambda D, S: float(D) / float(S)
            },
            "inputs": ["Speed (S)", "Distance (D)", "Time (T)"]
        },
        "Force (F = M * A)": {
            "variables": {
                "Force (F)": lambda M, A: float(M) * float(A),
                "Mass (M)": lambda F, A: float(F) / float(A),
                "Acceleration (A)": lambda F, M: float(F) / float(M)
            },
            "inputs": ["Force (F)", "Mass (M)", "Acceleration (A)"]
        }
    }
    
    class FormulaSolverApp:
        def __init__(self, root):
            self.root = root
            self.root.title("DENSITY, SPEED and TIME")
    
            self.formula_var = tk.StringVar()
            self.target_var = tk.StringVar()
            self.entries = {}
    
            self.create_widgets()
    
        def create_widgets(self):
            ttk.Label(self.root, text="Select Formula:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
            self.formula_menu = ttk.Combobox(self.root, textvariable=self.formula_var, values=list(FORMULAS.keys()), width=30)
            self.formula_menu.grid(row=0, column=1, padx=10, pady=5)
            self.formula_menu.bind("<<ComboboxSelected>>", self.update_target_options)
    
            ttk.Label(self.root, text="Calculate:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
            self.target_menu = ttk.Combobox(self.root, textvariable=self.target_var, width=30)
            self.target_menu.grid(row=1, column=1, padx=10, pady=5)
            self.target_menu.bind("<<ComboboxSelected>>", self.generate_inputs)
    
            self.input_frame = tk.Frame(self.root)
            self.input_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    
            self.calc_button = ttk.Button(self.root, text="Calculate", command=self.calculate)
            self.calc_button.grid(row=3, column=0, columnspan=2, pady=10)
    
            self.result_label = ttk.Label(self.root, text="Result: ", font=("Arial", 12, "bold"))
            self.result_label.grid(row=4, column=0, columnspan=2, pady=10)
    
        def update_target_options(self, event=None):
            selected_formula = self.formula_var.get()
            if selected_formula in FORMULAS:
                options = list(FORMULAS[selected_formula]["variables"].keys())
                self.target_menu["values"] = options
                self.target_menu.set("")
    
        def generate_inputs(self, event=None):
            for widget in self.input_frame.winfo_children():
                widget.destroy()
            self.entries.clear()
    
            selected_formula = self.formula_var.get()
            selected_target = self.target_var.get()
    
            if not selected_formula or not selected_target:
                return
    
            all_vars = FORMULAS[selected_formula]["inputs"]
            input_vars = [v for v in all_vars if v != selected_target]
    
            for i, var in enumerate(input_vars):
                ttk.Label(self.input_frame, text=var + ":").grid(row=i, column=0, sticky="w")
                entry = ttk.Entry(self.input_frame)
                entry.grid(row=i, column=1, pady=2)
                self.entries[var] = entry
    
        def calculate(self):
            selected_formula = self.formula_var.get()
            target = self.target_var.get()
            inputs = {}
    
            try:
                for var, entry in self.entries.items():
                    val = float(entry.get())
                    inputs[var] = val
    
                calc_fn = FORMULAS[selected_formula]["variables"][target]
                arg_order = [v for v in FORMULAS[selected_formula]["inputs"] if v != target]
                args = [inputs[v] for v in arg_order]
                result = calc_fn(*args)
    
                self.result_label.config(text=f"Result: {result:.4f}")
            except Exception as e:
                messagebox.showerror("Error", f"Calculation error: {str(e)}")
    
    # Run the app
    if __name__ == "__main__":
        root = tk.Tk()
        app = FormulaSolverApp(root)
        root.mainloop()

    
    def calculate_density(mass, volume):
        """
        Calculates the density of an object given its mass and volume.
    
        Args:
            mass (float): The mass of the object in grams.
            volume (float): The volume of the object in cubic centimeters.
    
        Returns:
            float: The density of the object in grams per cubic centimeter.
        """
        if volume == 0:
            raise ValueError("Volume cannot be zero.")
    
        density = mass / volume
        return density
    
    def main():
        """
        Prompts the user for the mass and volume of an object, calculates the density, and displays the result.
        """
        try:
            mass = float(input("Enter the mass of the object (in grams): "))
            volume = float(input("Enter the volume of the object (in cubic centimeters): "))
    
            density = calculate_density(mass, volume)
            print(f"The density of the object is {density:.2f} g/cm^3.")
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")
    
    if __name__ == "__main__":
        main()    

def multiple_one_function():
    call(["python", "multiple one.py"])

def multiple_two_function():
    call(["python", "multiple two.py"])

def chemistry_function():
    call(["python", "chemistry.py"])

def music_function():call(["python", "SOUND PLAYER.py"])

def multiple_three_function():
    class FormulaSolver:
        def __init__(self):
            self.formulas = {
                "area_circle": lambda r: 3.14159 * r ** 2,
                "circumference_circle": lambda r: 2 * 3.14159 * r,
                "area_rectangle": lambda l, w: l * w,
                "perimeter_rectangle": lambda l, w: 2 * (l + w),
                "area_triangle": lambda b, h: 0.5 * b * h,
                "pythagorean_theorem": lambda a, b: (a ** 2 + b ** 2) ** 0.5,
                "force": lambda m, a: m * a,
                "work": lambda f, d: f * d,
                "kinetic_energy": lambda m, v: 0.5 * m * v ** 2,
                "potential_energy": lambda m, h: m * 9.81 * h,
                # Add more formulas here...
            }
    
        def calculate(self, formula_name, *args):
            if formula_name in self.formulas:
                return self.formulas[formula_name](*args)
            else:
                return "Formula not found."
    
    def main():
        solver = FormulaSolver()
        print("Available formulas:")
        print("1. area_circle")
        print("2. circumference_circle")
        print("3. area_rectangle")
        print("4. perimeter_rectangle")
        print("5. area_triangle")
        print("6. pythagorean_theorem")
        print("7. force")
        print("8. work")
        print("9. kinetic_energy")
        print("10. potential_energy")
        # Add more options here...
    
        choice = input("Choose a formula to calculate: ")
        if choice == "area_circle":
            r = float(input("Enter radius: "))
            print("Area of circle:", solver.calculate(choice, r))
        elif choice == "circumference_circle":
            r = float(input("Enter radius: "))
            print("Circumference of circle:", solver.calculate(choice, r))
        elif choice == "area_rectangle":
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            print("Area of rectangle:", solver.calculate(choice, l, w))
        elif choice == "perimeter_rectangle":
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            print("Perimeter of rectangle:", solver.calculate(choice, l, w))
        elif choice == "area_triangle":
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            print("Area of triangle:", solver.calculate(choice, b, h))
        elif choice == "pythagorean_theorem":
            a = float(input("Enter side a: "))
            b = float(input("Enter side b: "))
            print("Hypotenuse:", solver.calculate(choice, a, b))
        elif choice == "force":
            m = float(input("Enter mass: "))
            a = float(input("Enter acceleration: "))
            print("Force:", solver.calculate(choice, m, a))
        elif choice == "work":
            f = float(input("Enter force: "))
            d = float(input("Enter distance: "))
            print("Work done:", solver.calculate(choice, f, d))
        elif choice == "kinetic_energy":
            m = float(input("Enter mass: "))
            v = float(input("Enter velocity: "))
            print("Kinetic energy:", solver.calculate(choice, m, v))
        elif choice == "potential_energy":
            m = float(input("Enter mass: "))
            h = float(input("Enter height: "))
            print("Potential energy:", solver.calculate(choice, m, h))
        else:
            print("Invalid choice.")
    
    if __name__ == "__main__":
        main()
    

def multiple_four_function():
    import math
    
    class FormulaSolver:
        def __init__(self):
            self.formulas = {
                "quadratic": self.quadratic_formula,
                "pythagorean": self.pythagorean_theorem,
                "area_circle": self.area_circle,
                "force": self.force_formula,
                "energy": self.energy_formula,
                # Add more formulas here
            }
    
        def quadratic_formula(self, a, b, c):
            discriminant = b**2 - 4*a*c
            if discriminant < 0:
                return "No real roots"
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            return root1, root2
    
        def pythagorean_theorem(self, a, b):
            return math.sqrt(a**2 + b**2)
    
        def area_circle(self, radius):
            return math.pi * radius**2
    
        def force_formula(self, mass, acceleration):
            return mass * acceleration
    
        def energy_formula(self, mass, speed_of_light=3e8):
            return mass * speed_of_light**2
    
        def calculate(self, formula_name, *args):
            if formula_name in self.formulas:
                return self.formulas[formula_name](*args)
            else:
                return "Formula not found"
    
    def main():
        solver = FormulaSolver()
        while True:
            print("Available formulas:")
            for formula in solver.formulas.keys():
                print(formula)
            choice = input("Enter the formula you want to calculate (or 'exit' to quit): ")
            if choice == 'exit':
                break
            if choice == "quadratic":
                a = float(input("Enter a: "))
                b = float(input("Enter b: "))
                c = float(input("Enter c: "))
                print(solver.calculate(choice, a, b, c))
            elif choice == "pythagorean":
                a = float(input("Enter side a: "))
                b = float(input("Enter side b: "))
                print(solver.calculate(choice, a, b))
            elif choice == "area_circle":
                radius = float(input("Enter radius: "))
                print(solver.calculate(choice, radius))
            elif choice == "force":
                mass = float(input("Enter mass: "))
                acceleration = float(input("Enter acceleration: "))
                print(solver.calculate(choice, mass, acceleration))
            elif choice == "energy":
                mass = float(input("Enter mass: "))
                print(solver.calculate(choice, mass))
            else:
                print("Formula not found")
    
    if __name__ == "__main__":
        main()

def interest_function():
    
    call(["python", "interest.py"])
        
def physics_function():
    import tkinter as tk
    from tkinter import ttk
    import math
    
    # Physics functions
    
    def newtons_law(mass, acceleration):
        return mass * acceleration
    
    def kinetic_energy(mass, velocity):
        return 0.5 * mass * velocity ** 2
    
    def ideal_gas_law(pressure, volume, temp):
        R = 8.314
        return (pressure * volume) / (R * temp)
    
    def ohms_law(current, resistance):
        return current * resistance
    
    def resistance(voltage, current):
        if current == 0:
            raise ValueError("Current cannot be zero")
        return voltage / current
    
    def snells_law(n1, theta1_deg, n2):
        theta1_rad = math.radians(theta1_deg)
        return math.degrees(math.asin(n1 * math.sin(theta1_rad) / n2))
    
    def lens_equation(do, di):
        return 1 / ((1 / do) + (1 / di))
    
    def gravitational_potential_energy(mass, height, g=9.8):
        return mass * g * height
    
    def momentum(mass, velocity):
        return mass * velocity
    
    def work_done(force, distance):
        return force * distance
    
    def power(work, time):
        return work / time
    
    def wave_speed(frequency, wavelength):
        return frequency * wavelength
    
    def period(frequency):
        return 1 / frequency
    
    def pressure(force, area):
        return force / area
    
    def capacitance(charge, voltage):
        return charge / voltage
    
    def coulombs_law(q1, q2, r):
        k = 8.99e9
        return k * q1 * q2 / r ** 2
    
    def velocity_uniform_acceleration(u, a, t):
        return u + a * t
    
    def displacement_uniform_acceleration(u, a, t):
        return u * t + 0.5 * a * t ** 2
    
    def force_friction(mu, normal_force):
        return mu * normal_force
    
    def work_isothermal(n, R, T, Vf, Vi):
        return n * R * T * math.log(Vf / Vi)
    
    def magnetic_force(q, v, B, theta_deg):
        theta_rad = math.radians(theta_deg)
        return q * v * B * math.sin(theta_rad)
    
    def pendulum_frequency(g, L):
        return (1 / (2 * math.pi)) * math.sqrt(g / L)
    
    def efficiency(useful_energy_out, total_energy_in):
        return (useful_energy_out / total_energy_in) * 100
    
    def centripetal_force(mass, velocity, radius):
        return mass * velocity ** 2 / radius
    
    def elastic_potential_energy(k, x):
        return 0.5 * k * x ** 2
    
    def frequency_from_period(T):
        return 1 / T
    
    def voltage_divider(v_in, r1, r2):
        return v_in * (r2 / (r1 + r2))
    
    def resistors_in_series(*resistances):
        return sum(resistances)
    
    def resistors_in_parallel(*resistances):
        if any(r == 0 for r in resistances):
            raise ValueError("Resistance cannot be zero in parallel circuit")
        return 1 / sum(1 / r for r in resistances)
    
    def displacement_wave(speed, frequency, time):
        return speed * frequency * time
    
    def intensity_power_area(power, area):
        return power / area
    
    def half_life_decay(initial_amount, decay_constant, time):
        return initial_amount * math.exp(-decay_constant * time)
    
    def lens_magnification(image_distance, object_distance):
        return image_distance / object_distance
    
    
    # Formulas metadata
    
    formulas = {
        "Mechanics": {
            "Newton's Second Law": {"inputs": ["Mass (kg)", "Acceleration (m/sÂ²)"], "function": newtons_law, "unit": "N"},
            "Kinetic Energy": {"inputs": ["Mass (kg)", "Velocity (m/s)"], "function": kinetic_energy, "unit": "J"},
            "Gravitational Potential Energy": {"inputs": ["Mass (kg)", "Height (m)"], "function": gravitational_potential_energy, "unit": "J"},
            "Momentum": {"inputs": ["Mass (kg)", "Velocity (m/s)"], "function": momentum, "unit": "kgÂ·m/s"},
            "Work Done": {"inputs": ["Force (N)", "Distance (m)"], "function": work_done, "unit": "J"},
            "Power": {"inputs": ["Work (J)", "Time (s)"], "function": power, "unit": "W"},
            "Velocity with Uniform Acceleration": {"inputs": ["Initial Velocity (m/s)", "Acceleration (m/sÂ²)", "Time (s)"], "function": velocity_uniform_acceleration, "unit": "m/s"},
            "Displacement with Uniform Acceleration": {"inputs": ["Initial Velocity (m/s)", "Acceleration (m/sÂ²)", "Time (s)"], "function": displacement_uniform_acceleration, "unit": "m"},
            "Force of Friction": {"inputs": ["Coefficient of Friction", "Normal Force (N)"], "function": force_friction, "unit": "N"},
            "Centripetal Force": {"inputs": ["Mass (kg)", "Velocity (m/s)", "Radius (m)"], "function": centripetal_force, "unit": "N"},
            "Elastic Potential Energy": {"inputs": ["Spring Constant (N/m)", "Displacement (m)"], "function": elastic_potential_energy, "unit": "J"},
        },
        "Thermodynamics": {
            "Ideal Gas Law": {"inputs": ["Pressure (Pa)", "Volume (mÂ³)", "Temperature (K)"], "function": ideal_gas_law, "unit": "mol"},
            "Work done in Isothermal Process": {"inputs": ["Amount of Substance (mol)", "Gas Constant (J/molÂ·K)", "Temperature (K)", "Final Volume (mÂ³)", "Initial Volume (mÂ³)"], "function": work_isothermal, "unit": "J"},
        },
        "Electromagnetism": {
            "Ohm's Law": {"inputs": ["Current (A)", "Resistance (Î©)"], "function": ohms_law, "unit": "V"},
            "Resistance (Ohm's Law)": {"inputs": ["Voltage (V)", "Current (A)"], "function": resistance, "unit": "Î©"},
            "Capacitance": {"inputs": ["Charge (C)", "Voltage (V)"], "function": capacitance, "unit": "F"},
            "Coulomb's Law": {"inputs": ["Charge 1 (C)", "Charge 2 (C)", "Distance (m)"], "function": coulombs_law, "unit": "N"},
            "Magnetic Force on Moving Charge": {"inputs": ["Charge (C)", "Velocity (m/s)", "Magnetic Field (T)", "Angle (Â°)"], "function": magnetic_force, "unit": "N"},
            "Voltage Divider": {"inputs": ["Input Voltage (V)", "Resistor R1 (Î©)", "Resistor R2 (Î©)"], "function": voltage_divider, "unit": "V"},
            "Resistors in Series": {"inputs": ["Resistance 1 (Î©)", "Resistance 2 (Î©)", "Resistance 3 (Î©)"], "function": resistors_in_series, "unit": "Î©"},
            "Resistors in Parallel": {"inputs": ["Resistance 1 (Î©)", "Resistance 2 (Î©)", "Resistance 3 (Î©)"], "function": resistors_in_parallel, "unit": "Î©"},
        },
        "Optics": {
            "Snell's Law": {"inputs": ["n1", "Angle Î¸1 (Â°)", "n2"], "function": snells_law, "unit": "Angle Î¸2 (Â°)"},
            "Lens Equation": {"inputs": ["Object Distance (cm)", "Image Distance (cm)"], "function": lens_equation, "unit": "Focal Length (cm)"},
            "Lens Magnification": {"inputs": ["Image Distance (cm)", "Object Distance (cm)"], "function": lens_magnification, "unit": "Magnification (ratio)"},
        },
        "Waves": {
            "Wave Speed": {"inputs": ["Frequency (Hz)", "Wavelength (m)"], "function": wave_speed, "unit": "m/s"},
            "Period": {"inputs": ["Frequency (Hz)"], "function": period, "unit": "s"},
            "Pendulum Frequency": {"inputs": ["Gravitational Acceleration (m/sÂ²)", "Length (m)"], "function": pendulum_frequency, "unit": "Hz"},
            "Frequency from Period": {"inputs": ["Period (s)"], "function": frequency_from_period, "unit": "Hz"},
            "Displacement of Wave": {"inputs": ["Wave Speed (m/s)", "Frequency (Hz)", "Time (s)"], "function": displacement_wave, "unit": "m"},
        },
        "Pressure": {
            "Pressure": {"inputs": ["Force (N)", "Area (mÂ²)"], "function": pressure, "unit": "Pa"},
            "Intensity of Wave": {"inputs": ["Power (W)", "Area (mÂ²)"], "function": intensity_power_area, "unit": "W/mÂ²"},
        },
        "Energy": {
            "Efficiency": {"inputs": ["Useful Energy Output (J)", "Total Energy Input (J)"], "function": efficiency, "unit": "%"},
            "Half-Life Decay": {"inputs": ["Initial Amount", "Decay Constant", "Time"], "function": half_life_decay, "unit": "Amount"},
        }
    }
    
    
    class PhysicsApp(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("Physics Formula Calculator")
            self.geometry("600x600")
            self.inputs = []
            self.create_widgets()
    
        def create_widgets(self):
            ttk.Label(self, text="Category:").pack()
            self.category_cb = ttk.Combobox(self, values=list(formulas.keys()), state="readonly")
            self.category_cb.pack(pady=5)
            self.category_cb.bind("<<ComboboxSelected>>", self.update_formulas)
    
            ttk.Label(self, text="Formula:").pack()
            self.formula_cb = ttk.Combobox(self, state="readonly")
            self.formula_cb.pack(pady=5)
            self.formula_cb.bind("<<ComboboxSelected>>", self.update_inputs)
    
            self.inputs_frame = tk.Frame(self)
            self.inputs_frame.pack(pady=10, fill='x')
    
            self.calc_btn = ttk.Button(self, text="Calculate", command=self.calculate)
            self.calc_btn.pack(pady=10)
    
            self.result_lbl = ttk.Label(self, text="", font=("Arial", 14))
            self.result_lbl.pack(pady=10)
    
        def update_formulas(self, event):
            category = self.category_cb.get()
            self.formula_cb['values'] = list(formulas[category].keys())
            self.formula_cb.set('')
            self.clear_inputs()
            self.result_lbl.config(text="")
    
        def update_inputs(self, event):
            self.clear_inputs()
            category = self.category_cb.get()
            formula = self.formula_cb.get()
            input_labels = formulas[category][formula]["inputs"]
            self.inputs = []
            for label_text in input_labels:
                frame = tk.Frame(self.inputs_frame)
                frame.pack(pady=2, fill='x')
                label = ttk.Label(frame, text=label_text)
                label.pack(side=tk.LEFT, padx=5)
                entry = ttk.Entry(frame)
                entry.pack(side=tk.RIGHT, padx=5)
                self.inputs.append(entry)
            self.result_lbl.config(text="")
    
        def clear_inputs(self):
            for widget in self.inputs_frame.winfo_children():
                widget.destroy()
            self.inputs = []
    
        def calculate(self):
            try:
                category = self.category_cb.get()
                formula = self.formula_cb.get()
                func = formulas[category][formula]["function"]
                unit = formulas[category][formula]["unit"]
                args = [float(e.get()) for e in self.inputs]
                result = func(*args)
                self.result_lbl.config(text=f"Result: {result:.4f} {unit}")
            except Exception as e:
                self.result_lbl.config(text=f"Error: {str(e)}")
    
    
    if __name__ == "__main__":
        app = PhysicsApp()
        app.mainloop()
    
def conversions_two_function():
    call(["python", "si units.py"])

def multiple_five_function():
    import sympy as sp
    
    class FormulaSolver:
        def __init__(self):
            self.formulas = {
                'quadratic': 'ax^2 + bx + c = 0',
                'pythagorean': 'a^2 + b^2 = c^2',
                'ohm': 'V = I * R',
                'force': 'F = m * a',
                'kinetic_energy': 'KE = 0.5 * m * v^2',
                'potential_energy': 'PE = m * g * h',
                'work': 'W = F * d * cos(theta)',
                'momentum': 'p = m * v',
                'circular_motion': 'F_c = m * v^2 / r',
                'ideal_gas': 'PV = nRT',
                # Add more formulas as needed
            }
    
        def display_formulas(self):
            print("Available formulas:")
            for key in self.formulas.keys():
                print(key)
    
        def solve_formula(self, formula_name, **kwargs):
            if formula_name not in self.formulas:
                return "Formula not found."
            
            formula = self.formulas[formula_name]
            symbols = sp.symbols(' '.join(kwargs.keys()))
            equation = sp.sympify(formula.replace('^', '**').replace('=', '-(') + ')')
            
            solutions = sp.solve(equation.subs(kwargs), symbols)
            return solutions
    
    if __name__ == "__main__":
        solver = FormulaSolver()
        solver.display_formulas()
        
        # Example usage
        formula_name = input("Enter the formula name: ")
        params = {}
        
        if formula_name == 'quadratic':
            params['a'] = float(input("Enter a: "))
            params['b'] = float(input("Enter b: "))
            params['c'] = float(input("Enter c: "))
        elif formula_name == 'ohm':
            params['I'] = float(input("Enter current (I): "))
            params['R'] = float(input("Enter resistance (R): "))
        # Add more input handling for other formulas as needed
    
        result = solver.solve_formula(formula_name, **params)
        print("Result:", result)

def multiple_function():
    multiple_one_button = Button(main_window, text = "MULTIPLE (PACK 1)")
    multiple_two_button = Button(main_window, text = "MULTIPLE (PACK 2)")
    multiple_three_button = Button(main_window, text = "MULTIPLE (PACK 3)")
    multiple_four_button = Button(main_window, text = "MULTIPLE (PACK 4)")
    multiple_five_button = Button(main_window, text = "MULTIPLE (PACK 5)")
    multiple_six_button = Button(main_window, text = "MULTIPLE (PACK 6)")
    #multiple_seven_button = Button(main_window, text = "MULTIPLE (PACK 7)")
    multiple_eight_button = Button(main_window, text = "MULTIPLE (PACK 7)")
    multiple_nine_button = Button(main_window, text = "MULTIPLE (PACK 8)")
    
    multiple_one_button.config(bg = "black", fg = "red", command = multiple_one_function)
    multiple_two_button.config(bg = "black", fg = "red", command = multiple_two_function)
    multiple_three_button.config(bg = "black", fg = "red", command = multiple_three_function)
    multiple_four_button.config(bg = "black", fg = "red", command = multiple_four_function)
    multiple_five_button.config(bg = "black", fg = "red", command = multiple_five_function)
    multiple_six_button.config(bg = "black", fg = "red", command = multiple_six_function)
    #multiple_seven_button.config(bg = "black", fg = "red", command = multiple_seven_function)
    multiple_eight_button.config(bg = "black", fg = "red", command = multiple_eight_function)
    multiple_nine_button.config(bg = "black", fg = "red", command = multiple_nine_function) 
    
    multiple_one_button.pack()
    multiple_two_button.pack()
    multiple_three_button.pack()
    multiple_four_button.pack()
    multiple_five_button.pack()
    multiple_six_button.pack()
    #multiple_seven_button.pack()
    multiple_eight_button.pack()
    multiple_nine_button.pack()
    
    main_window.update()

def multiple_six_function():
    import math
    
    # Dictionary of formulas
    formulas = {
        # Physics formulas
        "Kinetic Energy": "0.5 * m * v**2",
        "Potential Energy": "m * g * h",
        "Force": "m * a",
        "Momentum": "m * v",
        "Work": "F * d * cos(theta)",
        "Power": "W / t",
        "Ohm's Law": "V = I * R",
        "Capacitance": "Q / V",
        "Inductance": "V / (dI/dt)",
        "Frequency": "1 / T",
        # Mathematics formulas
        "Area of a Circle": "pi * r**2",
        "Circumference of a Circle": "2 * pi * r",
        "Volume of a Sphere": "(4/3) * pi * r**3",
        "Pythagorean Theorem": "a**2 + b**2 = c**2",
        "Quadratic Formula": "(-b +/- sqrt(b**2 - 4*a*c)) / (2*a)",
        "Exponential Growth": "a * e**(b*t)",
        "Logarithm": "log(x, base)",
        "Factorial": "math.factorial(n)",
        "Binomial Coefficient": "math.comb(n, k)",
        "Sine": "math.sin(x)",
        # Add more formulas as needed
    }
    
    def solve_formula():
        print("Available formulas:")
        for formula_name in formulas:
            print(f"- {formula_name}")
    
        formula_name = input("Enter the formula you want to calculate: ")
    
        if formula_name in formulas:
            formula = formulas[formula_name]
            print(f"Formula: {formula}")
    
            # Prompt the user for the necessary variables
            variables = formula.split()
            values = {}
            for var in variables:
                if var not in ["*", "/", "+", "-", "**", "(", ")", "=", "0.5"]:
                    value = float(input(f"Enter the value for {var}: "))
                    values[var] = value
    
            # Evaluate the formula
            result = eval(formula.format(**values))
            print(f"Result: {result}")
        else:
            print("Sorry, the formula you entered is not available.")
    
    if __name__ == "__main__":
        solve_formula()    
        
def multiple_eight_function():
    import math
    
    # Dictionary of formulas
    formulas = {
        # Physics formulas
        "Kinetic Energy": "0.5 * m * v**2",
        "Potential Energy": "m * g * h",
        "Force": "m * a",
        "Momentum": "m * v",
        "Work": "F * d * cos(theta)",
        "Power": "W / t",
        "Ohm's Law": "V = I * R",
        "Capacitance": "Q / V",
        "Inductance": "V / (dI/dt)",
        "Frequency": "1 / T",
        # Mathematics formulas
        "Area of a Circle": "pi * r**2",
        "Circumference of a Circle": "2 * pi * r",
        "Volume of a Sphere": "(4/3) * pi * r**3",
        "Pythagorean Theorem": "a**2 + b**2 = c**2",
        "Quadratic Formula": "(-b +/- sqrt(b**2 - 4*a*c)) / (2*a)",
        "Exponential Growth": "a * e**(b*t)",
        "Logarithm": "log(x, base)",
        "Factorial": "math.factorial(n)",
        "Binomial Coefficient": "math.comb(n, k)",
        "Sine": "math.sin(x)",
        # Add more formulas as needed
    }
    
    def solve_formula():
        print("Available formulas:")
        for formula_name in formulas:
            print(f"- {formula_name}")
    
        formula_name = input("Enter the formula you want to calculate: ")
    
        if formula_name in formulas:
            formula = formulas[formula_name]
            print(f"Formula: {formula_name}")
            print(f"Formula expression: {formula}")
    
            # Prompt the user for the necessary variables
            variables = formula.split()
            values = []
            for var in variables:
                if var not in ["*", "/", "+", "-", "**", "(", ")", "=", "0.5"]:
                    value = float(input(f"Enter the value for {var}: "))
                    values.append(value)
    
            # Evaluate the formula
            result = eval(formula.format(*values))
            print(f"Result: {result}")
        else:
            print(f"Sorry, the formula '{formula_name}' is not available.")
    
    if __name__ == "__main__":
        solve_formula()   

def simultaneous_equation_function():
    import tkinter as tk
    from sympy import symbols, Eq, solve
    
    def solve_equations():
        """Solves the system of two linear equations."""
        try:
            # Get the coefficients from the entry fields
            a1 = float(entry_a1.get())
            b1 = float(entry_b1.get())
            c1 = float(entry_c1.get())
            a2 = float(entry_a2.get())
            b2 = float(entry_b2.get())
            c2 = float(entry_c2.get())
    
            # Define the variables
            x, y = symbols('x y')
    
            # Define the equations
            eq1 = Eq(a1*x + b1*y, c1)
            eq2 = Eq(a2*x + b2*y, c2)
    
            # Solve the system of equations
            solution = solve((eq1, eq2), (x, y))
    
            # Display the solution
            if solution:
                result_label.config(text=f"Solution: x = {solution[x]}, y = {solution[y]}")
            else:
                result_label.config(text="No unique solution found.")
    
        except ValueError:
            result_label.config(text="Error: Please enter valid numbers.")
        except Exception as e:
            result_label.config(text=f"An error occurred: {e}")
    
    # Create the main window
    root = tk.Tk()
    root.title("Simultaneous Equation Solver")
    
    # Labels and entry fields for the first equation (a1*x + b1*y = c1)
    label_eq1 = tk.Label(root, text="Equation 1: a1*x + b1*y = c1")
    label_eq1.grid(row=0, column=0, columnspan=6, padx=5, pady=5)
    
    label_a1 = tk.Label(root, text="a1:")
    label_a1.grid(row=1, column=0, padx=5, pady=5)
    entry_a1 = tk.Entry(root, width=5)
    entry_a1.grid(row=1, column=1, padx=5, pady=5)
    
    label_b1 = tk.Label(root, text="b1:")
    label_b1.grid(row=1, column=2, padx=5, pady=5)
    entry_b1 = tk.Entry(root, width=5)
    entry_b1.grid(row=1, column=3, padx=5, pady=5)
    
    label_c1 = tk.Label(root, text="c1:")
    label_c1.grid(row=1, column=4, padx=5, pady=5)
    entry_c1 = tk.Entry(root, width=5)
    entry_c1.grid(row=1, column=5, padx=5, pady=5)
    
    # Labels and entry fields for the second equation (a2*x + b2*y = c2)
    label_eq2 = tk.Label(root, text="Equation 2: a2*x + b2*y = c2")
    label_eq2.grid(row=2, column=0, columnspan=6, padx=5, pady=5)
    
    label_a2 = tk.Label(root, text="a2:")
    label_a2.grid(row=3, column=0, padx=5, pady=5)
    entry_a2 = tk.Entry(root, width=5)
    entry_a2.grid(row=3, column=1, padx=5, pady=5)
    
    label_b2 = tk.Label(root, text="b2:")
    label_b2.grid(row=3, column=2, padx=5, pady=5)
    entry_b2 = tk.Entry(root, width=5)
    entry_b2.grid(row=3, column=3, padx=5, pady=5)
    
    label_c2 = tk.Label(root, text="c2:")
    label_c2.grid(row=3, column=4, padx=5, pady=5)
    entry_c2 = tk.Entry(root, width=5)
    entry_c2.grid(row=3, column=5, padx=5, pady=5)
    
    # Button to solve the equations
    solve_button = tk.Button(root, text="Solve", command=solve_equations)
    solve_button.grid(row=4, column=0, columnspan=6, padx=5, pady=10)
    
    # Label to display the result
    result_label = tk.Label(root, text="Solution:")
    result_label.grid(row=5, column=0, columnspan=6, padx=5, pady=5)
    
    # Run the Tkinter event loop
    root.mainloop()
    

def multiple_nine_function():
    import math
    
    # Dictionary of formulas
    formulas = {
        # Physics formulas
        "Kinetic Energy": "0.5 * m * v**2",
        "Potential Energy": "m * g * h",
        "Force": "m * a",
        "Momentum": "m * v",
        "Work": "F * d * cos(theta)",
        "Power": "W / t",
        "Ohm's Law": "V = I * R",
        "Capacitance": "Q / V",
        "Inductance": "V / (dI/dt)",
        "Frequency": "1 / T",
        # Mathematics formulas
        "Area of a Circle": "pi * r**2",
        "Circumference of a Circle": "2 * pi * r",
        "Volume of a Sphere": "(4/3) * pi * r**3",
        "Pythagorean Theorem": "a**2 + b**2 = c**2",
        "Quadratic Formula": "(-b +/- sqrt(b**2 - 4*a*c)) / (2*a)",
        "Exponential Growth": "a * e**(b*t)",
        "Logarithm": "log(x, base)",
        "Factorial": "math.factorial(n)",
        "Binomial Coefficient": "math.comb(n, k)",
        "Sine": "math.sin(x)",
        # Add more formulas as needed
    }

def physics_two_function():
    call(["python", "Physics pro.py"])

def volume_of_a_cylider_function():
    call(["python", "volume of a cylinder.py"])


def calc_function():
    
    call(["python", "calc.py"])
    
def area_function():
    
    call(["python", "area.py"])
    
def conversions_function():
    call(["python", "conversions_file.py"])

def math_two_function():
    call(["python", "math pro.py"])


def custom_two_function():
    
    call(["python", "MATH AI 3.py"])

def clear_function():
    #This program is still being developed.
    main_window.mainloop()
    
def compond_interest_function():
  
  call(["python", "compound interest.py"])

style = ttk.Style()
style.theme_use("default")
style.configure("TButton",
                foreground="#ffffff",
                background="#444",
                font=("Helvetica", 10, "bold"),
                padding=6)
style.map("TButton",
          background=[('active', '#00aaff')],
          foreground=[('active', '#ffffff')])

# === TITLE ===
title_label = tk.Label(main_window,
                       text="\U0001F4D8 MATH AI",
                       font=("Segoe UI", 20, "bold"),
                       fg="#00ffcc",
                       bg="#2b2b2b")
title_label.pack(pady=15)

# === SEARCH ===
search_frame = tk.Frame(main_window, bg="#2b2b2b")
search_frame.pack(pady=10)

search_entry = ttk.Entry(search_frame, width=35, font=("Segoe UI", 11))
search_entry.grid(row=0, column=0, padx=10)

def help_two_function(): call(["python", "help window 2.py"])

def button_function():
    search_info = search_entry.get().strip().lower()
    actions = {
        "settings": settings,
        "base": base_function,
        "physics": physics_function,
        "density": density_function,
        "pro": pro_function,
        "help": help,
        "pythagorean": pythagorean_theorem_function
    }
    if search_info in actions:
        actions[search_info]()
    else:
        messagebox.showinfo("Search", f"No function bound to '{search_info}'")
    if search_info == "compond interest":
        compond_interest_function()
    elif search_info == "Compond interst":
        compond_interest_function()
        
    if search_info == "base":
        base_function()
    elif search_info == "Base":
        base_function()
        
    if search_info == "physics":
        physics_function()
    elif search_info == "Physics":
        physics_function()        

    if search_info == "density":
        density_function()
    elif search_info == "Density":
        density_function()
        
    if search_info == "custom":
        custom_function()
    elif search_info == "Custom":
        custom_function()

    if search_info == "calc":
        calc_function()
    elif search_info == "Calc":
        calc_function()

    if search_info == "area":
        area_function()
    elif search_info == "Area":
        area_function()

    if search_info == "volume":
        volume_function()
    elif search_info == "Volume":
        volume_function()

    if search_info == "volume of a cylinder":
        volume_of_a_cylider_function()
    elif search_info == "Volume of a cylinder":
        volume_of_a_cylider_function()
        
    if search_info == "velocity":
        velocity_function()
    elif search_info == "Velocity":
        velocity_function()

    if search_info == "multiple one":
        multiple_one_function()
    elif search_info == "Multiple one":
        multiple_one_function()

    if search_info == "multiple two":
        multiple_two_function()
    elif search_info == "Multiple two":
        multiple_two_function()
        
    if search_info == "multiple three":
        multiple_three_function()
    elif search_info == "Multiple three":
        multiple_three_function()
        
    if search_info == "multiple four":
        multiple_four_function()
    elif search_info == "Multiple four":
        multiple_four_function()

    if search_info == "multiple six":
        multiple_six_function()
    elif search_info == "Multiple six":
        multiple_six_function()

    if search_info == "multiple":
        multiple_function()
    elif search_info == "Multiple":
        multiple_function()

    if search_info == "physics 2":
        physics_two_function()
    elif search_info == "Physics 2":
        physics_two_function()

    if search_info == "multiple eight":
        multiple_eight_function()
    elif search_info == "Multiple eight":
        multiple_eight_function()

    if search_info == "multiple five":
        multiple_five_function()
    elif search_info == "Multiple five":
        multiple_five_function()

    if search_info == "multiple nine":
        multiple_nine_function()
    elif search_info == "Multiple nine":
        multiple_nine_function()
        
    if search_info == "conversions":
        conversions_function()
    elif search_info == "Conversions":
        conversions_function()

    if search_info == "conversions 2":
        conversions_two_function()
    elif search_info == "Conversions 2":
        conversions_two_function()

    if search_info == "interest":
        interest_function()
    elif search_info == "Interest":
        interest_function()

    if search_info == "math 2":
        math_two_function()
    elif search_info == "math 2":
        math_two_function()

    if search_info == "clear":
        clear_function()
    elif search_info == "Clear":
        clear_function()
    
    if search_info == "chemistry":
        chemistry_function()
    elif search_info == "Chemistry":
        chemistry_function()

    if search_info == "custom 2":
        custom_two_function()
    elif search_info == "Custom 2":
        custom_two_function()

    if search_info == "Help 2":
        help_two_function()
    elif search_info == "help 2":
        help_two_function()

    if search_info == "music":
        music_function()
    elif search_info == "Music":
        music_function()

    if search_info == "simultaneous equations":
        simultaneous_equation_function()
    elif search_info == "Simultaneous equations":
        simultaneous_equation_function()


    if search_info == "pythangorean theorem":
        pythagorean_theorem_function()
    elif search_info == "Pythangorean theorem":
        pythagorean_theorem_function()

search_button = ttk.Button(search_frame, text="\U0001F50D SEARCH", command=button_function)
search_button.grid(row=0, column=1)

# === BUTTONS ===
button_frame = tk.Frame(main_window, bg="#2b2b2b")
button_frame.pack(pady=20)

def make_button(text, command, row, col):
    btn = ttk.Button(button_frame, text=text, command=command)
    btn.grid(row=row, column=col, padx=8, pady=6, sticky="ew")

# === FUNCTION DEFINITIONS ===
def settings():
    def change_color():
        color = color_entry.get()
        main_window.configure(bg=color)
        title_label.configure(bg=color)
        footer.configure(bg=color)
    top = tk.Toplevel(main_window)
    top.title("Settings")
    tk.Label(top, text="Background Color:").pack(pady=5)
    color_entry = ttk.Entry(top)
    color_entry.pack(pady=5)
    ttk.Button(top, text="Apply", command=change_color).pack(pady=5)

def base_function():
    call(["python", "base.py"])

def physics_function():
    call(["python", "physics.py"])

def density_function():
    call(["python", "density.py"])

def pro_function():
    call(["python", "pro.py"])

def help():
    call(["python", "help +.py"])

def pythagorean_theorem_function():
    call(["python", "pythagorean theorem.py"])

# === BUTTON SETUP ===
make_button("\u2699  Settings", settings, 0, 0)
make_button("\U0001F4D0 Pythagoras", pythagorean_theorem_function, 0, 1)
make_button("\U0001F52C Physics", physics_function, 1, 0)
make_button("\U0001F4A1 Density", density_function, 1, 1)
make_button("\U0001F9E0 Base AI", base_function, 2, 0)
make_button("\U0001F4BB PRO", pro_function, 2, 1)
make_button("\U0001F4DA Help", help, 3, 0)

# === FOOTER ===
footer = tk.Label(main_window,
                  text="Made by Mwilima Liyoni ❤️ using Tkinter",
                  bg="#2b2b2b",
                  fg="#888888",
                  font=("Segoe UI", 8))
footer.pack(side="bottom", pady=10)

main_window.mainloop()
