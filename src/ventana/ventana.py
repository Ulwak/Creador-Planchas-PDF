import tkinter as tk
from tkinter import ttk

def crear_contenido(ventana, imagenes):
    tab_Control = ttk.Notebook(ventana)
    
    pestaña_selec_img = ttk.Frame(tab_Control)
    tab_Control.add(pestaña_selec_img, text = "Seleccionar Imagenes")

    pestaña_vista_previa = ttk.Frame(tab_Control)
    tab_Control.add(pestaña_vista_previa, text = "Vista Previa")
    
    tab_Control.pack(expand = 1, fill = "both")

    var_check = []
    for _ in range(len(imagenes)):
        check = tk.BooleanVar
        var_check.append(check)

    check_usar = []
    for nom_img, num in zip(imagenes, range(len(imagenes))):
        ttk.Label(pestaña_selec_img, text = nom_img.name).grid(column = 0, row = num)
        ttk.Label(pestaña_selec_img, text = "¿Utilizar esta imagen para la plantilla en el PDF?").grid(column = 2, row = num)
        boton = ttk.Checkbutton(pestaña_selec_img, variable = var_check[num])
        boton.grid(column = 3, row = num)
        check_usar.append(boton)

def crear_ventana(imagenes):
    ventana = tk.Tk()
    ventana.title("Generador de planchas en PDF")
    ventana.resizable(0, 0)
    crear_contenido(ventana, imagenes)
    ventana.mainloop()