-- 코드를 입력하세요
SELECT history_id, car_id, DATE_FORMAT(start_date, '%Y-%m-%d') as START_DATE, 
        DATE_FORMAT(end_date, '%Y-%m-%d') AS END_DATE,
        CASE 
            WHEN DATEDIFF(end_date, start_date) >= 29 THEN '장기 대여'
            ELSE '단기 대여'
            END AS RENT_TYPE
FROM car_rental_company_rental_history
WHERE DATE_FORMAT(start_date, '%Y-%m') = '2022-09'
ORDER BY history_id DESC;

