select distinct a.num as ConsecutiveNums from (select num , LAG(num,1,0) over(order by id ) as prev, LEAD(num,1,0) over(order by id) as num_next from Logs ) a where a.num = a.prev and a.num = a.num_next 

/* select distinct(a.num) as ConsecutiveNums  from logs a
join logs b on a.id = b.id + 1 and a.num  = b.num
join logs c on a.id = c.id + 2  and a.num = c.num */

/* select distinct a.num ConsecutiveNums
from (select num, LAG(num, 1, 0) OVER(ORDER BY id) AS num_prev,
LEAD(num, 1, 0) OVER(ORDER BY id) AS num_next
from LOGS) a
where a.num = a.num_prev
and a.num = a.num_next */