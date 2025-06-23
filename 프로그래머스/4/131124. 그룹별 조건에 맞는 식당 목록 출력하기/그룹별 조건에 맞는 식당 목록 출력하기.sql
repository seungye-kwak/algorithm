WITH review_cnt AS (
    SELECT member_id, count(*) as cnt
    FROM REST_REVIEW
    GROUP BY 1
),
max_member AS (
    SELECT member_id
    FROM review_cnt
    WHERE cnt = (SELECT MAX(cnt) FROM review_cnt)
)

SELECT mf.member_name, r.review_text, date_format(r.review_date, '%Y-%m-%d')
FROM max_member m JOIN rest_review r
ON m.member_id = r.member_id
JOIN member_profile AS mf ON m.member_id = mf.member_id
ORDER BY 3, 2