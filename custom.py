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
custom_function()