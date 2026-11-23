from PIL import Image, ImageTk
import random

def mostrar_vista_previa(hoja_A4, vista_previa_etiqueta):
    hoja_vista_pre = hoja_A4.copy()
    hoja_vista_pre.thumbnail((296, 416), Image.Resampling.LANCZOS)
    plantilla_foto = ImageTk.PhotoImage(hoja_vista_pre)

    vista_previa_etiqueta.config(image = plantilla_foto)
    vista_previa_etiqueta.image = plantilla_foto

def generar_vista_previa(imagenes_seleccionadas, ancho, altura, total, medida_h_px, medida_v_px):
    
    unidades, resto = divmod(total, len(imagenes_seleccionadas))

    imagenes_para_pegar = []
    for imagen in imagenes_seleccionadas:
        imagenes_para_pegar.extend([imagen] * unidades)

    imagenes_para_pegar.extend(random.sample(imagenes_seleccionadas, resto))

    columnas_A4 = ancho // medida_h_px

    hoja_A4 = Image.new("RGB", (ancho, altura), "white")

    for indice, imagen in enumerate(imagenes_para_pegar):
    
        fila = indice // columnas_A4
        columna = indice % columnas_A4

        coordenada_x = columna * medida_h_px
        coordenada_y = fila * medida_v_px
    
        hoja_A4.paste(imagen, (coordenada_x, coordenada_y), mask=imagen)

    for imagen in imagenes_seleccionadas:
        imagen.close()

    return hoja_A4
