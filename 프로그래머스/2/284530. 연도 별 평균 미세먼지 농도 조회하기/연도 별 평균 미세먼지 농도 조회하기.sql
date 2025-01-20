SELECT YEAR(YM) as year, 
        ROUND(AVG(pm_val1),2) as 'pm10', 
        ROUND(AVG(pm_val2),2) as 'PM2.5'
FROM AIR_POLLUTION
WHERE LOCATION2 = '수원'
GROUP BY YEAR(ym)
ORDER BY YEAR(ym);

