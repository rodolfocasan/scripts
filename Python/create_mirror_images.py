# create_mirror_images.py
import os
import sys
import argparse
from PIL import Image, ImageOps





def create_mirror_images(folder_path):
    """
    Crea imágenes espejo de todas las imágenes en una carpeta especificada.

    Args:
        folder_path (str): Ruta de la carpeta que contiene las imágenes.
    """
    
    print("[ Script para obtener el modo espejo de imágenes ]")
    try:
        # Verifica si la carpeta existe
        if not os.path.exists(folder_path):
            print(f" [!!] La carpeta '{folder_path}' no existe.")
            return
        
        # Crea la carpeta 'mirrors' dentro de la carpeta original
        mirror_folder = os.path.join(folder_path, "mirrors")
        if not os.path.exists(mirror_folder):
            os.makedirs(mirror_folder)

        # Procesa todas las imágenes en la carpeta
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            # Verifica si es un archivo de imagen válido
            if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
                try:
                    # Abre la imagen
                    with Image.open(file_path) as img:
                        # Crea la imagen en modo espejo
                        mirrored_image = ImageOps.mirror(img)
                        
                        # Guarda la imagen en la carpeta 'mirrors' con el mismo nombre y formato
                        mirrored_path = os.path.join(mirror_folder, filename)
                        mirrored_image.save(mirrored_path, format=img.format, quality=100)
                        print(f" [OK] Imagen procesada y guardada en: {mirrored_path}")
                except Exception as e:
                    print(f" [!!] Error al procesar la imagen '{filename}': {e}")
        print(" - Proceso completado.")    
    except Exception as e:
        print(f" - Error general: {e}")





def main():
    # Configura el parser de argumentos
    parser = argparse.ArgumentParser(
        description = "Script para crear imágenes espejo en una carpeta dada."
    )
    parser.add_argument(
        "--images_folder",
        type = str,
        required = True,
        help = "Ruta de la carpeta que contiene las imágenes originales."
    )
    
    # Si no se pasa ningún argumento, muestra la ayuda automáticamente
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    # Llama a la función principal con el argumento proporcionado
    create_mirror_images(args.images_folder)





if __name__ == "__main__":
    main()