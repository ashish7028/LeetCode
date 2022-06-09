select a.name as Employee from Employee a join Employee b on a.managerId = b.id where a.salary > b.salary


/*select a.name as Employee_name, b.name as  manager_name from Employee a join Employee b where a.managerId  = b.id */