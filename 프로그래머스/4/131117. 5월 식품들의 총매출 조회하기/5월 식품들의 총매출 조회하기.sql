-- 코드를 입력하세요
SELECT A.product_id,
        B.product_name,
        sum(A.amount * B.price) AS TOTAL_SALES
FROM FOOD_ORDER as A LEFT JOIN FOOD_PRODUCT as B
ON A.product_id = B.product_id
WHERE DATE_FORMAT(A.produce_date, '%Y-%m') = '2022-05'
GROUP BY a.PRODUCT_ID, b.PRODUCT_NAME
ORDER BY TOTAL_SALES DESC, a.PRODUCT_ID