
# Importamos la librería para trabajar con bases de datos SQLite
import sqlite3
import mysql
# Creamos una conexión a la base de datos
conn = sqlite3.connect('usuarios.db')

# Creamos la tabla de usuarios si no existe
conn.execute('''CREATE TABLE IF NOT EXISTS usuarios
             (usuario TEXT PRIMARY KEY NOT NULL,
             contrasena TEXT NOT NULL);''')

# Función para verificar si el usuario y la contraseña son correctos
def verificar_login(usuario, contrasena):
    cursor = conn.execute("SELECT contrasena from usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()
    if resultado is not None and resultado[0] == contrasena:
        return True
    else:
        return False

# Interfaz de usuario para ingresar el usuario y la contraseña
usuario = input("Ingrese su usuario: ")
contrasena = input("Ingrese su contraseña: ")

# Verificamos si el usuario y la contraseña son correctos
if verificar_login(usuario, contrasena):
    print("Login exitoso!")
else:
    print("Usuario o contraseña incorrectos.")
