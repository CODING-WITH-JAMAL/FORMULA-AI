def main():
    import tkinter as tk
    from tkinter import ttk
    # Fully expanded SI unit list (base unit conversions)
    si_units = {
        # Length
        "Meter (m)": 1,
        "Kilometer (km)": 1e3,
        "Centimeter (cm)": 1e-2,
        "Millimeter (mm)": 1e-3,
        "Micrometer (Âµm)": 1e-6,
        "Nanometer (nm)": 1e-9,
        "Angstrom (Ã…)": 1e-10,
        "Inch (in)": 0.0254,
        "Foot (ft)": 0.3048,
        "Yard (yd)": 0.9144,
        "Mile (mi)": 1609.34,
        "Astronomical Unit (au)": 1.496e11,
        "Light-Year": 9.461e15,
        "Parsec (pc)": 3.086e16,
    
        # Mass
        "Kilogram (kg)": 1,
        "Gram (g)": 1e-3,
        "Milligram (mg)": 1e-6,
        "Microgram (Âµg)": 1e-9,
        "Tonne (t)": 1e3,
        "Pound (lb)": 0.453592,
        "Ounce (oz)": 0.0283495,
    
        # Time
        "Second (s)": 1,
        "Millisecond (ms)": 1e-3,
        "Microsecond (Âµs)": 1e-6,
        "Nanosecond (ns)": 1e-9,
        "Minute (min)": 60,
        "Hour (h)": 3600,
        "Day": 86400,
        "Week": 604800,
        "Year (365d)": 3.154e7,
    
        # Temperature (Kelvin base)
        "Kelvin (K)": 1,
    
        # Electricity
        "Ampere (A)": 1,
        "Milliampere (mA)": 1e-3,
        "Microampere (ÂµA)": 1e-6,
    
        # Derived (scientific) units
        "Hertz (Hz)": 1,
        "Newton (N)": 1,
        "Pascal (Pa)": 1,
        "Joule (J)": 1,
        "Watt (W)": 1,
        "Coulomb (C)": 1,
        "Volt (V)": 1,
        "Farad (F)": 1,
        "Ohm (Î©)": 1,
        "Siemens (S)": 1,
        "Weber (Wb)": 1,
        "Tesla (T)": 1,
        "Henry (H)": 1,
        "Lumen (lm)": 1,
        "Lux (lx)": 1,
        "Becquerel (Bq)": 1,
        "Gray (Gy)": 1,
        "Sievert (Sv)": 1,
        "Katal (kat)": 1,
    
        # Others
        "Radian (rad)": 1,
        "Steradian (sr)": 1,
        "Candela (cd)": 1,
        "Mole (mol)": 1
    }
    
    # Fully expanded Data unit list
    data_units = {
        # Bytes
        "Byte (B)": 1,
        "Kilobyte (KB)": 1e3,
        "Megabyte (MB)": 1e6,
        "Gigabyte (GB)": 1e9,
        "Terabyte (TB)": 1e12,
        "Petabyte (PB)": 1e15,
        "Exabyte (EB)": 1e18,
        "Zettabyte (ZB)": 1e21,
        "Yottabyte (YB)": 1e24,
    
        # Binary
        "Kibibyte (KiB)": 1024,
        "Mebibyte (MiB)": 1024**2,
        "Gibibyte (GiB)": 1024**3,
        "Tebibyte (TiB)": 1024**4,
        "Pebibyte (PiB)": 1024**5,
        "Exbibyte (EiB)": 1024**6,
        "Zebibyte (ZiB)": 1024**7,
        "Yobibyte (YiB)": 1024**8,
    
        # Bits
        "Bit (b)": 1 / 8,
        "Kilobit (kb)": 1000 / 8,
        "Megabit (Mb)": 1e6 / 8,
        "Gigabit (Gb)": 1e9 / 8,
        "Terabit (Tb)": 1e12 / 8,
    
        # Legacy Storage
        "Floppy 3.5\" (HD)": 1474560,
        "CD-ROM (700MB)": 700 * 1e6,
        "DVD (4.7GB)": 4.7 * 1e9,
        "Blu-ray (25GB)": 25 * 1e9,
        "Blu-ray Dual Layer (50GB)": 50 * 1e9,
        "SSD 512GB": 512 * 1e9,
        "HDD 1TB": 1e12
    }
    
    
    class UnitConverterApp:
        def __init__(self, root):
            self.root = root
            root.title("Ultimate SI & Data Unit Converter")
            root.geometry("600x420")
            root.resizable(False, False)
    
            # UI Components
            ttk.Label(root, text="Select Unit Category:").pack(pady=5)
            self.category = ttk.Combobox(root, values=["SI Units", "Data Units"])
            self.category.pack()
            self.category.bind("<<ComboboxSelected>>", self.update_units)
    
            ttk.Label(root, text="From Unit:").pack(pady=5)
            self.from_unit = ttk.Combobox(root)
            self.from_unit.pack()
    
            ttk.Label(root, text="To Unit:").pack(pady=5)
            self.to_unit = ttk.Combobox(root)
            self.to_unit.pack()
    
            ttk.Label(root, text="Enter Value:").pack(pady=5)
            self.value_entry = ttk.Entry(root)
            self.value_entry.pack()
    
            ttk.Button(root, text="Convert", command=self.convert).pack(pady=10)
    
            ttk.Label(root, text="Result:").pack(pady=5)
            self.result = ttk.Label(root, text="", font=("Arial", 12, "bold"))
            self.result.pack()
    
        def update_units(self, event):
            cat = self.category.get()
            units = list(si_units.keys()) if cat == "SI Units" else list(data_units.keys())
            self.from_unit["values"] = units
            self.to_unit["values"] = units
            self.from_unit.set('')
            self.to_unit.set('')
    
        def convert(self):
            try:
                val = float(self.value_entry.get())
                from_u = self.from_unit.get()
                to_u = self.to_unit.get()
                cat = self.category.get()
    
                if cat == "SI Units":
                    converted = val * si_units[from_u] / si_units[to_u]
                elif cat == "Data Units":
                    converted = val * data_units[from_u] / data_units[to_u]
                else:
                    raise ValueError("Please select a valid category.")
    
                self.result.config(text=f"{val} {from_u} = {converted:.6g} {to_u}")
            except Exception as e:
                self.result.config(text=f"Error: {e}")
    
    
    if __name__ == "__main__":
        root = tk.Tk()
        app = UnitConverterApp(root)
        root.mainloop()
main()