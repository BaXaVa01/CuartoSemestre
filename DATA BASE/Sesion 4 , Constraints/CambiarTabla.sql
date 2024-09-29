Alter table empleado
alter column salario decimal (20,2) not null

--Se cambia la longitud del campo salario de 18 a 20


--Para cambiar el nomber a una tabla: 
sp_rename 'dbo.empleado','empleado'
