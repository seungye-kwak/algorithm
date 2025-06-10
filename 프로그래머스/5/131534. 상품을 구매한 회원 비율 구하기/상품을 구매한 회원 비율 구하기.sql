-- 전체 가입 회원 수
WITH joined_users AS (
    SELECT DISTINCT user_id
    FROM user_info
    WHERE YEAR(joined) = 2021
)

SELECT YEAR(sales_date) AS year, MONTH(sales_date) AS month,
        COUNT(DISTINCT user_id) AS purchased_users,
        ROUND(COUNT(DISTINCT user_id) / (SELECT COUNT(user_id) FROM joined_users),1) AS purchased_rate
FROM online_sale
WHERE user_id IN (SELECT user_id
                 FROM joined_users)
GROUP BY YEAR(sales_date), MONTH(sales_date)
ORDER BY year, month