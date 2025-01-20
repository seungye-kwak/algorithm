SELECT SUM(price) as TOTAL_PRICE
FROM item_info
group by rarity
having rarity = 'LEGEND'