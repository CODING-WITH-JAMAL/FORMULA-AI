#This is an animation tutorial

import tkinter as tk
import time, threading
from PIL import Image, ImageTk

class MyApp(tk.frame):
    def __init__(self, root):
        super().__init__(
            root,
            bg = "white"
        )
        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand = True)
        self.main_frame.columnconfigure(0, weight = 1)
        self.main_frame.rowconfigure(0, weight = 1)

root = tk.Tk()
root.tit("My App")
root.geometry("300x400")
root.resizable(width=False, height = False)
my_app_instance = MyApp(root)
root.mainloop()