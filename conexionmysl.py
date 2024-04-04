import mysql.connector

# Establecer la conexión a la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="usuarios"
)

if conexion.is_connected():
    print("Conexión exitosa a la base de datos")

    # Aquí puedes ejecutar consultas, actualizar datos, etc.

    # Por ejemplo, para ejecutar una consulta
    cursor = conexion.cursor()



    # Definir la consulta de inserción
    consulta = "INSERT INTO usuarios (username, email, password,img) VALUES (%s, %s, %s, %s)"
    
    # Valores del nuevo registro
    valores = ("tomas", "tomas@gmail.com", "1234","foto.jpg")

    # Ejecutar la consulta de inserción con los valores proporcionados
    cursor.execute(consulta, valores)

    # Hacer commit para guardar los cambios en la base de datos
    conexion.commit()

    print("Registro insertado exitosamente")


    cursor.execute("SELECT * FROM usuarios")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

    # No olvides cerrar la conexión cuando hayas terminado
    cursor.close()
    conexion.close()
    print("Conexión cerrada")
else:
    print("No se pudo conectar a la base de datos")
