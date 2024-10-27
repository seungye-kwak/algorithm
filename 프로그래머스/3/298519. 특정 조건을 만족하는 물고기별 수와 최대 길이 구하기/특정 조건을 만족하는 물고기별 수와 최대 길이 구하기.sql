select count(fish_type) as fish_count, max(length) as MAX_LENGTH, fish_type
from (select fish_type, ifnull(length, 10) as length, time
    from fish_info) as info
group by fish_type
having AVG(length) >= 33
order by fish_type