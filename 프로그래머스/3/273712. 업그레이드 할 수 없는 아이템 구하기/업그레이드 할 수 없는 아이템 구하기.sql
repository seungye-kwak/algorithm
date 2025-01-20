SELECT item_id, item_name, rarity
FROM ITEM_INFO
WHERE ITEM_ID NOT IN
    (SELECT distinct parent_item_id
    FROM item_tree
    WHERE parent_item_id IS NOT NULL)
ORDER BY ITEM_ID DESC;



