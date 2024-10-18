SElect BusinessENtityID
from Person.Person
Where BusinessEntityID < 50
EXCEPT
Select BusinessEntityID
from HumanResources.Employee
Where BusinessEntityID < 50