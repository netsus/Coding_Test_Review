/*
날짜 <2023/11/12 (일)>
- 문제 링크: https://www.acmicpc.net/problem/20115
- 문제 요약
    가장 먼저 들어온 동물의 이름 1개 출력
- 상상 코딩
    datetime순으로 오름차순하여 가장 먼저 들어온 동물순으로 출력하되 limit 1을 하여 1개의 행만 출력

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    1
*/
SELECT name
FROM animal_ins
ORDER BY datetime ASC
LIMIT 1;