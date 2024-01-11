SELECT 
    YEAR(S.SALES_DATE) AS YEAR,
    MONTH(S.SALES_DATE) AS MONTH,
    COUNT(DISTINCT S.USER_ID) AS PURCHASED_USERS,
    ROUND(COUNT(DISTINCT S.USER_ID) / (SELECT COUNT(DISTINCT USER_ID) FROM USER_INFO WHERE YEAR(JOINED) = 2021), 1) AS PURCHASED_RATIO
FROM 
    USER_INFO U
INNER JOIN 
    ONLINE_SALE S ON U.USER_ID = S.USER_ID
WHERE 
    YEAR(U.JOINED) = 2021
    AND U.JOINED <= S.SALES_DATE
GROUP BY 
    YEAR(S.SALES_DATE), 
    MONTH(S.SALES_DATE)
ORDER BY 
    YEAR(S.SALES_DATE), 
    MONTH(S.SALES_DATE);
