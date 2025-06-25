import tkinter as tk
from tkinter import ttk
import math

class BaseCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Base Converter & Calculator")
        self.geometry("620x580")
        self.resizable(False, False)

        # Themes with highlight colors
        self.themes = {
            'Light':   {'bg': '#f7f7f7', 'fg': '#333333', 'btn': '#e0e0e0', 'highlight': '#FF8C00'},
            'Dark':    {'bg': '#2b2b2b', 'fg': '#f1f1f1', 'btn': '#3c3c3c', 'highlight': '#FF5722'},
            'Ocean':   {'bg': '#e0f7fa', 'fg': '#006064', 'btn': '#4dd0e1', 'highlight': '#00796B'}
        }
        self.current_theme = 'Light'
        self.apply_theme()
        self.create_widgets()
        self.bind_keys()

    def apply_theme(self):
        c = self.themes[self.current_theme]
        self.config(bg=c['bg'])
        style = ttk.Style(self)
        style.theme_use('default')
        style.configure('TCombobox', fieldbackground=c['btn'], background=c['btn'], foreground=c['fg'])
        style.map('TCombobox', fieldbackground=[('readonly', c['btn'])])

    def create_widgets(self):
        c = self.themes[self.current_theme]
        tf = tk.Frame(self, bg=c['bg'])
        tf.pack(fill='x', pady=6)
        tk.Label(tf, text="Theme:", bg=c['bg'], fg=c['fg'], font=('Arial',10,'bold')).pack(side='left', padx=5)
        for t in self.themes:
            tk.Button(tf, text=t, command=lambda t=t: self.change_theme(t),
                      bg=c['btn'], fg=c['fg'], relief='flat', padx=6, pady=4).pack(side='left', padx=4)

        bases = [2,3,4,5,6,7,8,9,10,12,16,32,36]

        # Conversion
        cf = tk.LabelFrame(self, text="Base Conversion", bg=c['bg'], fg=c['fg'],
                           font=('Arial',12,'bold'), padx=10, pady=10)
        cf.pack(fill='x', padx=10, pady=8)
        tk.Label(cf, text="Value:", bg=c['bg'], fg=c['fg']).grid(row=0,column=0, sticky='e')
        self.conv_input = tk.Entry(cf, width=18)
        self.conv_input.grid(row=0,column=1, padx=6)
        tk.Label(cf, text="From:", bg=c['bg'], fg=c['fg']).grid(row=1,column=0, sticky='e')
        self.conv_from = ttk.Combobox(cf, values=bases, state='readonly', width=5)
        self.conv_from.set(10)
        self.conv_from.grid(row=1,column=1)
        tk.Label(cf, text="To:", bg=c['bg'], fg=c['fg']).grid(row=2,column=0, sticky='e')
        self.conv_to = ttk.Combobox(cf, values=bases, state='readonly', width=5)
        self.conv_to.set(2)
        self.conv_to.grid(row=2,column=1)
        tk.Button(cf, text="Convert", command=self.convert,
                  bg=c['btn'], fg=c['fg'], padx=8).grid(row=3,column=0,columnspan=2, pady=6)

        # Arithmetic
        af = tk.LabelFrame(self, text="Arithmetic", bg=c['bg'], fg=c['fg'],
                           font=('Arial',12,'bold'), padx=10, pady=10)
        af.pack(fill='x', padx=10, pady=8)
        tk.Label(af, text="A:", bg=c['bg'], fg=c['fg']).grid(row=0,column=0, sticky='e')
        self.calc_a = tk.Entry(af, width=12)
        self.calc_a.grid(row=0,column=1, padx=6)
        tk.Label(af, text="B:", bg=c['bg'], fg=c['fg']).grid(row=1,column=0, sticky='e')
        self.calc_b = tk.Entry(af, width=12)
        self.calc_b.grid(row=1,column=1, padx=6)
        tk.Label(af, text="Base:", bg=c['bg'], fg=c['fg']).grid(row=2,column=0, sticky='e')
        self.calc_base = ttk.Combobox(af, values=bases, state='readonly', width=5)
        self.calc_base.set(10)
        self.calc_base.grid(row=2,column=1)
        ops = ['+', '-', '*', '/']
        of = tk.Frame(af, bg=c['bg'])
        of.grid(row=3,column=0,columnspan=2, pady=6)
        for s in ops:
            tk.Button(of, text=s, command=lambda s=s: self.calculate(s),
                      width=4, bg=c['btn'], fg=c['fg']).pack(side='left', padx=5)

        # Scientific
        sf = tk.LabelFrame(self, text="Scientific", bg=c['bg'], fg=c['fg'],
                           font=('Arial',12,'bold'), padx=10, pady=10)
        sf.pack(fill='x', padx=10, pady=8)
        tk.Label(sf, text="Input:", bg=c['bg'], fg=c['fg']).pack(side='left')
        self.sci_input = tk.Entry(sf, width=12)
        self.sci_input.pack(side='left', padx=6)
        sci_ops = ['sin','cos','tan','log','ln','sqrt','exp']
        for op in sci_ops:
            tk.Button(sf, text=op, command=lambda op=op: self.scientific(op),
                      width=5, bg=c['btn'], fg=c['fg']).pack(side='left', padx=6)

        # Result
        self.result = tk.Label(self, text="Result:", font=('Consolas',14),
                               bg=c['bg'], fg=c['fg'])
        self.result.pack(pady=12)

    def change_theme(self, t):
        self.current_theme = t
        self.apply_theme()
        for w in self.winfo_children(): w.destroy()
        self.create_widgets()

    def bind_keys(self):
        for char in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            self.bind(f'<KeyPress-{char}>', self.key_input)
        for k,s in [('plus','+'),('minus','-'),('asterisk','*'),('slash','/')]:
            self.bind(f'<KeyPress-{k}>', lambda e,s=s: self.calculate(s))
        self.bind('<Return>', lambda e: self.convert())

    def key_input(self, e):
        w = self.focus_get()
        if isinstance(w, tk.Entry): w.insert('end', e.char)

    def convert(self):
        try:
            v = int(self.conv_input.get().strip(), int(self.conv_from.get()))
            out = self._format(v, int(self.conv_to.get()))
        except:
            out = 'Conversion Error'
        self.show(out)

    def calculate(self, op):
        try:
            a = int(self.calc_a.get().strip(), int(self.calc_base.get()))
            b = int(self.calc_b.get().strip(), int(self.calc_base.get()))
            res = {'+':a+b,'-':a-b,'*':a*b,'/':a/b}.get(op)
            out = self._format(res, int(self.calc_base.get()))
        except:
            out = 'Calc Error'
        self.show(out)

    def scientific(self, op):
        try:
            x_str = self.sci_input.get().strip()
            x = float(x_str)
            funcs = {
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'log': lambda v: math.log10(v),
                'ln': math.log,
                'sqrt': math.sqrt,
                'exp': math.exp
            }
            val = funcs[op](math.radians(x) if op in ['sin','cos','tan'] else x)
            out = f"{op}({x_str}) = {val:.6f}"
        except:
            out = 'Sci Error'
        self.show(out)

    def _format(self, num, base):
        if isinstance(num, int):
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            sign = '-' if num<0 else ''
            n = abs(num)
            s = '' if n else '0'
            while n:
                s = digits[n%base] + s; n//=base
            return sign + s
        return str(num)

    def show(self, t):
        c = self.themes[self.current_theme]
        self.result.config(text=f"Result: {t}", fg=c['highlight'])
        def flash(i=0):
            color = c['fg'] if i%2 else c['highlight']
            self.result.config(fg=color)
            if i < 6: self.after(100, flash, i+1)
        flash()

if __name__ == '__main__':
    BaseCalculator().mainloop()
