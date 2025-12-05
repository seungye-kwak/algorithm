-- 코드를 입력하세요
SELECT history_id, car_id, 
        DATE_FORMAT(start_date, '%Y-%m-%d') as START_DATE, 
        DATE_FORMAT(end_date, '%Y-%m-%d') AS END_DATE,
        CASE 
            WHEN DATEDIFF(end_date, start_date) >= 29 THEN '장기 대여'
            ELSE '단기 대여'
            END AS RENT_TYPE
FROM car_rental_company_rental_history
WHERE DATE_FORMAT(start_date, '%Y-%m') = '2022-09'
ORDER BY history_id DESC;

# SELECT HISTORY_ID, CAR_ID, 
#        date_format(START_DATE,"%Y-%m-%d") START_DATE, 
#        date_format(END_DATE, "%Y-%m-%d") END_DATE,
#        case when (end_date - start_date) >= 29 then "장기 대여"
#        else "단기 대여" end RENT_TYPE
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY
# where START_DATE like "2022-09%"
# order by 1 desc