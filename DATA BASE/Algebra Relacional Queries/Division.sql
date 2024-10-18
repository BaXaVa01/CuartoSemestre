-- Division Divide

Select BusinessEntityID as EmployeeID into #AllEmployees from HumanResources.Employee;
SELECT DepartmentID into #AllDepartments from HumanResources.Department;

Select distinct BusinessEntityID as employeeID, departmentID into #EmployeeDepartments from HumanResources.EmployeeDepartmentHistory;


Select ed.EmployeeID from #EmployeeDepartments ed GROUP by ed.employeeID having count(Distinct ed.DepartmentID) = (select COUNT(*)From#AllDepartments)