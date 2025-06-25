from tkinter import*
from subprocess import call

def interest():
    call(["python", "interest.py"])

def physics():
    call(["python", "physics.py"])

def calc():
    call(["python", "calc.py"])

def base():
    call(["python", "base.py"])

def density():
    call(["python", "density.py"])
    
def custom():
    call(["python", "custom.py"])

def volume():
    call(["python", "volume graphical.py"])

def pt():
    call(["python", "pythagorean theorem.py"])

def physics_two_function():
    call(["python", "Physics pro.py"])

def math_two_function():
    call(["python", "math pro.py"])

def multiple_one_function():
    call(["python", "multiple one.py"])

def multiple_two_function():
    call(["python", "multiple two.py"])

def si_one_function():
    call(["python", "conversions_file.py"])

def si_two_function():
    call(["python", "si units.py"])

help_window = Tk()
help_window.geometry("350x700")
help_window.title("HELP")
help_window.config(bg = "grey")
instructons_label = Label(help_window, text = "Calculatable formulas include:\n\n")
instructons_label.config(bg = "grey", fg = "green", font = ("Ariel", 15, "underline", "bold"))

interest_button = Button(help_window, command = interest, text = "Interest")
physics_button = Button(help_window,  command = physics, text = "Physics")
calc_button = Button(help_window, text = "Calc", command = calc)
base_button = Button(help_window, text = "Base number converstions", command = base)
density_button = Button(help_window, text = "Density, Mass and Volume", command = density)
custom_button = Button(help_window, text = "Custom input", command = custom)
volume_button = Button(help_window, command = volume, text = "Volume")
pythagorean_theorem_button = Button(help_window, command = pt, text = "Pythagorean Theorem")
physics_two_button = Button(help_window, command = physics_two_function, text = "Physics 2")
math_two_button = Button(help_window, command = math_two_function, text = "Math 2")
multiple_one_button = Button(help_window, command = multiple_one_function, text = "Multiple 1")
si_button_one = Button(help_window, command = si_one_function, text = "SI Conversitons 1")
si_button_two = Button(help_window, command = si_two_function, text = "SI Conversitons 2")
multiple_two_button = Button(help_window, command = si_two_function, text = "Multiple 2")
chemistry_button = Button(help_window, command = si_two_function, text = "Chemistry")

interest_button.config(width = 50,font = ("Ariel", 10, "bold"), activebackground="green", activeforeground="red")
physics_button.config(width = 50,font = ("Ariel", 10, "bold"), activebackground="green", activeforeground="red")
calc_button.config(width = 50,font = ("Ariel", 10, "bold"), activebackground="green", activeforeground="red")
base_button.config(width = 50,font = ("Ariel", 10, "bold"), activebackground="green", activeforeground="red")
density_button.config(width = 50,font = ("Ariel", 10, "bold"), activebackground="green", activeforeground="red")
custom_button.config(width = 50,font = ("Ariel", 10, "bold"), activebackground="green", activeforeground="red")
volume_button.config(width = 50,font = ("Ariel", 10, "bold"), activebackground="green", activeforeground="red")
pythagorean_theorem_button.config(width = 50,font = ("Ariel", 10, "bold"), activebackground="green", activeforeground="red")
physics_two_button.config(width = 50,font = ("Ariel", 10, "bold"), activebackground="green", activeforeground="red")
math_two_button.config(width = 50,font = ("Ariel", 10, "bold"), activebackground="green", activeforeground="red")
multiple_one_button.config(width = 50,font = ("Ariel", 10, "bold"), activebackground="green", activeforeground="red")
si_button_one.config(width = 50,font = ("Ariel", 10, "bold"), activebackground="green", activeforeground="red")
si_button_two.config(width = 50,font = ("Ariel", 10, "bold"), activebackground="green", activeforeground="red")
multiple_two_button.config(width = 50,font = ("Ariel", 10, "bold"), activebackground="green", activeforeground="red")
chemistry_button.config(width = 50,font = ("Ariel", 10, "bold"), activebackground="green", activeforeground="red")

instructons_label.pack()
interest_button.pack()
physics_button.pack()
calc_button.pack()
calc_button.pack
base_button.pack()
density_button.pack()
custom_button.pack()
volume_button.pack()
pythagorean_theorem_button.pack()
physics_two_button.pack()
math_two_button.pack()
multiple_one_button.pack()
si_button_one.pack()
si_button_two.pack()
multiple_two_button.pack()
chemistry_button.pack()
help_window.mainloop()