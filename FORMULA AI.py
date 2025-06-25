import tkinter as tk
import subprocess

class LoadingScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Loading")
        self.root.geometry("400x250")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        # Center the window
        self.center_window()

        # Label: Loading text
        self.label = tk.Label(self.root, text="Loading", font=("Segoe UI", 18, "bold"), fg="white", bg="#1e1e1e")
        self.label.pack(pady=40)

        # Canvas: Custom progress bar
        self.canvas = tk.Canvas(self.root, width=300, height=20, bg="#2e2e2e", bd=0, highlightthickness=0, relief='ridge')
        self.canvas.pack(pady=20)
        self.progress = self.canvas.create_rectangle(0, 0, 0, 20, fill="#00bfff", width=0)

        self.dot_count = 0
        self.progress_width = 0

        self.animate_dots()
        self.animate_progress()

        # End after 5 seconds
        self.root.after(5000, self.launch_main_app)

    def center_window(self):
        self.root.update_idletasks()
        width = 400
        height = 250
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def animate_dots(self):
        dots = "." * (self.dot_count % 4)
        self.label.config(text=f"Loading{dots}")
        self.dot_count += 1
        self.root.after(500, self.animate_dots)

    def animate_progress(self):
        if self.progress_width < 300:
            self.progress_width += 10
            self.canvas.coords(self.progress, 0, 0, self.progress_width, 20)
            self.root.after(100, self.animate_progress)

    def launch_main_app(self):
        self.root.destroy()
        try:
            subprocess.run(["python", "MAIN FILE.py"])
        except Exception as e:
            print("Failed to launch main_app.py:", e)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoadingScreen(root)
    root.mainloop()
