-- 문제 설명
-- https://programmers.co.kr/learn/courses/30/lessons/59049

-- CASE 구문 사용
-- CASE WHEN ~ THEN ~ ELSE ~ END 순
-- WHEN 뒤에는 조건절을,
-- THEN 뒤에는 참일 경우,
-- ELSE 뒤에는 거짓일 경우,
-- END로 구문을 닫아줌
SELECT ANIMAL_ID, NAME,
CASE
WHEN SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%'
THEN 'O'
ELSE 'X' END AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC;