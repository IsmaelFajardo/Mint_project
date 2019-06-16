-- Crear la base de datos
CREATE DATABASE mint
USE mint

-- Crear tabla "Cliente"
CREATE TABLE cliente(
    clienteid   INT NOT NULL AUTO_INCREMENT,
    nombre      VARCHAR(255),
    apellidop   VARCHAR(255),
    apellidom   VARCHAR(255),
    fecha_nac   DATE,
    genero      VARCHAR(255),
    email       VARCHAR(255),
    telefono    VARCHAR(255),
    pais        VARCHAR(255),
    calle       VARCHAR(255),
    num_ext     VARCHAR(255),
    num_int     VARCHAR(255),
    col         VARCHAR(255),
    estado      VARCHAR(255),
    cp          SMALLINT,
    tarjeta     INT,
    PRIMARY_KEY (clienteid)
)


-- Crear tabla "Cliente"
CREATE TABLE pedido(

)


-- Crear tabla "Cliente"
CREATE TABLE producto(

)


-- Crear tabla "Cliente"
CREATE TABLE subcategoria(

)


-- Crear tabla "Cliente"
CREATE TABLE categoria(

)


-- Crear tabla "Cliente"
CREATE TABLE carrito


-- Crear tabla "Cliente"
CREATE TABLE categoria_subcategoria