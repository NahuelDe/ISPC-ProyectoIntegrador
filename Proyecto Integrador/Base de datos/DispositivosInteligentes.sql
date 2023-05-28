CREATE DATABASE DispositivosInteligentes;

use DispositivosInteligentes;

CREATE TABLE Dispositivos (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Modelo VARCHAR(50),
    NumeroSerie VARCHAR(50),
    DireccionInstalacion VARCHAR(100),
    FechaInstalacion DATE,
    Coordenadas VARCHAR(50),
    Estado VARCHAR(50)
);

CREATE TABLE Dispositivos (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Modelo VARCHAR(50),
    NumeroSerie VARCHAR(50),
    DireccionInstalacion VARCHAR(100),
    FechaInstalacion DATE,
    Coordenadas VARCHAR(50),
    Estado VARCHAR(50)
);
INSERT INTO dispositivos (Modelo, NumeroSerie, DireccionInstalacion, FechaInstalacion, Coordenadas, Estado)
VALUES
    ('Modelo 1', 'NS001', 'Primavera 123', '2023-05-20', 'Coordenadas 1', 'Operativo'),
    ('Modelo 2', 'NS002', 'Avenida del Sol 456', '2023-05-20', 'Coordenadas 2', 'Sin conexión'),
    ('Modelo 3', 'NS003', 'Camino de los Pinos 789', '2023-05-20', 'Coordenadas 3', 'Operativo'),
    ('Modelo 4', 'NS004', 'Carrera de la Luna 234', '2023-05-20', 'Coordenadas 4', 'Baja batería'),
    ('Modelo 2', 'NS005', 'Callejón del Río 567', '2023-05-20', 'Coordenadas 5', 'Operativo'),
    ('Modelo 1', 'NS006', 'Avenida Principal 890', '2023-05-20', 'Coordenadas 6', 'Sin conexión'),
    ('Modelo 3', 'NS007', 'Paseo de los Robles 1234', '2023-05-20', 'Coordenadas 7', 'Operativo'),
    ('Modelo 3', 'NS008', 'Plaza de la Fuente 5678', '2023-05-20', 'Coordenadas 8', 'Baja batería'),
    ('Modelo 1', 'NS009', 'Callejuela del Carmen 901', '2023-05-20', 'Coordenadas 9', 'Operativo'),
    ('Modelo 4', 'NS010', 'Avenida Central 2345', '2023-05-20', 'Coordenadas 10', 'Sin conexión');
    
 /*Listado de dispositivos totales*/
 SELECT * FROM dispositivos;
 
  /*Listado de dispositivos por modelos*/
 SELECT * FROM dispositivos WHERE Modelo = 'Modelo 2';
 
  /*Listado de dispositivos por estados*/
  SELECT * FROM dispositivos WHERE Estado = 'Operativo';
