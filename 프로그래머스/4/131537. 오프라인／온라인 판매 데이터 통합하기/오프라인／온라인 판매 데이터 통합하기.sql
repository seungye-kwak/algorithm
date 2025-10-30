-- 코드를 입력하세요
# SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d'), PRODUCT_ID, USER_ID, SALES_AMOUNT
# FROM (
# SELECT SALES_DATE AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
# FROM ONLINE_SALE
# UNION ALL
# SELECT SALES_DATE AS SALES_DATE, PRODUCT_ID, NULL AS user_id, SALES_AMOUNT
# FROM OFFLINE_SALE
# ) AS T
# WHERE DATE_FORMAT(SALES_DATE, '%Y-%m') = '2022-03'
# ORDER BY SALES_DATE, PRODUCT_ID, USER_ID;

select substr(sales_date,1,10) sales_date,
       product_id,
       USER_ID,
       sales_amount
from ONLINE_SALE
where sales_date BETWEEN '2022-03-01' AND '2022-03-31'
union all
select substr(sales_date,1,10) sales_date,
       product_id,
       NULL AS user_id,
       sales_amount
from OFFLINE_SALE
where sales_date like '2022-03%'

order by 1,2,3