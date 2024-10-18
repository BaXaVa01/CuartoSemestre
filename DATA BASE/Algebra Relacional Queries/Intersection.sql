Select BusinessEntityID
From HumanResources.Employee
INTERSECT
Select CustomerID
From Sales.Customer
Order By 1 ;