-- 문제 설명
-- https://programmers.co.kr/learn/courses/30/lessons/59045

SELECT INS.ANIMAL_ID, INS.ANIMAL_TYPE, INS.NAME
FROM ANIMAL_INS AS INS
INNER JOIN ANIMAL_OUTS AS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.SEX_UPON_INTAKE LIKE 'Intact%' 
AND OUTS.SEX_UPON_OUTCOME NOT LIKE 'Intact%'
ORDER BY INS.ANIMAL_ID ASC;

-- 특정 문자가 포함된 데이터를 검색할 때는 LIKE
-- 'A'로 시작하는 모든 값 조회 -> LIKE 'A%'
-- 'B'로 끝나는 모든 값 조회 -> LIKE '%B'
-- 'C'가 들어가는 모든 값 조회 -> LIKE '%C%'
-- 'D' + 외글자인 모든 값 조회 -> LIKE 'D?'