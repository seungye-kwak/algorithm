-- 코드를 입력하세요
SET @hour := -1;
SELECT @hour := @hour + 1 AS hour,
    (SELECT COUNT(*)
    FROM animal_outs
    WHERE HOUR(datetime) = @hour) AS count
FROM animal_outs
WHERE @hour < 23
ORDER BY hour;