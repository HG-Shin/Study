SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH,
       GENDER, COUNT(DISTINCT(USER_ID)) AS USERS
FROM USER_INFO JOIN ONLINE_SALE USING(USER_ID)
WHERE GENDER IS NOT NULL
GROUP BY YEAR(SALES_DATE), MONTH(SALES_DATE), GENDER
ORDER BY YEAR(SALES_DATE), MONTH(SALES_DATE), GENDER