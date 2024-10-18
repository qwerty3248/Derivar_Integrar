import sympy as sp
import tkinter as tk
from tkinter import messagebox

# Función para derivar
def derivar():
    try:
        funcion = entrada.get()
        x = sp.symbols('x')
        derivada = sp.diff(funcion, x)
        salida.delete(1.0, tk.END)
        salida.insert(tk.END, f"Derivada: {derivada}")
    except Exception as e:
        messagebox.showerror("Error", "Introduce una función válida para derivar")

# Función para integrar
def integrar():
    try:
        funcion = entrada.get()
        x = sp.symbols('x')
        integral = sp.integrate(funcion, x)
        salida.delete(1.0, tk.END)
        salida.insert(tk.END, f"Integral: {integral}")
    except Exception as e:
        messagebox.showerror("Error", "Introduce una función válida para integrar")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Derivación e Integración")

# Entrada de texto
tk.Label(ventana, text="Introduce la función (en términos de x):").pack()
entrada = tk.Entry(ventana, width=50)
entrada.pack()

# Botones
tk.Button(ventana, text="Derivar", command=derivar).pack(pady=5)
tk.Button(ventana, text="Integrar", command=integrar).pack(pady=5)

# Salida
salida = tk.Text(ventana, height=5, width=50)
salida.pack()

# Ejecutar la interfaz
ventana.mainloop()
