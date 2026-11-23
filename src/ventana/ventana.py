import tkinter as tk
from tkinter import ttk

def crear_contenido(ventana, imagenes):
    tab_Control = ttk.Notebook(ventana)
    
    pestaña_selec_img = ttk.Frame(tab_Control)
    tab_Control.add(pestaña_selec_img, text = "Seleccionar Imagenes")

    pestaña_vista_previa = ttk.Frame(tab_Control)
    tab_Control.add(pestaña_vista_previa, text = "Vista Previa")
    
    tab_Control.pack(expand = 1, fill = "both")

    check_usar = []
    for num, imagen in enumerate(imagenes):
        check = tk.BooleanVar()

        ttk.Label(pestaña_selec_img, text = imagen.name).grid(column = 0, row = num)
        ttk.Label(pestaña_selec_img, text = "¿Utilizar esta imagen para la plantilla en el PDF?").grid(column = 1, row = num)
        
        boton = tk.Checkbutton(pestaña_selec_img, variable = check)
        boton.deselect()
        boton.grid(column = 2, row = num)

        check_usar.append((imagen, check))

    botones = []
    b_mostrar_vista = ttk.Button(pestaña_selec_img, text = "Mostrar Vista Previa En 'Vista Previa'")
    b_mostrar_vista.grid(column = 0, row = len(imagenes) + 3)
    botones.append(b_mostrar_vista)

    marco_vista_previa = tk.Frame(pestaña_vista_previa, width=300, height=420)
    marco_vista_previa.pack_propagate(False)
    marco_vista_previa.grid(column = 0, row = 0)
    
    etiqueta_vista_previa = ttk.Label(marco_vista_previa, text = "Vista previa de la hoja A4:" )
    etiqueta_vista_previa.pack(expand=True, fill="both")

    b_crear_pdf = ttk.Button(pestaña_vista_previa, text = "Crear PDF", state = "disabled")
    b_crear_pdf.grid(column = 0, row = 1)
    botones.append(b_crear_pdf)

    altura_img = tk.IntVar()
    ancho_img = tk.IntVar()

    ttk.Label(pestaña_selec_img, text = "Altura de las imagenes en CM:").grid(column = 0, row = len(imagenes) + 1)
    ttk.Entry(pestaña_selec_img, textvariable = altura_img).grid(column = 1, row = len(imagenes) + 1)

    ttk.Label(pestaña_selec_img, text = "Ancho de las imagenes en CM:").grid(column = 0, row = len(imagenes) + 2)
    ttk.Entry(pestaña_selec_img, textvariable = ancho_img).grid(column = 1, row = len(imagenes) + 2)

    error = ttk.Label(pestaña_selec_img, text = "")
    error.grid(column = 0, row = len(imagenes) + 4)

    return check_usar, botones, altura_img, ancho_img, error, etiqueta_vista_previa
    
def crear_ventana(imagenes):
    ventana = tk.Tk()
    ventana.title("Generador de planchas en PDF")
    ventana.resizable(0, 0)
    check_img, botones, altura, ancho, error, etiqueta_vista_previa = crear_contenido(ventana, imagenes)
    return ventana, check_img, botones, altura, ancho, error, etiqueta_vista_previa