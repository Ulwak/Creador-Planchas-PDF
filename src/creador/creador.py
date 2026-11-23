from datetime import datetime
from PIL import Image

A4_HORIZONTAL_PX = 2480
A4_VERTICAL_PX = 3508

def reformar_imagenes(imagenes_seleccionadas, medida_v, medida_h):
    imagenes_redimensionadas = []
    for imagen in imagenes_seleccionadas:
        with Image.open(imagen) as img:
            img_estandarizada = img.convert("RGBA")
            img_redimensionada = img_estandarizada.resize((medida_h, medida_v), Image.Resampling.LANCZOS)    
            imagenes_redimensionadas.append(img_redimensionada)
    return imagenes_redimensionadas

def calcular_imagenes(medida_v, medida_h, imagenes_seleccionadas):
    medida_v_p = int((float(medida_v) * 300) // 2.54)
    medida_h_p = int((float(medida_h) * 300) // 2.54)

    total_vertical = (A4_HORIZONTAL_PX // medida_h_p) * (A4_VERTICAL_PX // medida_v_p)
    total_horizontal = (A4_HORIZONTAL_PX // medida_v_p) * (A4_VERTICAL_PX // medida_h_p)

    imagenes_seleccionadas = reformar_imagenes(imagenes_seleccionadas, medida_v_p, medida_h_p)

    if total_horizontal > total_vertical:
        return imagenes_seleccionadas, A4_VERTICAL_PX, A4_HORIZONTAL_PX, total_horizontal, medida_h_p, medida_v_p
    else:
        return imagenes_seleccionadas, A4_HORIZONTAL_PX, A4_VERTICAL_PX, total_vertical, medida_h_p, medida_v_p



def crear_pdf(hoja_A4, error, ruta_raiz):
    carpeta_pdf = ruta_raiz / "PDFs"
    carpeta_pdf.mkdir(exist_ok=True)

    nombre_plancha = carpeta_pdf / f"plancha_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    hoja_A4.save(nombre_plancha, format="PDF", resolution=300.0)

    hoja_A4.close()

    error.configure(text = "PDF Guardado en la carpeta de PDFs")
