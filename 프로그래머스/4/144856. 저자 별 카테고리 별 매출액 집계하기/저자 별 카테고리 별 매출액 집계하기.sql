-- 코드를 입력하세요
-- 2022년 1월 도서 판매 데이터 기준
-- 저자 별, 카테고리 별 매출액 (Total_sales = 판매량 * 판매가)
-- 저자 ID, 저자명, 카테고리, 매출액 리스트 출력
-- 저자 ID 오름차순 -> 카테고리 내림차순
SELECT A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, SUM(B.PRICE*C.SALES) AS TOTAL_SALES
FROM  BOOK B
  LEFT
  JOIN  AUTHOR A
    ON  A.AUTHOR_ID = B.AUTHOR_ID
  LEFT
  JOIN  BOOK_SALES C 
    ON  B.BOOK_ID = C.BOOK_ID
WHERE SALES_DATE LIKE '2022-01%'
GROUP BY A.AUTHOR_ID, B.CATEGORY
ORDER BY A.AUTHOR_ID ASC, B.CATEGORY DESC
