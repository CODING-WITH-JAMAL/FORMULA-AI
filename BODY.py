import tkinter as tk
from tkinter import colorchooser
from subprocess import call
from math import*
import math
from tkinter import*
import tkinter

def run():

    
    search_info = self.formula_entry.get()
    
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
        import tkinter as tk
        from tkinter import messagebox
        
        def evaluate_formula():
            formula = entry.get()
            try:
                result = eval(formula)
                messagebox.showinfo("Result", f"The result is: {result}")
            except Exception as e:
                messagebox.showerror("Error", f"Invalid formula: {e}")
        
        app = tk.Tk()
        app.title("Formula Evaluator")
        
        label = tk.Label(app, text="Enter a formula:")
        label.pack()
        
        entry = tk.Entry(app)
        entry.pack()
        
        button = tk.Button(app, text="Evaluate", command=evaluate_formula)
        button.pack()
        
        app.mainloop()
        
    def volume_function():
        import math
        
        def calculate_cube_volume(side_length):
            """Calculate volume of a cube"""
            return side_length ** 3
        
        def calculate_sphere_radius(radius):
            """Calculate volume of a sphere using radius"""
            return (4/3) * math.pi * (radius ** 3)
        
        def calculate_cylinder_volume(radius, height):
            """Calculate volume of a cylinder"""
            return math.pi * (radius ** 2) * height
        
        def calculate_cone_volume(radius, height):
            """Calculate volume of a cone"""
            return (1/3) * math.pi * (radius ** 2) * height
        
        def calculate_rectangular_prism_volume(length, width, height):
            """Calculate volume of a rectangular prism"""
            return length * width * height
        
        def calculate_pyramid_volume(base_area, height):
            """Calculate volume of a pyramid"""
            return (1/3) * base_area * height
        
        def calculate_ellipsoid_volume(a, b, c):
            """Calculate volume of an ellipsoid"""
            return (4/3) * math.pi * a * b * c
        
        def calculate_torus_volume(major_radius, minor_radius):
            """Calculate volume of a torus (donut)"""
            return (math.pi * minor_radius ** 2) * (2 * math.pi * major_radius)
        
        def main():
            print("Volume Calculator Program")
            print("------------------------")
            print("Available shapes:")
            print("1. Cube")
            print("2. Sphere")
            print("3. Cylinder")
            print("4. Cone")
            print("5. Rectangular Prism")
            print("6. Pyramid")
            print("7. Ellipsoid")
            print("8. Torus")
            
            while True:
                try:
                    choice = int(input("\nEnter the number of the shape (1-8) or 0 to exit: "))
                    
                    if choice == 0:
                        print("Exiting the program. Goodbye!")
                        break
                        
                    elif choice == 1:  # Cube
                        side = float(input("Enter the side length of the cube: "))
                        volume = calculate_cube_volume(side)
                        print(f"\nFormula used: Volume = sideÂ³ = {side}Â³")
                        
                    elif choice == 2:  # Sphere
                        radius = float(input("Enter the radius of the sphere: "))
                        volume = calculate_sphere_radius(radius)
                        print(f"\nFormula used: Volume = (4/3)�€rÂ³ = (4/3)�€({radius})Â³")
                        
                    elif choice == 3:  # Cylinder
                        radius = float(input("Enter the radius of the cylinder: "))
                        height = float(input("Enter the height of the cylinder: "))
                        volume = calculate_cylinder_volume(radius, height)
                        print(f"\nFormula used: Volume = �€rÂ²h = �€({radius})Â²({height})")
                        
                    elif choice == 4:  # Cone
                        radius = float(input("Enter the radius of the cone: "))
                        height = float(input("Enter the height of the cone: "))
                        volume = calculate_cone_volume(radius, height)
                        print(f"\nFormula used: Volume = (1/3)�€rÂ²h = (1/3)�€({radius})Â²({height})")
                        
                    elif choice == 5:  # Rectangular Prism
                        length = float(input("Enter the length: "))
                        width = float(input("Enter the width: "))
                        height = float(input("Enter the height: "))
                        volume = calculate_rectangular_prism_volume(length, width, height)
                        print(f"\nFormula used: Volume = length Ã— width Ã— height = {length} Ã— {width} Ã— {height}")
                        
                    elif choice == 6:  # Pyramid
                        base_area = float(input("Enter the base area: "))
                        height = float(input("Enter the height: "))
                        volume = calculate_pyramid_volume(base_area, height)
                        print(f"\nFormula used: Volume = (1/3) Ã— base_area Ã— height = (1/3) Ã— {base_area} Ã— {height}")
                        
                    elif choice == 7:  # Ellipsoid
                        a = float(input("Enter the first semi-axis (a): "))
                        b = float(input("Enter the second semi-axis (b): "))
                        c = float(input("Enter the third semi-axis (c): "))
                        volume = calculate_ellipsoid_volume(a, b, c)
                        print(f"\nFormula used: Volume = (4/3)�€abc = (4/3)�€ Ã— {a} Ã— {b} Ã— {c}")
                        
                    elif choice == 8:  # Torus
                        major_r = float(input("Enter the major radius (distance from center to tube center): "))
                        minor_r = float(input("Enter the minor radius (tube radius): "))
                        volume = calculate_torus_volume(major_r, minor_r)
                        print(f"\nFormula used: Volume = (�€ Ã— minor_radiusÂ²) Ã— (2�€ Ã— major_radius) = (�€ Ã— {minor_r}Â²) Ã— (2�€ Ã— {major_r})")
                        
                    else:
                        print("Invalid choice. Please enter a number between 1 and 8.")
                        continue
                        
                    print(f"The volume is: {volume:.2f} cubic units")
                    
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    
        if __name__ == "__main__":
            main()
        
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
        import math
        
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
        import math
        
        # Dictionary of formulas
        formulas = {
            "Area of a Circle": "pi * r ** 2",
            "Circumference of a Circle": "2 * pi * r",
            "Volume of a Sphere": "(4/3) * pi * r ** 3",
            "Kinetic Energy": "0.5 * m * v ** 2",
            "Potential Energy": "m * g * h",
            "Force of Gravity": "m * g",
            "Ohm's Law (Voltage)": "I * R",
            "Ohm's Law (Current)": "V / R",
            "Ohm's Law (Resistance)": "V / I",
            "Pythagorean Theorem": "sqrt(a ** 2 + b ** 2)"
            # Add more formulas as needed
        }
        
        def calculate_formula(formula_name, *args):
            """
            Calculates the result of a given formula using the provided input parameters.
        
            Args:
                formula_name (str): The name of the formula to be calculated.
                *args: The input parameters required for the formula.
        
            Returns:
                float: The calculated result of the formula.
            """
            try:
                formula = formulas[formula_name]
                result = eval(formula, {"__builtins__": None}, {"pi": math.pi, **dict(zip(["r", "m", "v", "g", "h", "I", "R", "a", "b"], args))})
                return result
            except (KeyError, ValueError, ZeroDivisionError) as e:
                print(f"Error: {e}")
                return None
        
        def main():
            """
            Provides a user interface to select a formula, enter input parameters, and display the calculated result.
            """
            print("Available Formulas:")
            for formula_name in formulas:
                print(f"- {formula_name}")
        
            formula_name = input("Enter the formula name: ")
            if formula_name not in formulas:
                print(f"Error: '{formula_name}' is not a valid formula name.")
                return
        
            print(f"Formula: {formula_name}")
            input_params = []
            for param in formulas[formula_name].split("*"):
                for var in ["r", "m", "v", "g", "h", "I", "R", "a", "b"]:
                    if var in param:
                        value = float(input(f"Enter the value for {var}: "))
                        input_params.append(value)
                        break
        
            result = calculate_formula(formula_name, *input_params)
            if result is not None:
                print(f"Result: {result:.2f}")
        
        if __name__ == "__main__":
            main()    
    def multiple_two_function():
        import math
    
    # Dictionary of formulas
    formulas = {
        # Physics formulas
        "Kinetic Energy": "0.5 * m * v**2",
        "Potential Energy": "m * g * h",
        "Momentum": "m * v",
        "Force": "m * a",
        "Work": "F * d * cos(theta)",
        "Power": "W / t",
        "Acceleration": "F / m",
        "Velocity": "d / t",
        "Displacement": "0.5 * (v_i + v_f) * t",
        "Circular Motion": "v**2 / r",
        "Gravitational Force": "G * (m1 * m2) / r**2",
        "Ohm's Law": "V = I * R",
        "Capacitance": "Q / V",
        "Inductance": "N * A / l",
        "Frequency": "1 / T",
        "Period": "1 / f",
        "Wavelength": "v / f",
        # Math formulas
        "Area of a Circle": "pi * r**2",
        "Circumference of a Circle": "2 * pi * r",
        "Volume of a Sphere": "(4/3) * pi * r**3",
        "Surface Area of a Sphere": "4 * pi * r**2",
        "Area of a Rectangle": "l * w",
        "Perimeter of a Rectangle": "2 * (l + w)",
        "Volume of a Cube": "s**3",
        "Surface Area of a Cube": "6 * s**2",
        "Area of a Triangle": "0.5 * b * h",
        "Pythagorean Theorem": "a**2 + b**2 = c**2",
        "Quadratic Formula": "(-b +/- sqrt(b**2 - 4*a*c)) / (2*a)",
        "Exponential Growth": "P = P0 * e**(r*t)",
        "Logarithm": "log(x, base)",
        "Factorial": "math.factorial(n)",
        "Combination": "math.comb(n, r)",
        "Permutation": "math.perm(n, r)"
    }
    
    def solve_formula():
        print("Available formulas:")
        for formula in formulas:
            print(f"- {formula}")
    
        formula_name = input("Enter the formula you want to solve: ")
    
        if formula_name in formulas:
            formula_expression = formulas[formula_name]
            print(f"Formula: {formula_name}")
            print(f"Expression: {formula_expression}")
    
            # Prompt the user for the necessary variables
            variables = formula_expression.split("*")
            values = []
            for variable in variables:
                variable = variable.strip()
                if variable != "**2" and variable != "**3" and variable != "/":
                    value = float(input(f"Enter the value for {variable}: "))
                    values.append(value)
    
            # Evaluate the formula and display the result
            result = eval(formula_expression.format(*values))
            print(f"Result: {result}")
        else:
            print(f"Sorry, the formula '{formula_name}' is not available.")
    
    if __name__ == "__main__":
        solve_formula()
    
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
    
    def volume_of_a_cylider_function():
        import tkinter as tk
        from tkinter import ttk
        import math
        
        def calculate_volume():
            try:
                radius = float(radius_entry.get())
                height = float(height_entry.get())
                volume = math.pi * radius**2 * height
                result_label.config(text=f"Volume: {volume:.2f}")
            except ValueError:
                result_label.config(text="Invalid input")
        
        # Main window
        window = tk.Tk()
        window.title("Cylinder Volume Calculator")
        
        # Radius label and entry
        radius_label = ttk.Label(window, text="Radius:")
        radius_label.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
        radius_entry = ttk.Entry(window)
        radius_entry.grid(column=1, row=0, padx=5, pady=5)
        
        # Height label and entry
        height_label = tk.Label(window, text="Height:")
        height_label.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
        height_entry = ttk.Entry(window)
        height_entry.grid(column=1, row=1, padx=5, pady=5)
        
        # Calculate button
        calculate_button = ttk.Button(window, text="Calculate", command=calculate_volume)
        calculate_button.grid(column=0, row=2, columnspan=2, padx=5, pady=10)
        
        # Result label
        result_label = ttk.Label(window, text="Volume: ")
        result_label.grid(column=0, row=3, columnspan=2, padx=5, pady=5)
        
        window.mainloop()
        
    
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
    
    def colour_change():
        change_info = background_entry.get()
        main_window.config(bg = change_info)
        main_window.update()
    
    def calc_function():
        from subprocess import call
        call(["python", "calc.py"])
        
    
    def compond_interest_function():
        # Compound Interest Calculator
        
        def compound_interest(principal, rate, time, compounding_periods):
            """
            Calculates the final amount after compound interest is applied.
        
            Args:
                principal (float): The initial amount of money.
                rate (float): The annual interest rate as a decimal.
                time (int): The number of years the money is invested.
                compounding_periods (int): The number of times the interest is compounded per year.
        
            Returns:
                float: The final amount after compound interest is applied.
            """
            amount = principal * (1 + (rate / compounding_periods)) ** (compounding_periods * time)
            return amount
        
        # Example usage
        principal = float(input("Enter the initial principal amount: "))
        rate = float(input("Enter the annual interest rate (as a decimal): "))
        time = int(input("Enter the number of years: "))
        compounding_periods = int(input("Enter the number of compounding periods per year: "))
        
        final_amount = compound_interest(principal, rate, time, compounding_periods)
        print(f"The final amount after compound interest is: ${final_amount:.2f}")    
    
    def button_function():
        
        search_info = search_entry.get()
    
        if search_info == "compond interest":
            compond_interest_function()
        elif search_info == "Compond interst":
            compond_interest_function()
            
        if search_info == "base":
            base_function()
        elif search_info == "Base":
            base_function()
            
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
            
        if search_info == "simultaneous equations":
            simultaneous_equation_function()
        elif search_info == "Simultaneous equations":
            simultaneous_equation_function()
    
    
        if search_info == "pythangorean theorem":
            pythagorean_theorem_function()
        elif search_info == "Pythangorean theorem":
            pythagorean_theorem_function()
    
 

class FormulaInputApp:
    def __init__(self, master):
        self.master = master
        master.title("Formula Input")

        # Set default background color
        self.background_color = "lightblue"  # Default color
        self.master.configure(bg=self.background_color)  # Apply default background color

        # Formula Input Section
        self.formula_label = tk.Label(master, text="Enter Formula:", bg=self.background_color)
        self.formula_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.formula_entry = tk.Entry(master, width=50)
        self.formula_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        self.calculate_button = tk.Button(master, text="Calculate", command = run)
        self.calculate_button.grid(row=0, column=2, padx=5, pady=5)

        # Result Display Section
        self.result_label = tk.Label(master, text="Result:", bg=self.background_color)
        self.result_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.result_display = tk.Label(master, text="", bg=self.background_color)
        self.result_display.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky="we")

        # Settings Button
        self.settings_button = tk.Button(master, text="Settings", command=self.open_settings)
        self.settings_button.grid(row=2, column=0, columnspan=3, padx=5, pady=10)

    def open_settings(self):
        """Opens a settings window for changing background color."""
        settings_window = tk.Toplevel(self.master)
        settings_window.title("Settings")

        color_label = tk.Label(settings_window, text="Choose Background Color:")
        color_label.pack(padx=10, pady=5)

        color_button = tk.Button(settings_window, text="Select Color", command=self.choose_background_color)
        color_button.pack(padx=10, pady=5)

    def choose_background_color(self):
        """Opens a color chooser dialog and updates the background color."""
        color_code = colorchooser.askcolor(title="Choose Background Color")[1]
        if color_code:  # Check if a color was selected
            self.background_color = color_code
            self.master.configure(bg=self.background_color)  # Update the main window background
            self.formula_label.configure(bg=self.background_color)
            self.result_label.configure(bg=self.background_color)
            self.result_display.configure(bg=self.background_color)

root = tk.Tk()
app = FormulaInputApp(root)
root.mainloop()
