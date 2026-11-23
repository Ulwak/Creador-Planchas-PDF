from seleccionador.seleccionador import listar_imagenes
from ventana.ventana import crear_ventana
from pathlib import Path

def main():
    ruta_raiz = Path(__file__).parent.parent
    imagenes = listar_imagenes(ruta_raiz)
    crear_ventana(imagenes)

if __name__ == "__main__":
    main()