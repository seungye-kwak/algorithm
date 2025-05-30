-- 코드를 입력하세요
SELECT *
FROM PLACES
WHERE host_id IN (SELECT HOST_ID
                 FROM PLACES
                 GROUP BY host_id
                 HAVING COUNT(*) >= 2)
ORDER BY id