# Proyecto de Sistema Distribuido: Banco

El proyecto consiste en un sistema distribuido utilizando **Oracle Express 21c** y dos **contenedores de Docker** con imagen. Estos contenedores se encuentran conectados por medio de un **DATABASE LINK**. 

Las tablas globales que se encuentran en ambos contenedores son:
* sucursal: 
* préstamo

El esquema de cada tabla se encuentra en el archivo **gBanco.sql**.

El objetivo de la aplicación es poder realizar operaciones en dos contenedores diferentes, y que se puedan replicar los cambios. 

Las tablas sucursal y préstamo se fragmentaron con base en la región:
* sucursal1 y prestamo1 corresponden al primer contenedor, donde se encuentran los datos pertenecientes a la región 1
* sucursal2 y prestamo2 corresponden al segundo contenedor, donde se encuentran los datos pertenecientes a la región 2

