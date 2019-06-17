-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS mint
USE mint

-- Crear tabla "Cliente"
CREATE TABLE IF NOT EXISTS clientes 
(
    clientes_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre              VARCHAR(255),
    apellidop           VARCHAR(255),
    apellidom           VARCHAR(255),
    fecha_nac           DATE,
    genero              VARCHAR(255),
    email               VARCHAR(255),
    telefono            VARCHAR(255),
    pais                VARCHAR(255),
    calle               VARCHAR(255),
    num_ext             VARCHAR(255),
    num_int             VARCHAR(255),
    col                 VARCHAR(255),
    estado              VARCHAR(255),
    cp                  SMALLINT,
    tarjeta             INT
)


-- Crear tabla "Pedido"
CREATE TABLE IF NOT EXISTS pedidos 
(
    pedido_id           INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    estado              VARCHAR(255),
    fecha               DATETIME,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id),
    FOREIGN KEY (carrito_id) REFERENCES carritos(carrito_id)
)


-- Crear tabla "Producto"
CREATE TABLE IF NOT EXISTS productos 
(
    producto_id         VARCHAR(255) NOT NULL PRIMARY KEY,
    marca               VARCHAR(255),
    modelo              VARCHAR(255),
    talla               INT,
    cantidad            INT,
    nombre              VARCHAR(255),
    precio              FLOAT,
    --imagen            ,
    FOREIGN KEY (subcategoria_id) REFERENCES subcategorias(subcategoria_id)
)


-- Crear tabla "Subcategoria"
CREATE TABLE IF NOT EXISTS subcategorias 
(
    subcategoria_id    INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre              VARCHAR(255)
    --imagen      
)


-- Crear tabla "Categoria"
CREATE TABLE IF NOT EXISTS categorias 
(
    categoria_id        INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre              VARCHAR(255),
    --imagen      , 
)


-- Crear tabla "Carrito"
CREATE TABLE IF NOT EXISTS carritos 
(
    carrito_id          INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    total               FLOAT,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(pedido_id),
    FOREIGN KEY (producto_id) REFERENCES productos(producto_id)
)


-- Crear tabla "Categoria_Subcategoria"
CREATE TABLE IF NOT EXISTS categorias_subcategorias 
(
    categoria_subcategoria_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id),
    FOREIGN KEY (subcategoria_id) REFERENCES subcategorias(subcategoria_id)
)