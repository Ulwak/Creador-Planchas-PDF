from seleccionador.seleccionador import listar_imagenes
from ventana.ventana import crear_ventana
from pathlib import Path

def main():
    ruta_raiz = Path(__file__).parent.parent
    imagenes = listar_imagenes(ruta_raiz)
    ventana, check_img, botones, altura, ancho, error = crear_ventana(imagenes)
    botones[0]
    ventana.mainloop()

if __name__ == "__main__":
    main()