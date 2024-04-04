import requests
import os

def descargar_imagen(url, nombre_archivo):
    response = requests.get(url)
    if response.status_code == 200:
        with open(nombre_archivo, 'wb') as f:
            f.write(response.content)
        print("Imagen descargada con éxito como", nombre_archivo)
    else:
        print("Error al descargar la imagen:", response.status_code)

def descargar_imagenes_desde_thispersondoesnotexist(num_imagenes):
    url_base = "https://thispersondoesnotexist.com"
    for i in range(1, num_imagenes + 1):
        url = f"{url_base}"
        nombre_archivo = f"persona_{i}.jpg"
        descargar_imagen(url, nombre_archivo)

if __name__ == "__main__":
    num_imagenes = int(input("Ingrese el número de imágenes que desea descargar: "))
    descargar_imagenes_desde_thispersondoesnotexist(num_imagenes)
