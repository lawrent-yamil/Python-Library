-- hacer la tabla de libros con cod_libro, nom_libro para mariaDB

CREATE TABLE libros (
  cod_libro INTEGER NOT NULL,
  nom_libro VARCHAR(255) NOT NULL,
  PRIMARY KEY (cod_libro)
);


-- agregar datos a la tabla de libros
INSERT INTO libros (cod_libro,nom_libro) VALUES (1,'El señor de los anillos');

INSERT INTO libros (cod_libro,nom_libro) VALUES (2,'El principito');
INSERT INTO libros (cod_libro,nom_libro) VALUES (3,'El señor de los anillos 2');
INSERT INTO libros (cod_libro,nom_libro) VALUES (4,'El señor de los anillos 3');
INSERT INTO libros (cod_libro,nom_libro) VALUES (5,'El señor de los anillos 4');
INSERT INTO libros (cod_libro,nom_libro) VALUES (6,'Tras la muerte de sus padres');
INSERT INTO libros (cod_libro,nom_libro) VALUES (7,'El señor de los anillos 5');
INSERT INTO libros (cod_libro,nom_libro) VALUES (8,'Narcos');


-- mirar los datos de libros
SELECT * FROM libros;
-- agregar una columna a la tabla de libros descripcion
ALTER TABLE libros ADD COLUMN descripcion VARCHAR(255);
-- agregar una descripcion a los libros
UPDATE libros SET descripcion = 'Un libro muy bueno'

-- hacer la tabla de usuarios
CREATE TABLE usuarios (
  cedula INTEGER NOT NULL,
  nom_usuario VARCHAR(255) NOT NULL,
  PRIMARY KEY (cedula)
);

-- agregar datos a la tabla de usuarios
INSERT INTO usuarios (cedula,nom_usuario) VALUES (1,'lawrent');

-- ver todas las tablas
SHOW TABLES;

-- hacer la tabla de prestamos
CREATE TABLE prestamos (
  cod_prestamo INTEGER NOT NULL,
  tipo_prestamo VARCHAR(255) NOT NULL,
  PRIMARY KEY (cod_prestamo)
);

-- hacer un join de usuarios libros y prestamos