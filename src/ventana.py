import tkinter as tk 
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Aviso", "¡Boton presionado!")
ventana = tk.Tk()
ventana.title("ventana simple")


label = tk.Label(ventana, text="Hola mundo", font=("Arial", 30))
label.pack()


boton = tk.Button(ventana, text="Haz clic aqui")
boton.pack

label = tk.Label(ventana, text="presiona el boton para ver un mensaje")
label.pack()

boton = tk.Button(ventana, text="Haz clic aqui", command=mostrar_mensaje)
boton.pack(pady=10)

ventana.mainloop()