def listar_imagenes(ruta_raiz):
    ruta_imagenes = ruta_raiz / "imagenes"
    extensiones_imagenes = [".png", ".jpeg", ".jpg", ".gif", ".webp", ".bmp"]
    imagenes = [archivo for archivo in ruta_imagenes.iterdir() if archivo.is_file() and archivo.suffix() in extensiones_imagenes]
    return imagenes
    