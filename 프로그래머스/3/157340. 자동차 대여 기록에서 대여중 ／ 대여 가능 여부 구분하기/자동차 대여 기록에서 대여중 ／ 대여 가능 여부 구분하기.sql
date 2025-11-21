-- 코드를 입력하세요
# SELECT CAR_ID, (CASE WHEN CAR_ID IN (
#                                     SELECT CAR_ID
#                                     FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
#                                     WHERE '2022-10-16' BETWEEN START_DATE AND END_DATE)
#                THEN '대여중'
#                ELSE '대여 가능'
#                END) AVAILABILITY
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# GROUP BY CAR_ID
# ORDER BY CAR_ID DESC;

SELECT
    CAR_ID,
    CASE
        WHEN MAX(START_DATE <= DATE('2022-10-16') AND END_DATE >= DATE('2022-10-16')) = 1
             THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;