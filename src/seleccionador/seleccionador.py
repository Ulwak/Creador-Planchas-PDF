def listar_imagenes(ruta_raiz):
    ruta_imagenes = ruta_raiz / "imagenes"
    extensiones_imagenes = [".png", ".jpeg", ".jpg", ".gif", ".webp", ".bmp"]
    imagenes = [archivo for archivo in ruta_imagenes.iterdir() if archivo.is_file() and archivo.suffix in extensiones_imagenes]
    print(imagenes)
    return imagenes

def obtener_imagenes_seleccionadas(imagenes):
    imagenes_seleccionadas = []
    for imagen, check in imagenes:
        if check.get() == True:
            imagenes_seleccionadas.append(imagen)
    if imagenes_seleccionadas:
        return imagenes_seleccionadas
    else:
        return 1
    