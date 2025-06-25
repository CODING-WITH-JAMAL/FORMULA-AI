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

