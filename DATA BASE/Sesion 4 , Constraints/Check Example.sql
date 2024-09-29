Create table empleado
(id_empleado int constraint pq_id_empleado primary key, 
nombre_empleado varchar(50) null, salario int constraint ck_salario_base check (salario > 0))
go 

drop table empleado



Alter table empleado add salario DECIMAL(10, 2) constraint ck_salario_base check (salario > 0)