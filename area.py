import tkinter as tk
from tkinter import ttk
import math

# Modern Theme Definitions
THEMES = [
    {   # Soft Light
        "bg": "#F9FAFB",      # Light gray
        "fg": "#1F2937",      # Dark gray
        "canvas_bg": "#FFFFFF",  # White
        "shape_fill": "#3B82F6", # Blue
        "shape_outline": "#1E40AF" # Dark Blue
    },
    {   # Deep Dark
        "bg": "#111827",      # Almost black
        "fg": "#F9FAFB",      # Off-white
        "canvas_bg": "#1F2937",  # Dark gray-blue
        "shape_fill": "#EF4444", # Red
        "shape_outline": "#B91C1C" # Deep Red
    },
    {   # Fresh Pastel
        "bg": "#FEF3C7",      # Light cream
        "fg": "#92400E",      # Brown
        "canvas_bg": "#FEFCE8",  # Very light cream
        "shape_fill": "#10B981", # Green
        "shape_outline": "#065F46" # Deep Green
    }
]

# SI Units and conversion to meters
UNITS = {
    'mm': 1e-3,
    'cm': 1e-2,
    'm': 1,
    'km': 1e3
}

class AreaCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SI Unit Area Calculator")
        self.geometry("900x600")
        self.resizable(False, False)
        self.theme_index = 0
        self.apply_theme()

        # Variables
        self.unit_var = tk.StringVar(value='m')
        self.shape_var = tk.StringVar(value="Circle")
        self.params = {}
        self.animation_step = 0

        # UI Setup
        self.create_widgets()
        self.bind('<Return>', lambda e: self.calculate_area())
        self.animate()

    def apply_theme(self):
        theme = THEMES[self.theme_index]
        self.configure(bg=theme['bg'])
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('TLabel', background=theme['bg'], foreground=theme['fg'], font=('Helvetica', 11))
        style.configure('TButton', background=theme['canvas_bg'], foreground=theme['fg'], padding=6, font=('Helvetica', 11, 'bold'))
        style.map('TButton', background=[('active', theme['shape_fill'])])
        style.configure('TEntry', foreground=theme['fg'], font=('Helvetica', 11))

    def switch_theme(self):
        self.theme_index = (self.theme_index + 1) % len(THEMES)
        self.apply_theme()
        self.canvas.configure(bg=THEMES[self.theme_index]['canvas_bg'])

    def create_widgets(self):
        control_frame = ttk.Frame(self)
        control_frame.place(x=10, y=10, width=280, height=580)

        # Unit selection
        ttk.Label(control_frame, text="Select Unit:").pack(anchor='w', pady=(0,4))
        unit_menu = ttk.OptionMenu(control_frame, self.unit_var, 'm', *UNITS.keys())
        unit_menu.pack(fill='x', pady=(0,12))

        # Shape selection
        ttk.Label(control_frame, text="Select Shape:").pack(anchor='w', pady=(0,4))
        shapes = ["Sector", "Parallelogram", "Ellipse", "Trapezoid", 
                  "Triangle", "Square", "Rectangle", "Circle"]
        shape_menu = ttk.OptionMenu(control_frame, self.shape_var, shapes[0], *shapes, command=self.on_shape_change)
        shape_menu.pack(fill='x', pady=(0,12))

        # Parameter inputs
        self.param_frame = ttk.Frame(control_frame)
        self.param_frame.pack(pady=(0,15))
        self.build_param_fields()

        # Result display
        self.result_label = ttk.Label(control_frame, text="Area: ", font=('Helvetica', 13, 'bold'))
        self.result_label.pack(pady=(10,15))

        ttk.Button(control_frame, text="Calculate", command=self.calculate_area).pack(fill='x', pady=(0,8))
        ttk.Button(control_frame, text="Switch Theme", command=self.switch_theme).pack(fill='x')

        # Canvas for Animation
        self.canvas = tk.Canvas(self, width=600, height=580, bg=THEMES[self.theme_index]['canvas_bg'], highlightthickness=0)
        self.canvas.place(x=290, y=10)

    def clear_params(self):
        for child in self.param_frame.winfo_children():
            child.destroy()
        self.params.clear()

    def build_param_fields(self):
        self.clear_params()
        shape = self.shape_var.get()
        unit_label = f"({self.unit_var.get()})"
        fields = {
            'Circle': [f'Radius {unit_label}'],
            'Square': [f'Side {unit_label}'],
            'Rectangle': [f'Width {unit_label}', f'Height {unit_label}'],
            'Triangle': [f'Base {unit_label}', f'Height {unit_label}'],
            'Parallelogram': [f'Base {unit_label}', f'Height {unit_label}'],
            'Trapezoid': [f'Base1 {unit_label}', f'Base2 {unit_label}', f'Height {unit_label}'],
            'Ellipse': [f'Axis A {unit_label}', f'Axis B {unit_label}'],
            'Sector': [f'Radius {unit_label}', 'Angle (deg)']
        }[shape]
        for field in fields:
            ttk.Label(self.param_frame, text=field).pack(anchor='w')
            var = tk.DoubleVar()
            entry = ttk.Entry(self.param_frame, textvariable=var)
            entry.pack(fill='x', pady=(2,8))
            self.params[field] = var
        # Rebuild when unit changes
        self.unit_var.trace('w', lambda *args: self.build_param_fields())

    def on_shape_change(self, event=None):
        self.build_param_fields()
        self.animation_step = 0

    def calculate_area(self):
        shape = self.shape_var.get()
        unit = self.unit_var.get()
        factor = UNITS[unit]
        try:
            # convert inputs to meters
            def mval(key):
                val = list(self.params.keys())[list(self.params.values()).index(self.params[key])]
            # read raw inputs then convert
            vals = {k: v.get() * factor for k, v in self.params.items() if 'Angle' not in k}
            if shape == 'Circle':
                r = vals[f'Radius ({unit})']
                area_m2 = math.pi * r**2
            elif shape == 'Square':
                s = vals[f'Side ({unit})']
                area_m2 = s**2
            elif shape == 'Rectangle':
                w = vals[f'Width ({unit})']; h = vals[f'Height ({unit})']
                area_m2 = w * h
            elif shape == 'Triangle':
                b = vals[f'Base ({unit})']; h = vals[f'Height ({unit})']
                area_m2 = 0.5 * b * h
            elif shape == 'Parallelogram':
                b = vals[f'Base ({unit})']; h = vals[f'Height ({unit})']
                area_m2 = b * h
            elif shape == 'Trapezoid':
                b1 = vals[f'Base1 ({unit})']; b2 = vals[f'Base2 ({unit})']; h = vals[f'Height ({unit})']
                area_m2 = 0.5 * (b1 + b2) * h
            elif shape == 'Ellipse':
                a = vals[f'Axis A ({unit})']; b = vals[f'Axis B ({unit})']
                area_m2 = math.pi * a * b
            elif shape == 'Sector':
                r = vals[f'Radius ({unit})']
                angle = math.radians(self.params['Angle (deg)'].get())
                area_m2 = 0.5 * r**2 * angle
            # convert back to chosen unit squared
            area_unit2 = area_m2 / (factor**2)
            self.result_label.config(text=f"Area: {area_unit2:.4f} {unit}²")
        except Exception:
            self.result_label.config(text="Error: Invalid input")

    def animate(self):
        self.canvas.delete('all')
        theme = THEMES[self.theme_index]
        shape = self.shape_var.get()
        w, h = 600, 580
        cx, cy = w/2, h/2
        t = self.animation_step
        scale = 1 + 0.03 * math.sin(math.radians(t))
        fill = theme['shape_fill']
        outline = theme['shape_outline']

        # Helper to draw dimension lines
        def draw_dims(coords, text):
            x1, y1, x2, y2 = coords
            self.canvas.create_line(x1, y1, x2, y1, dash=(4,2))
            self.canvas.create_line(x2, y1, x2, y2, dash=(4,2))
            self.canvas.create_text((x1+x2)/2, y1-10, text=text, fill=theme['fg'], font=('Arial', 9))

        if shape == 'Circle':
            r = 100 * scale
            self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=fill, outline=outline, width=3)
            draw_dims((cx, cy, cx+r, cy), "r")
        elif shape == 'Rectangle':
            rw, rh = 160*scale, 100*scale
            x1, y1 = cx-rw, cy-rh
            x2, y2 = cx+rw, cy+rh
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline, width=3)
            draw_dims((x1, y2, x2, y2), "width")
            draw_dims((x2, y1, x2, y2), "height")
        elif shape == 'Square':
            s = 140*scale
            x1, y1 = cx-s, cy-s; x2, y2 = cx+s, cy+s
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline, width=3)
            draw_dims((x1, y2, x2, y2), "s")
        elif shape == 'Triangle':
            size = 160*scale
            p1 = (cx, cy-size); p2 = (cx-size, cy+size); p3 = (cx+size, cy+size)
            self.canvas.create_polygon(p1, p2, p3, fill=fill, outline=outline, width=3)
            draw_dims((cx, cy-size, cx+size, cy+size), "base")
            draw_dims((cx-size, cy+size, cx, cy-size), "height")
        elif shape == 'Parallelogram':
            dx = 60 * scale; dy = 80*scale
            pts = [cx-dx-100, cy-dy, cx+100, cy-dy, cx+dx+100, cy+dy, cx-100, cy+dy]
            self.canvas.create_polygon(pts, fill=fill, outline=outline, width=3)
            draw_dims((cx-100, cy+dy, cx+100, cy+dy), "base")
            draw_dims((cx+dx+100, cy-dy, cx+dx+100, cy+dy), "height")
        elif shape == 'Trapezoid':
            top = 100 * scale; bot = 180 * scale; dy = 80
            pts = [cx-top, cy-dy, cx+top, cy-dy, cx+bot, cy+dy, cx-bot, cy+dy]
            self.canvas.create_polygon(pts, fill=fill, outline=outline, width=3)
            draw_dims((cx-top, cy-dy, cx+top, cy-dy), "b1")
            draw_dims((cx-bot, cy+dy, cx+bot, cy+dy), "b2")
            draw_dims((cx+bot, cy-dy, cx+bot, cy+dy), "h")
        elif shape == 'Ellipse':
            rx, ry = 160*scale, 100*scale
            self.canvas.create_oval(cx-rx, cy-ry, cx+rx, cy+ry, fill=fill, outline=outline, width=3)
            draw_dims((cx-rx, cy, cx+rx, cy), "2a")
            draw_dims((cx, cy-ry, cx, cy+ry), "2b")
        elif shape == 'Sector':
            r = 140
            extent = (t % 360)
            self.canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=0, extent=extent,
                                   fill=fill, outline=outline, width=3, style='pieslice')
            draw_dims((cx, cy, cx+r, cy), "r")
            self.canvas.create_text(cx+math.cos(math.radians(extent/2))*r/1.5,
                                    cy-math.sin(math.radians(extent/2))*r/1.5,
                                    text=f"θ={extent:.0f}°", fill=theme['fg'], font=('Arial', 10, 'bold'))

        self.animation_step += 4
        self.after(50, self.animate)

if __name__ == '__main__':
    AreaCalculator().mainloop()
