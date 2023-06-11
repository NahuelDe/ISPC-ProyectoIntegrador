import mysql.connector

class Modelos:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='8704',
            database='Dispositivos_Inteligentes'
        )
        self.cursor = self.connection.cursor()

    def insert(self, nombre):
        query = "INSERT INTO Modelos (Nombre) VALUES (%s)"
        values = (nombre,)
        self.cursor.execute(query, values)
        self.connection.commit()

    def select(self):
        query = "SELECT * FROM Modelos"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def __del__(self):
        self.cursor.close()
        self.connection.close()


class Estados:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='8704',
            database='Dispositivos_Inteligentes'
        )
        self.cursor = self.connection.cursor()

    def insert(self, nombre):
        query = "INSERT INTO Estados (Nombre) VALUES (%s)"
        values = (nombre,)
        self.cursor.execute(query, values)
        self.connection.commit()

    def select(self):
        query = "SELECT * FROM Estados"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def __del__(self):
        self.cursor.close()
        self.connection.close()


class Dispositivos:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='8704',
            database='Dispositivos_Inteligentes'
        )
        self.cursor = self.connection.cursor()

    def insert(self, modelo_id, estado_id, numero_serie, direccion_instalacion, fecha_instalacion, coordenadas):
        query = "INSERT INTO Dispositivos (ModeloId, EstadoId, NumeroSerie, DireccionInstalacion, FechaInstalacion, Coordenadas) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (modelo_id, estado_id, numero_serie, direccion_instalacion, fecha_instalacion, coordenadas)
        self.cursor.execute(query, values)
        self.connection.commit()

    def select(self):
        query = "SELECT * FROM Dispositivos"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def __del__(self):
        self.cursor.close()
        self.connection.close()


