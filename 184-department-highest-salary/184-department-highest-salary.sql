select Department,Employee, Salary from (select b.name as Department , a.name as Employee , a.salary as Salary  , dense_rank() over(partition by departmentId order by salary desc ) r  from 
Employee a join Department b on a.departmentId  = b.id ) z where r = 1

/* select d.name as Department , e.name  as Employee , Salary  from Employee e 
join Department d on e.departmentId = d.id where (departmentId,salary) in (select departmentId , max(salary) as salary  from Employee group by departmentId ) */