
Select FirstName,
    LastName,
    EmailPromotion

From Person.Person

Where BusinessEntityID <= 10
Union
select FirstName,
LastName,
EmailPromotion
From Person.Person
where BusinessEntityID > 10 and BusinessEntityID <= 20;