select sum(score) as score, e.emp_no, e.emp_name, e.position, e.email
from hr_grade as g
left join hr_employees as e
on e.emp_no = g.emp_no
group by emp_no
order by score desc
limit 1;

# select *
# from (select sum(score) as score, e.emp_no, e.emp_name, e.position, e.email
#      from hr_grade as g
#      left join hr_employees as e
#      on e.emp_no = g.emp_no
#      group by emp_no)

