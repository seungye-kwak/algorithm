-- 코드를 입력하세요
SELECT I.animal_id, I.animal_type, I.name
FROM (SELECT ANIMAL_ID, ANIMAL_TYPE, NAME
     FROM ANIMAL_INS
     WHERE sex_upon_intake NOT LIKE 'Spayed%' 
     AND sex_upon_intake NOT LIKE 'Neutered%') I
JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.SEX_UPON_OUTCOME LIKE 'Spayed%' or
O.SEX_UPON_OUTCOME LIKE 'Neutered%'
ORDER BY I.ANIMAL_ID