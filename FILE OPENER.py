import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

class FileOpenerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced File Opener")
        self.geometry("700x500")
        self.configure(bg="#2e3440")  # Dark modern background
        
        self.create_widgets()
        self.apply_styles()
    
    def create_widgets(self):
        # Frame for input and buttons
        top_frame = tk.Frame(self, bg="#3b4252")
        top_frame.pack(fill="x", padx=20, pady=15)
        
        # Entry for file path
        self.file_entry = tk.Entry(top_frame, font=("Segoe UI", 12), fg="#d8dee9", bg="#4c566a", insertbackground="white")
        self.file_entry.pack(side="left", fill="x", expand=True, ipady=6, padx=(0, 10))
        self.file_entry.insert(0, "Enter file path or use Browse...")
        self.file_entry.bind("<FocusIn>", self.clear_placeholder)
        self.file_entry.bind("<FocusOut>", self.add_placeholder)
        
        # Browse button
        self.browse_btn = tk.Button(top_frame, text="Browse", command=self.browse_file, bg="#5e81ac", fg="white", font=("Segoe UI", 11, "bold"))
        self.browse_btn.pack(side="left", padx=(0, 10), ipadx=10, ipady=5)
        self.add_hover_effect(self.browse_btn, "#81a1c1", "#5e81ac")
        
        # Open file button
        self.open_btn = tk.Button(top_frame, text="Open File", command=self.open_file, bg="#a3be8c", fg="#2e3440", font=("Segoe UI", 11, "bold"))
        self.open_btn.pack(side="left", ipadx=10, ipady=5)
        self.add_hover_effect(self.open_btn, "#b5d99c", "#a3be8c")
        
        # Clear button
        self.clear_btn = tk.Button(self, text="Clear", command=self.clear_all, bg="#bf616a", fg="white", font=("Segoe UI", 11, "bold"))
        self.clear_btn.pack(pady=(0, 10), ipadx=10, ipady=5)
        self.add_hover_effect(self.clear_btn, "#d08770", "#bf616a")
        
        # Scrolled text widget to display file content
        self.text_area = ScrolledText(self, font=("Consolas", 12), bg="#3b4252", fg="#d8dee9", insertbackground="white", wrap="word")
        self.text_area.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        self.text_area.config(state="disabled")
        
    def apply_styles(self):
        self.file_entry.config(relief="flat", highlightthickness=2, highlightcolor="#81a1c1", highlightbackground="#4c566a")
        
    def add_hover_effect(self, widget, hover_bg, normal_bg):
        def on_enter(e):
            widget['background'] = hover_bg
        def on_leave(e):
            widget['background'] = normal_bg
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)
        
    def clear_placeholder(self, event):
        if self.file_entry.get() == "Enter file path or use Browse...":
            self.file_entry.delete(0, tk.END)
            self.file_entry.config(fg="#d8dee9")
    
    def add_placeholder(self, event):
        if not self.file_entry.get():
            self.file_entry.insert(0, "Enter file path or use Browse...")
            self.file_entry.config(fg="#7c8797")
    
    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)
    
    def open_file(self):
        path = self.file_entry.get()
        if path == "" or path == "Enter file path or use Browse...":
            messagebox.showwarning("Input Error", "Please enter or select a valid file path.")
            return
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            self.text_area.config(state="normal")
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, content)
            self.text_area.config(state="disabled")
        except Exception as e:
            messagebox.showerror("File Error", f"Failed to open the file:\n{e}")
    
    def clear_all(self):
        self.file_entry.delete(0, tk.END)
        self.add_placeholder(None)
        self.text_area.config(state="normal")
        self.text_area.delete(1.0, tk.END)
        self.text_area.config(state="disabled")
        
if __name__ == "__main__":
    app = FileOpenerApp()
    app.mainloop()
