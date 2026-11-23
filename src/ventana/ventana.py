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
        check = tk.BooleanVar()
        var_check.append(check)

    check_usar = []
    for imagen, num in zip(imagenes, range(len(imagenes))):
        ttk.Label(pestaña_selec_img, text = imagen.name).grid(column = 0, row = num)
        ttk.Label(pestaña_selec_img, text = "¿Utilizar esta imagen para la plantilla en el PDF?").grid(column = 1, row = num)
        boton = tk.Checkbutton(pestaña_selec_img, variable = var_check[num])
        boton.deselect()
        boton.grid(column = 2, row = num)
        check_usar.append((imagen, boton))

    botones = []
    b_mostrar_vista = ttk.Button(pestaña_selec_img, text = "Mostrar Vista Previa En 'Vista Previa'")
    b_mostrar_vista.grid(column = 0, row = len(imagenes) + 1)
    botones.append(b_mostrar_vista)

    b_crear_pdf = ttk.Button(pestaña_vista_previa, text = "Crear PDF")
    b_crear_pdf.grid(column = 0, row = 0)
    botones.append(b_crear_pdf)

    altura_img = tk.IntVar()
    ancho_img = tk.IntVar()

    ttk.Label(pestaña_selec_img, text = "Altura de las imagenes en CM:").grid(column = 0, row = len(imagenes) + 2)
    ttk.Entry(pestaña_selec_img, textvariable = altura_img).grid(column = 1, row = len(imagenes) + 2)

    ttk.Label(pestaña_selec_img, text = "Ancho de las imagenes en CM:").grid(column = 0, row = len(imagenes) + 3)
    ttk.Entry(pestaña_selec_img, textvariable = ancho_img).grid(column = 1, row = len(imagenes) + 3)

    error = ttk.Label(pestaña_selec_img, text = "")
    error.grid(column = 0, row = len(imagenes) + 4)

    return check_usar, botones, altura_img, ancho_img, error
    
def crear_ventana(imagenes):
    ventana = tk.Tk()
    ventana.title("Generador de planchas en PDF")
    ventana.resizable(0, 0)
    check_img, botones, altura, ancho, error = crear_contenido(ventana, imagenes)
    return ventana, check_img, botones, altura, ancho, error