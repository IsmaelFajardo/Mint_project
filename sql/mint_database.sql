-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS mint
USE mint

-- Crear tabla "Cliente"
CREATE TABLE IF NOT EXISTS clientes 
(
    id                  INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre              VARCHAR(50),
    apellidop           VARCHAR(50),
    apellidom           VARCHAR(50),
    fecha_nac           DATE,
    genero              TINYINT,
    email               VARCHAR(100),
    telefono            VARCHAR(10),
    pais                VARCHAR(3), --CODIGO ISO
    calle               VARCHAR(100),
    num_ext             VARCHAR(10),
    num_int             VARCHAR(10),
    col                 VARCHAR(50),
    estado              VARCHAR(3), --CODIGO ISO
    cp                  SMALLINT,
    tarjeta             INT
);


-- Crear tabla "Pedido"
CREATE TABLE IF NOT EXISTS pedidos
(
    id                  INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    estado              INT,
    fecha               DATETIME,
    FOREIGN KEY (cliente_id) REFERENCES clientes.id,
    FOREIGN KEY (carrito_id) REFERENCES carritos.id,
);


-- Crear tabla "Producto"
CREATE TABLE IF NOT EXISTS productos 
(
    id                  VARCHAR(50) NOT NULL PRIMARY KEY,
    marca               VARCHAR(50),
    modelo              VARCHAR(50),
    talla               INT,
    cantidad            INT,
    nombre              VARCHAR(50),
    precio              DECIMAL(11,2),
    imagen              VARCHAR(255), --URL de la ubicación de la imagen   
    FOREIGN KEY (categoria_id) REFERENCES categorias.id
    FOREIGN KEY (subcategoria_id) REFERENCES subcategorias.id
);


-- Crear tabla "Subcategoria"
CREATE TABLE IF NOT EXISTS subcategorias 
(
    id                  INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre              VARCHAR(50)
    imagen              VARCHAR(255) --URL de la ubicación de la imagen      
);


-- Crear tabla "Categoria"
CREATE TABLE IF NOT EXISTS categorias 
(
    id                  INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre              VARCHAR(50),
    imagen              VARCHAR(255), --URL de la ubicación de la imagen   
);


-- Crear tabla "Pedido_Detalle"
CREATE TABLE IF NOT EXISTS pedidos_detalle 
(
    cantidad            INT,
    subtotal            DECIMAL(11,2),
    FOREIGN KEY (pedido_id) REFERENCES pedidos.id,
    FOREIGN KEY (producto_id) REFERENCES productos.id,
);