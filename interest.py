import tkinter as tk
from tkinter import ttk, messagebox

# Function to calculate interest
def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        if var_interest_type.get() == "Simple":
            interest = (principal * rate * time) / 100
            total = principal + interest
            result.set(f"Simple Interest: {interest:.2f}\nTotal Amount: {total:.2f}")
        else:
            amount = principal * ((1 + (rate / 100)) ** time)
            compound_interest = amount - principal
            result.set(f"Compound Interest: {compound_interest:.2f}\nTotal Amount: {amount:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# GUI setup
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x400")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Principal (â‚¹):", font=('Arial', 12)).pack(pady=5)
entry_principal = tk.Entry(root, font=('Arial', 12))
entry_principal.pack(pady=5)

tk.Label(root, text="Rate of Interest (%):", font=('Arial', 12)).pack(pady=5)
entry_rate = tk.Entry(root, font=('Arial', 12))
entry_rate.pack(pady=5)

tk.Label(root, text="Time (years):", font=('Arial', 12)).pack(pady=5)
entry_time = tk.Entry(root, font=('Arial', 12))
entry_time.pack(pady=5)

var_interest_type = tk.StringVar(value="Simple")

tk.Label(root, text="Select Interest Type:", font=('Arial', 12)).pack(pady=5)
tk.Radiobutton(root, text="Simple Interest", variable=var_interest_type, value="Simple", font=('Arial', 10)).pack()
tk.Radiobutton(root, text="Compound Interest", variable=var_interest_type, value="Compound", font=('Arial', 10)).pack()

tk.Button(root, text="Calculate", command=calculate_interest, font=('Arial', 12), bg='lightblue').pack(pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=('Arial', 12), fg="green").pack(pady=10)

# Start GUI loop
root.mainloop()
