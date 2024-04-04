import requests
import os
import mysql.connector
from faker import Faker
import bcrypt

def descargar_imagen(url, nombre_archivo):
    response = requests.get(url)
    if not os.path.exists("img"):
        os.makedirs("img")
    nombre_archivo="img/"+nombre_archivo;
    if response.status_code == 200:
        with open(nombre_archivo, 'wb') as f:
            f.write(response.content)
        #print("Imagen descargada con éxito como", nombre_archivo)
    else:
        print("Error al descargar la imagen:", response.status_code)





# Instanciar el generador Faker
fake = Faker()
url_base = "https://thispersondoesnotexist.com"
# Establecer la conexión a la base de datos MySQL
conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="usuarios"
    )

if conexion.is_connected():
        print("Conexión exitosa a la base de datos")
        cursor = conexion.cursor()
        for i in range(10):
            # Generar un nombre de usuario
            username = fake.user_name()
            # Generar una dirección de correo electrónico
            email = fake.email()
            # Generar una contraseña
            password = "1234"
            # Encriptar la contraseña usando bcrypt
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            nombre_archivo=username+".jpg"
            descargar_imagen(url_base,nombre_archivo)

            # Por ejemplo, para ejecutar una consulta
        
            #Definir la consulta de inserción
            consulta = "INSERT INTO usuarios (username, email, password,img) VALUES (%s, %s, %s, %s)"
            # Valores del nuevo registro
            valores = (username, email, hashed_password,nombre_archivo)
            # Ejecutar la consulta de inserción con los valores proporcionados
            cursor.execute(consulta, valores)
            # Hacer commit para guardar los cambios en la base de datos
            conexion.commit()


 # No olvides cerrar la conexión cuando hayas terminado
cursor.close()
conexion.close()
print("Conexión cerrada")
