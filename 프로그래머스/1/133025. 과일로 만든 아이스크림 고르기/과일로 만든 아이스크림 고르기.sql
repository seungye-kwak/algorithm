-- 코드를 입력하세요
SELECT FIRST_HALF.FLAVOR
from FIRST_HALF
left join ICECREAM_INFO
on ICECREAM_INFO.flavor = FIRST_HALF.flavor
where FIRST_HALF.total_order >= 3000
and ICECREAM_INFO.INGREDIENT_TYPE = 'fruit_based'
order by FIRST_HALF.total_order desc