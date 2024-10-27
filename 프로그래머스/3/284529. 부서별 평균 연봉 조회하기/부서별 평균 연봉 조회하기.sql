select d.dept_id, dept_name_en, round(AVG(sal),0) as AVG_SAL
from hr_employees as e
left join hr_department as d
on e.dept_id = d.dept_id
group by dept_id
order by avg_sal desc;