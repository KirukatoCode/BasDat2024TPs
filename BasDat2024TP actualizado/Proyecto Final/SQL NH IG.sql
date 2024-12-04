CREATE DATABASE OnlineSalesSystem;
USE OnlineSalesSystem;

CREATE TABLE Categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

CREATE TABLE Producto (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES Categoria(id_categoria) ON DELETE SET NULL
);

CREATE TABLE Cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    telefono VARCHAR(20),
    direccion TEXT NOT NULL
);

CREATE TABLE Orden (
    id_orden INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    fecha DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Cliente(id_cliente) ON DELETE CASCADE
);

CREATE TABLE DetalleOrden (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    orden_id INT,
    producto_id INT,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (orden_id) REFERENCES Orden(id_orden) ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES Producto(id_producto) ON DELETE RESTRICT
);

INSERT INTO Categoria (nombre) VALUES 
    ('Tecnologia'),
    ('Snacks'),
    ('Bebidas'),
    ('Alcohol'),
    ('Tabaco'),
    ('Almacen'),
    ('Pilas'),
    ('Golosinas'),
    ('Juguetes'),
    ('Otros');

INSERT INTO Producto (nombre, descripcion, precio, stock, categoria_id) VALUES
    ('Auriculares Bluetooth', 'Auriculares inalámbricos con cancelación de ruido', 199.99, 80, 1),
    ('Smartwatch', 'Reloj inteligente con monitor de frecuencia cardíaca', 299.99, 90, 1),
    ('Snack de Frutos Secos', 'Mix de almendras, nueces y pasas', 5.99, 300, 2),
    ('Chocolatina', 'Chocolatina con relleno de avellanas', 1.49, 500, 8),
    ('Agua Mineral', 'Botella de agua sin gas 1L', 0.99, 600, 3),
    ('Cerveza Artesanal', 'Botella de cerveza estilo IPA 500ml', 3.99, 120, 4),
    ('Cigarrillos', 'Caja de 20 cigarrillos mentolados', 4.99, 200, 5),
    ('Harina', 'Bolsa de harina de trigo 1kg', 0.89, 400, 6),
    ('Pilas AA', 'Pack de 4 pilas alcalinas AA', 3.49, 250, 7),
    ('Dron', 'Dron compacto con cámara 4K', 599.99, 40, 1),
    ('Pelota de Básquet', 'Pelota oficial de la NBA', 39.99, 100, 4),
    ('Puzzle 1000 piezas', 'Puzzle de paisaje natural con 1000 piezas', 19.99, 150, 9),
    ('Pelota Saltarina', 'Pelota saltarina de colores', 2.99, 300, 9),
    ('Cuaderno de Notas', 'Cuaderno A4 con tapa dura', 5.49, 200, 10),
    ('Cargador Portátil', 'Batería externa de 20,000 mAh', 49.99, 1, 1);

INSERT INTO Cliente (nombre, email, telefono, direccion) VALUES
    ('Fernanda Castillo', 'fernanda.castillo@email.com', '9988776655', 'Calle Jardines 12'),
    ('Diego Herrera', 'diego.herrera@email.com', '7788996655', 'Av. Primavera 88'),
    ('Carolina Méndez', 'carolina.mendez@email.com', '6677885544', 'Calle Bosque 45'),
    ('Ricardo Vargas', 'ricardo.vargas@email.com', '5566774433', 'Av. del Lago 101'),
    ('Patricia Ortiz', 'patricia.ortiz@email.com', '4455663322', 'Calle del Norte 231'),
    ('Valeria Soto', 'valeria.soto@email.com', '3344552211', 'Calle Central 98'),
    ('Héctor Cruz', 'hector.cruz@email.com', '2233441100', 'Av. Gran Vista 202'),
    ('Camila Morales', 'camila.morales@email.com', '1122334455', 'Calle Lluvia 77'),
    ('Francisco Ruiz', 'francisco.ruiz@email.com', '5566778899', 'Av. Valle Dorado 105'),
    ('Natalia Peña', 'natalia.pena@email.com', '8899007766', 'Calle Aurora 300'),
    ('Roberto Gómez', 'roberto.gomez@email.com', '7766554433', 'Av. Horizonte 85'),
    ('Juliana López', 'juliana.lopez@email.com', '9988001122', 'Calle Dorada 456'),
    ('Andrés Jiménez', 'andres.jimenez@email.com', '4455667788', 'Av. del Río 67'),
    ('Manuela Torres', 'manuela.torres@email.com', '6677889900', 'Calle Azul 102'),
    ('Sebastián Medina', 'sebastian.medina@email.com', '3344556677', 'Calle de los Pinos 203');

INSERT INTO Orden (cliente_id, fecha, total) VALUES
    (1, '2024-06-11', 3489.10),
    (2, '2024-07-12', 1308.46),
    (3, '2024-08-13', 1398.27),
    (4, '2024-09-14', 153.24),
    (5, '2024-10-15', 30841.85);

INSERT INTO DetalleOrden (orden_id, producto_id, cantidad, precio_unitario) VALUES
    (1, 2, 3, 700.67),
    (2, 7, 4, 123.00),
    (3, 9, 2, 55.27),
    (4, 2, 1, 960.56),
    (5, 4, 5, 476.73);