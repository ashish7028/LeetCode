select Distinct S1.* from Stadium S1 join Stadium S2 join Stadium S3 on 
(S1.id = S2.id-1 and S1.id = S3.id-2 or 
S1.id = S2.id+1 and S1.id = S3.id-1 or 
S1.id = S2.id+1 and S1.id = S3.id+2)
where S1.people >=100 and  S2.people >=100 and S3.people >=100
order by visit_date