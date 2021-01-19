-- 문제 설명
-- https://programmers.co.kr/learn/courses/30/lessons/59414

-- DATETIME은 DATE_FORMAT 함수를 통해 형 변환을 원하는대로 가능 
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS '날짜'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC;