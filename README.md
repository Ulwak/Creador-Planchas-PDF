# Creador-Planchas-PDF

Aplicacion de escritorio en Python para armar planchas de imagenes optimizadas en hoja **A4** y exportarlas directamente a formato **PDF** listo para imprimir (300 DPI).

## ¿Cómo funciona?

1. **Carga tus imagenes:** Colocá los archivos que quieras usar dentro de la carpeta `imagenes` (soporta formatos tradicionales como `JPEG`, `JPG`, `PNG`, `WebP`, etc.).
2. **Configura la plancha:** Ejecutá el programa y, en la ventana principal, marca las imágenes a incluir e ingresá el alto y ancho deseado en centímetros.
3. **Genera la vista previa:** Presioná el botón correspondiente para que el programa calcule automáticamente la orientación (vertical u horizontal) que mejor aprovecha la hoja A4 y distribuya las imágenes de forma pareja.
4. **Exporta a PDF:** Si el resultado te convence, presiona **"Crear PDF"** para guardar la plancha en alta resolución dentro de la carpeta `PDFs`.

## Requisitos e instalación

1. Cloná el repositorio e instalá la dependencia necesaria (`Pillow`):
   ```bash
   pip install pillow
   ```
2. Ejecutá el programa desde la carpeta `src`:
   ```bash
   python src/planchador.py
   ```
