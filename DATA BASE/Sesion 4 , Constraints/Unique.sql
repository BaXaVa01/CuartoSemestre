create table empleado
(id_empleado int not null, 
nombre_empleado varchar(50) not null, 
doc_identidad varchar(50)
constraint UQ_DOC_IDENTIDAD UNIQUE)

drop table empleado

alter table empleado
add constraint pk_id_empleado primary key(ID_empleado)

select * from empleado

