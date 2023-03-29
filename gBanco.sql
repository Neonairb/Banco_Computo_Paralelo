drop table sucursal;
drop table prestamo;

create table sucursal
   (idsucursal		varchar(5),
    nombresucursal	varchar(15)	not null,
    ciudadsucursal     varchar(15)	not null,
    activos 		number		not null,
    region	           numbrer,
    primary key(idsucursal));

create table prestamo
   (noprestamo 	varchar(15)	not null,
    idsucursal	varchar(5),
    cantidad 	number		not null,
    primary key(noprestamo));

insert into sucursal	values ('S0001', 'Downtown',		'Brooklyn',	 	900000,1);
insert into sucursal	values ('S0002', 'Redwood',		'Palo Alto',	2100000, 1);
insert into sucursal	values ('S0003', 'Perryridge',	'Horseneck',	1700000, 1);
insert into sucursal	values ('S0004', 'Mianus',		'Horseneck',	 400200, 1);
insert into sucursal	values ('S0005', 'Round Hill',	'Horseneck',	8000000, 1);
insert into sucursal	values ('S0006', 'Pownal',		'Bennington',	 400000,2);
insert into sucursal	values ('S0007', 'North Town',	'Rye',		3700000, 2);
insert into sucursal	values ('S0008', 'Brighton',		'Brooklyn',		7000000, 2);
insert into sucursal	values ('S0009', 'Central',		'Rye',		 400280, 2);

insert into prestamo	values ('L-17',		'S0001',	1000);
insert into prestamo	values ('L-23',		'S0002',	2000);
insert into prestamo	values ('L-15',		'S0003',	1500);
insert into prestamo	values ('L-14',		'S0001',	1500);
insert into prestamo	values ('L-93',		'S0004',	500);
insert into prestamo	values ('L-11',		'S0005',	900);
insert into prestamo	values ('L-16',		'S0003',	1300);
insert into prestamo	values ('L-20',		'S0007',	7500);
insert into prestamo	values ('L-21',		'S0009',	570);

