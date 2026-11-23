from seleccionador.seleccionador import listar_imagenes, obtener_imagenes_seleccionadas
from ventana.ventana import crear_ventana
from creador.creador import calcular_imagenes, crear_pdf
from ventana.vista_previa import generar_vista_previa, mostrar_vista_previa
from pathlib import Path

hoja = {"hoja": None}

def mostrar_vista(altura, ancho, error, check_img, etiqueta_vista_previa, boton_pdf):
    imagenes_seleccionadas = obtener_imagenes_seleccionadas(check_img)
    if imagenes_seleccionadas == 1:
        error.configure(text = "No se selecciono ninguna imagen.")
    else:
        altura_c = altura.get()
        ancho_c = ancho.get()
        if ancho_c == 0 and altura_c == 0:
            error.configure(text = "El campo de altura y ancho no puede quedar en 0")
        else:
            imagenes_seleccionadas, ancho, altura, total, medida_h_px, medida_v_px = calcular_imagenes(altura_c, ancho_c, imagenes_seleccionadas)
            if len(imagenes_seleccionadas) > total:
                error.configure(text = "Se selecciono una cantidad de imagenes mayor a las que entran en la hoja. Reduzca el tamaño o seleccione menos. (Seran mostradas al azar en caso contrario)")
            else:    
                hoja["hoja"] = generar_vista_previa(imagenes_seleccionadas, ancho, altura, total, medida_h_px, medida_v_px)
                mostrar_vista_previa(hoja["hoja"], etiqueta_vista_previa)
                boton_pdf.configure(state = "activate")

def guardar_pdf(hoja_A4, error, ruta_raiz):
    crear_pdf(hoja_A4, error, ruta_raiz)

def main():
    ruta_raiz = Path(__file__).parent.parent
    imagenes = listar_imagenes(ruta_raiz)
    ventana, check_imagenes, botones, altura, ancho, error, etiqueta_vista_previa = crear_ventana(imagenes)
    botones[0].configure(command = lambda: mostrar_vista(altura, ancho, error, check_imagenes, etiqueta_vista_previa, botones[1]))
    botones[1].configure(command = lambda: guardar_pdf(hoja["hoja"], error, ruta_raiz))
    ventana.mainloop()

if __name__ == "__main__":
    main()