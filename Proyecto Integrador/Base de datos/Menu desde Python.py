import mysql.connector

# Conectarse a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="8704",
  database="Dispositivos_Inteligentes"
)

# Método para actualizar un dispositivo
def actualizar_dispositivo(dispositivo_id, modelo_id, estado_id, numero_serie, direccion_instalacion, fecha_instalacion, coordenadas):
    cursor = db.cursor()
    sql = "UPDATE Dispositivos SET ModeloId=%s, EstadoId=%s, NumeroSerie=%s, DireccionInstalacion=%s, FechaInstalacion=%s, Coordenadas=%s WHERE Id=%s"
    values = (modelo_id, estado_id, numero_serie, direccion_instalacion, fecha_instalacion, coordenadas, dispositivo_id)
    cursor.execute(sql, values)
    db.commit()
    print("Dispositivo actualizado correctamente")

# Método para eliminar un dispositivo
def eliminar_dispositivo(dispositivo_id):
    cursor = db.cursor()
    sql = "DELETE FROM Dispositivos WHERE Id=%s"
    value = (dispositivo_id,)
    cursor.execute(sql, value)
    db.commit()
    print("Dispositivo eliminado correctamente")

# Método para mostrar el menú
def mostrar_menu():
    print("------- MENÚ -------")
    print("1. Actualizar dispositivo")
    print("2. Eliminar dispositivo")
    print("3. Salir")
    print("--------------------")

# Ciclo principal del programa
while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        dispositivo_id = int(input("Ingrese el ID del dispositivo a actualizar: "))
        modelo_id = int(input("Ingrese el nuevo ID del modelo: "))
        estado_id = int(input("Ingrese el nuevo ID del estado: "))
        numero_serie = input("Ingrese el nuevo número de serie: ")
        direccion_instalacion = input("Ingrese la nueva dirección de instalación: ")
        fecha_instalacion = input("Ingrese la nueva fecha de instalación (YYYY-MM-DD): ")
        coordenadas = input("Ingrese las nuevas coordenadas: ")
        actualizar_dispositivo(dispositivo_id, modelo_id, estado_id, numero_serie, direccion_instalacion, fecha_instalacion, coordenadas)
    elif opcion == "2":
        dispositivo_id = int(input("Ingrese el ID del dispositivo a eliminar: "))
        eliminar_dispositivo(dispositivo_id)
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

# Cerrar la conexión a la base de datos
db.close()
