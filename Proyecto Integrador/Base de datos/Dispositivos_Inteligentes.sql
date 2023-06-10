CREATE DATABASE Dispositivos_Inteligentes;

USE Dispositivos_Inteligentes;

CREATE TABLE Modelos (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50)
);

CREATE TABLE Estados (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50)
);

CREATE TABLE Dispositivos (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    ModeloId INT,
    EstadoId INT,
    NumeroSerie VARCHAR(50),
    DireccionInstalacion VARCHAR(100),
    FechaInstalacion DATE,
    Coordenadas VARCHAR(50),
    FOREIGN KEY (ModeloId) REFERENCES Modelos(Id),
    FOREIGN KEY (EstadoId) REFERENCES Estados(Id)
);

INSERT INTO Modelos (Nombre)
VALUES
    ('Modelo 1'),
    ('Modelo 2'),
    ('Modelo 3'),
    ('Modelo 4');

INSERT INTO Estados (Nombre)
VALUES
    ('Operativo'),
    ('Sin conexión'),
    ('Baja batería');

INSERT INTO Dispositivos (ModeloId, EstadoId, NumeroSerie, DireccionInstalacion, FechaInstalacion, Coordenadas)
VALUES
    (1, 1, 'NS001', 'Primavera 123', '2023-05-20', 'Coordenadas 1'),
    (2, 2, 'NS002', 'Avenida del Sol 456', '2023-05-20', 'Coordenadas 2'),
    (3, 1, 'NS003', 'Camino de los Pinos 789', '2023-05-20', 'Coordenadas 3'),
    (4, 3, 'NS004', 'Carrera de la Luna 234', '2023-05-20', 'Coordenadas 4'),
    (2, 1, 'NS005', 'Callejón del Río 567', '2023-05-20', 'Coordenadas 5'),
    (1, 2, 'NS006', 'Avenida Principal 890', '2023-05-20', 'Coordenadas 6'),
    (3, 1, 'NS007', 'Paseo de los Robles 1234', '2023-05-20', 'Coordenadas 7'),
    (3, 3, 'NS008', 'Plaza de la Fuente 5678', '2023-05-20', 'Coordenadas 8'),
    (1, 1, 'NS009', 'Callejuela del Carmen 901', '2023-05-20', 'Coordenadas 9'),
    (4, 2, 'NS010', 'Avenida Central 2345', '2023-05-20', 'Coordenadas 10');

 
