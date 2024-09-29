Create table cita (
ID_cita int primary key, 
nombre_cita varchar(50) null,
fecha_solicitud date not null default GetDate())
Go

drop table cita

Insert into cita (id_cita, nombre_cita)
values (1, 'consulta Medica')

select * from cita

SELECT @sql += ' Drop table ' + QUOTENAME(s.NAME) + '.' + QUOTENAME(t.NAME) + '; '
FROM   sys.tables t
       JOIN sys.schemas s
         ON t.[schema_id] = s.[schema_id]
WHERE  t.type = 'U'

Exec sp_executesql @sql