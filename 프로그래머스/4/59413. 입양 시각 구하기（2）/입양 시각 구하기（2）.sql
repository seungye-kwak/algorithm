WITH RECURSIVE hours AS (
    SELECT 0 AS hour
    UNION ALL
    SELECT hour + 1
    FROM hours
    WHERE hour < 23
)

SELECT h.hour,
       IFNULL(COUNT(a.datetime), 0) AS count
FROM hours h
LEFT JOIN ANIMAL_OUTS a
  ON HOUR(a.datetime) = h.hour
GROUP BY h.hour
ORDER BY h.hour;