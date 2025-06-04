WITH reviews AS (
    SELECT MEMBER_ID, COUNT(*) AS r_cnt
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
),
review_rank AS (
    SELECT r.member_id, RANK() OVER (ORDER BY r.r_cnt DESC) as rnk
    FROM reviews r
)

SELECT mf.member_name, r.review_text, date_format(r.review_date, '%Y-%m-%d') AS review_date
FROM REST_REVIEW AS r
JOIN MEMBER_PROFILE AS mf
ON r.member_id = mf.member_id
WHERE r.member_id IN (
    SELECT member_id
    FROM review_rank
    WHERE rnk = 1
)
ORDER BY r.review_date, r.review_text;