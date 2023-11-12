"""
날짜 <2023/11/13 (월)>
- 문제 링크: https://www.acmicpc.net/problem/1758
- 문제 요약
    손님들이 순서대로 들어오며 팁을 주는데, 원래 주려던 팁에서 (받은 등수 - 1) 만큼이 차감된다.
    사람수 N과 N명이 주려던 팁이 있을 때, 적절히 줄을 세워 팁의 최댓값을 출력.

- 상상 코딩
    팁이 적은 사람이 마이너스를 크게 받아서 0원이 되는게 팁의 최댓값을 늘리는 방향이다.
    팁으로 내림차순하여 줄을 세우면, 팁이 적은 사람이 자연스럽게 차감이 많이 되어 최댓값은 늘어날 것이다.

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    1.5

- 문제 분석

    - 알고리즘 유형 분석

    - 시간복잡도 분석

    - 리팩토링 방향성
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
import sys
input = sys.stdin.readline
N = int(input())
tips = sorted(int(input()) for _ in range(N))[::-1]
result = sum(max(tips[i]-i,0) for i in range(N))
print(result)


