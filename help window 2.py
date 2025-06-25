import tkinter as tk
import subprocess
import sys

class FixedButtonsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quick File Opener")
        self.geometry("400x650")
        self.configure(bg="#2c3e50")

        self.commands = {
            "AREA": (["python","area.py"]),
            "BASE": (["python", "base.py"]),
            "CONVERSIONS": (["python", "conversions.py"]),
            "INTEREST":(["python", "interest.py"]),
            "CUSTOM": (["python", "custom.py"]),
            "CUSTOM 2": (["python", "custom2.py"]),
            "SI UNITS": (["python", "si units.py"]),
            "VOLUME OF A CYLINDER": (["python", "volume of a cylinder.py"]),
            "PHYSICS PRO": (["python", "physics pro.py"]),
            "CHEMISTRY": (["python", "chemistry.py"]),
            "CONVERSIONS 2": (["python", "conversions_file.py"]),
            "OPEN FILE": (["python", "FILE OPENER.py"]),
            "DENSITY": (["python", "density.py"]),
        }

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self, text="Click a button to open:", 
                               bg="#2c3e50", fg="white", font=("Segoe UI", 14))
        title_label.pack(pady=10)

        btn_frame = tk.Frame(self, bg="#2c3e50")
        btn_frame.pack(fill=tk.BOTH, expand=True, padx=20)

        for btn_text, cmd in self.commands.items():
            button = tk.Button(
                btn_frame, text=btn_text,
                font=("Segoe UI", 12, "bold"),
                bg="#2980b9", fg="white",
                activebackground="#3498db",
                command=lambda c=cmd: self.run_command(c)
            )
            button.pack(fill=tk.X, pady=6)

    def run_command(self, cmd):
        try:
            if sys.platform.startswith("win"):
                subprocess.Popen(cmd, shell=True)
            elif sys.platform == "darwin":
                subprocess.Popen(["open"] + cmd)
            else:
                subprocess.Popen(cmd)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to run command:\n{e}")

if __name__ == "__main__":
    app = FixedButtonsApp()
    app.mainloop()
