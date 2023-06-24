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

# Ejemplo de uso
actualizar_dispositivo(1, 2, 3, 'NS011', 'Calle Nueva 123', '2023-06-01', 'Coordenadas 11')
eliminar_dispositivo(2)

# Cerrar la conexión a la base de datos
db.close()
