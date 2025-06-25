import tkinter as tk
from tkinter import ttk, messagebox
import math

# Expanded formulas dictionary
FORMULAS = {
    "Mechanics": {
        "v = u + at (Final velocity)": {
            "inputs": ["Initial velocity (u)", "Acceleration (a)", "Time (t)"],
            "func": lambda u, a, t: u + a * t
        },
        "s = ut + 1/2 at^2 (Displacement)": {
            "inputs": ["Initial velocity (u)", "Acceleration (a)", "Time (t)"],
            "func": lambda u, a, t: u * t + 0.5 * a * t ** 2
        },
        "F = ma (Force)": {
            "inputs": ["Mass (m)", "Acceleration (a)"],
            "func": lambda m, a: m * a
        },
        "KE = 1/2 mv^2 (Kinetic Energy)": {
            "inputs": ["Mass (m)", "Velocity (v)"],
            "func": lambda m, v: 0.5 * m * v ** 2
        },
        "p = mv (Momentum)": {
            "inputs": ["Mass (m)", "Velocity (v)"],
            "func": lambda m, v: m * v
        },
        "a_c = v^2/r (Centripetal acceleration)": {
            "inputs": ["Velocity (v)", "Radius (r)"],
            "func": lambda v, r: v ** 2 / r
        },
        "F_c = mv^2/r (Centripetal force)": {
            "inputs": ["Mass (m)", "Velocity (v)", "Radius (r)"],
            "func": lambda m, v, r: m * v ** 2 / r
        },
        "Work done W = Fd cosθ": {
            "inputs": ["Force (F)", "Distance (d)", "Angle θ (degrees)"],
            "func": lambda F, d, theta: F * d * math.cos(math.radians(theta))
        },
        "Power P = W/t": {
            "inputs": ["Work done (W)", "Time (t)"],
            "func": lambda W, t: W / t
        },
        "Impulse J = Ft": {
            "inputs": ["Force (F)", "Time (t)"],
            "func": lambda F, t: F * t
        },
        "Pressure P = F/A": {
            "inputs": ["Force (F)", "Area (A)"],
            "func": lambda F, A: F / A
        },
        "Hooke's Law F = kx": {
            "inputs": ["Spring constant (k)", "Extension (x)"],
            "func": lambda k, x: k * x
        },
        "Angular velocity ω = θ/t": {
            "inputs": ["Angular displacement (θ) radians", "Time (t)"],
            "func": lambda theta, t: theta / t
        },
        "Torque τ = rF sinθ": {
            "inputs": ["Distance from pivot (r)", "Force (F)", "Angle θ (degrees)"],
            "func": lambda r, F, theta: r * F * math.sin(math.radians(theta))
        },
        "Rotational kinetic energy KE = 1/2 Iω^2": {
            "inputs": ["Moment of inertia (I)", "Angular velocity (ω)"],
            "func": lambda I, omega: 0.5 * I * omega ** 2
        },
        "Moment of inertia I = mr^2": {
            "inputs": ["Mass (m)", "Radius (r)"],
            "func": lambda m, r: m * r ** 2
        },
        "Gravitational potential energy U = mgh": {
            "inputs": ["Mass (m)", "Gravitational acceleration (g)", "Height (h)"],
            "func": lambda m, g, h: m * g * h
        },
        "Velocity in free fall v = gt": {
            "inputs": ["Gravitational acceleration (g)", "Time (t)"],
            "func": lambda g, t: g * t
        },
        "Period of pendulum T = 2π√(l/g)": {
            "inputs": ["Length of pendulum (l)", "Gravitational acceleration (g)"],
            "func": lambda l, g: 2 * math.pi * math.sqrt(l / g)
        },
    },
    "Thermodynamics": {
        "PV = nRT (Ideal Gas Law, solve P)": {
            "inputs": ["Number of moles (n)", "Gas constant (R)", "Temperature (T)", "Volume (V)"],
            "func": lambda n, R, T, V: (n * R * T) / V
        },
        "Q = mcΔT (Heat energy)": {
            "inputs": ["Mass (m)", "Specific heat capacity (c)", "Temperature change (ΔT)"],
            "func": lambda m, c, dT: m * c * dT
        },
        "W = PΔV (Work done by gas)": {
            "inputs": ["Pressure (P)", "Change in Volume (ΔV)"],
            "func": lambda P, dV: P * dV
        },
        "Efficiency η = W/Q_h": {
            "inputs": ["Work done (W)", "Heat input (Q_h)"],
            "func": lambda W, Qh: W / Qh
        },
        "Heat capacity C = Q/ΔT": {
            "inputs": ["Heat energy (Q)", "Temperature change (ΔT)"],
            "func": lambda Q, dT: Q / dT
        },
        "Entropy change ΔS = Q_rev/T": {
            "inputs": ["Reversible heat (Q_rev)", "Temperature (T)"],
            "func": lambda Qrev, T: Qrev / T
        },
        "First law ΔU = Q - W": {
            "inputs": ["Heat added to system (Q)", "Work done by system (W)"],
            "func": lambda Q, W: Q - W
        },
        "Root mean square speed v_rms = √(3RT/M)": {
            "inputs": ["Gas constant (R)", "Temperature (T)", "Molar mass (M)"],
            "func": lambda R, T, M: math.sqrt(3 * R * T / M)
        },
        "Thermal expansion ΔL = αL₀ΔT": {
            "inputs": ["Coefficient of linear expansion (α)", "Original length (L₀)", "Temperature change (ΔT)"],
            "func": lambda a, L0, dT: a * L0 * dT
        },
        "Heat of fusion Q = mLf": {
            "inputs": ["Mass (m)", "Latent heat of fusion (Lf)"],
            "func": lambda m, Lf: m * Lf
        },
        "Heat of vaporization Q = mLv": {
            "inputs": ["Mass (m)", "Latent heat of vaporization (Lv)"],
            "func": lambda m, Lv: m * Lv
        },
    },
    "Electromagnetism": {
        "V = IR (Ohm's Law, Voltage)": {
            "inputs": ["Current (I)", "Resistance (R)"],
            "func": lambda I, R: I * R
        },
        "F = qvB sinθ (Lorentz Force)": {
            "inputs": ["Charge (q)", "Velocity (v)", "Magnetic field (B)", "Angle θ (degrees)"],
            "func": lambda q, v, B, theta: q * v * B * math.sin(math.radians(theta))
        },
        "B = μ₀I/2πr (Magnetic field from wire)": {
            "inputs": ["Current (I)", "Radius (r)"],
            "func": lambda I, r: (4*math.pi*1e-7) * I / (2 * math.pi * r)
        },
        "Power P = IV": {
            "inputs": ["Current (I)", "Voltage (V)"],
            "func": lambda I, V: I * V
        },
        "Capacitance C = Q/V": {
            "inputs": ["Charge (Q)", "Voltage (V)"],
            "func": lambda Q, V: Q / V
        },
        "Energy stored in capacitor U = 1/2 CV^2": {
            "inputs": ["Capacitance (C)", "Voltage (V)"],
            "func": lambda C, V: 0.5 * C * V ** 2
        },
        "Resistance R = ρL/A": {
            "inputs": ["Resistivity (ρ)", "Length (L)", "Cross-sectional area (A)"],
            "func": lambda rho, L, A: rho * L / A
        },
        "Magnetic flux Φ = B A cosθ": {
            "inputs": ["Magnetic field (B)", "Area (A)", "Angle θ (degrees)"],
            "func": lambda B, A, theta: B * A * math.cos(math.radians(theta))
        },
        "Induced emf ε = -dΦ/dt": {
            "inputs": ["Change in flux (dΦ)", "Change in time (dt)"],
            "func": lambda dPhi, dt: - dPhi / dt
        },
        "Current I = Q/t": {
            "inputs": ["Charge (Q)", "Time (t)"],
            "func": lambda Q, t: Q / t
        }
    },
    "Waves and Optics": {
        "v = fλ (Wave speed)": {
            "inputs": ["Frequency (f)", "Wavelength (λ)"],
            "func": lambda f, wavelength: f * wavelength
        },
        "Lens formula 1/f = 1/do + 1/di": {
            "inputs": ["Object distance (d_o)", "Image distance (d_i)"],
            "func": lambda do_, di_: 1 / do_ + 1 / di_
        },
        "Snell's Law n1 sinθ1 = n2 sinθ2 (solve θ2)": {
            "inputs": ["Refractive index n1", "Angle θ1 (degrees)", "Refractive index n2"],
            "func": lambda n1, theta1, n2: math.degrees(math.asin(n1 * math.sin(math.radians(theta1)) / n2))
        },
        "Intensity I = P/A": {
            "inputs": ["Power (P)", "Area (A)"],
            "func": lambda P, A: P / A
        },
        "Photoelectric kinetic energy KE = hf - φ": {
            "inputs": ["Frequency (f)", "Planck constant (h)", "Work function (φ)"],
            "func": lambda f, h, phi: h * f - phi
        },
        "Magnification M = -di/do": {
            "inputs": ["Image distance (d_i)", "Object distance (d_o)"],
            "func": lambda di_, do_: -di_ / do_
        },
        "Critical angle sinθc = n2/n1": {
            "inputs": ["Refractive index n2", "Refractive index n1"],
            "func": lambda n2, n1: math.degrees(math.asin(n2 / n1))
        },
        "Energy of photon E = hf": {
            "inputs": ["Planck constant (h)", "Frequency (f)"],
            "func": lambda h, f: h * f
        },
        "Wave period T = 1/f": {
            "inputs": ["Frequency (f)"],
            "func": lambda f: 1 / f
        }
    },
    "Modern Physics": {
        "Energy E = mc^2": {
            "inputs": ["Mass (m)"],
            "func": lambda m: m * (3e8)**2
        },
        "de Broglie wavelength λ = h/p": {
            "inputs": ["Planck constant (h)", "Momentum (p)"],
            "func": lambda h, p: h / p
        },
        "Radioactive decay N = N0 e^(-λt)": {
            "inputs": ["Initial quantity (N0)", "Decay constant (λ)", "Time (t)"],
            "func": lambda N0, lmbda, t: N0 * math.exp(-lmbda * t)
        },
        "Half-life t1/2 = ln2 / λ": {
            "inputs": ["Decay constant (λ)"],
            "func": lambda lmbda: math.log(2) / lmbda
        },
        "Mass-energy equivalence E = γmc^2": {
            "inputs": ["Lorentz factor (γ)", "Mass (m)"],
            "func": lambda gamma, m: gamma * m * (3e8) ** 2
        },
        "Lorentz factor γ = 1 / √(1 - v²/c²)": {
            "inputs": ["Velocity (v)", "Speed of light (c)"],
            "func": lambda v, c: 1 / math.sqrt(1 - (v ** 2) / (c ** 2))
        },
        "Photoelectric current I = eN/t": {
            "inputs": ["Charge of electron (e)", "Number of electrons (N)", "Time (t)"],
            "func": lambda e, N, t: e * N / t
        }
    }
}


class PhysicsSolver(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Physics Formula Solver")
        self.geometry("600x450")
        self.resizable(False, False)

        # Variables
        self.category_var = tk.StringVar()
        self.formula_var = tk.StringVar()

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        # Category label and dropdown
        ttk.Label(self, text="Select Category:", font=("Arial", 12)).pack(pady=(15, 5))
        self.category_cb = ttk.Combobox(self, textvariable=self.category_var, state="readonly", font=("Arial", 11))
        self.category_cb['values'] = list(FORMULAS.keys())
        self.category_cb.bind("<<ComboboxSelected>>", self.update_formulas)
        self.category_cb.pack(pady=5)

        # Formula label and dropdown
        ttk.Label(self, text="Select Formula:", font=("Arial", 12)).pack(pady=(15, 5))
        self.formula_cb = ttk.Combobox(self, textvariable=self.formula_var, state="readonly", font=("Arial", 11))
        self.formula_cb.bind("<<ComboboxSelected>>", self.show_inputs)
        self.formula_cb.pack(pady=5)

        # Frame for input fields
        self.inputs_frame = ttk.Frame(self)
        self.inputs_frame.pack(pady=10, fill=tk.X, padx=20)

        # Solve button
        self.solve_btn = ttk.Button(self, text="Calculate", command=self.calculate)
        self.solve_btn.pack(pady=10)

        # Result label
        self.result_label = ttk.Label(self, text="", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

    def update_formulas(self, event):
        category = self.category_var.get()
        formulas = list(FORMULAS.get(category, {}).keys())
        self.formula_cb['values'] = formulas
        self.formula_var.set("")
        self.clear_inputs()
        self.result_label.config(text="")

    def clear_inputs(self):
        for widget in self.inputs_frame.winfo_children():
            widget.destroy()

    def show_inputs(self, event):
        self.clear_inputs()
        formula = self.formula_var.get()
        category = self.category_var.get()
        if not formula or not category:
            return
        inputs = FORMULAS[category][formula]["inputs"]
        self.entries = []
        for inp in inputs:
            frame = ttk.Frame(self.inputs_frame)
            frame.pack(fill=tk.X, pady=3)
            label = ttk.Label(frame, text=inp + ":", width=25, anchor=tk.W)
            label.pack(side=tk.LEFT)
            entry = ttk.Entry(frame, width=20)
            entry.pack(side=tk.LEFT, padx=5)
            self.entries.append(entry)
        self.result_label.config(text="")

    def calculate(self):
        formula = self.formula_var.get()
        category = self.category_var.get()
        if not formula or not category:
            messagebox.showwarning("Input error", "Please select a category and a formula.")
            return
        try:
            inputs = [float(entry.get()) for entry in self.entries]
        except ValueError:
            messagebox.showerror("Input error", "Please enter valid numbers for all inputs.")
            return
        try:
            func = FORMULAS[category][formula]["func"]
            result = func(*inputs)
            if isinstance(result, float):
                result_str = f"{result:.5g}"
            else:
                result_str = str(result)
            self.result_label.config(text=f"Result: {result_str}")
        except Exception as e:
            messagebox.showerror("Calculation error", f"An error occurred: {e}")

if __name__ == "__main__":
    app = PhysicsSolver()
    app.mainloop()
