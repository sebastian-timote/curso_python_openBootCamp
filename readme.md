* en los tema antes del tema 7 estan los ejemplo en cada commi
** MODULOS CURSOS PYTHON
tema 7 ejecutando modulos como scripts

# CURSO PYTHON
## TEMA 11 BASES DE DATOS
___
## verificacion de instalacion sqlite
- sqlite3 --version
## INSTALACION SQLITE3 EN UBUNTU
- sudo apt-get update
- sudo apt-get dist-upgrade
- sudo apt-get autoremove
- sudo apt-get update
- sudo apt install sqlite3
## COMANDOS SQLITE3
- para salir de sqlite3 --> CTRL + D O .quit
- para crear archivo de db e ingresar a èl ejecutamos --> sqlite3 nombre_archivo.db
- .show --> vemos la config del archivo de db
- .tables --> vemos las tablas creadas en la db
- .help --> vemos la ayuda
- para qcrear tablas o ver datos en tablas se crean con querys sql ejemplo:
    CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL);
- para agregar datos ala tabla:
    INSERT INTO users(id,username,password) VALUES(1, 'VROMN', 'MICALVE');
- para consultar datos a la tabla:
    SELECT * FROM users;

