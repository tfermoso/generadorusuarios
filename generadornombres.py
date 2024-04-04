from faker import Faker
import bcrypt

# Instanciar el generador Faker
fake = Faker()

# Generar un nombre de usuario
username = fake.user_name()

# Generar una dirección de correo electrónico
email = fake.email()

# Generar una contraseña
password = "1234"

# Encriptar la contraseña usando bcrypt
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

print("Nombre de usuario:", username)
print("Correo electrónico:", email)
print("Contraseña generada:", password)
print("Contraseña encriptada:", hashed_password)
