"""
날짜 <2023/11/13 (월)>
- 문제 링크: https://www.acmicpc.net/problem/2503
- 문제 요약
    1에서9 서로 다른 숫자 3개 스트라이크와 볼
    주어진 숫자 야구 게임 과정을 보고, 정답의 가능성의 총 개수 출력

- 상상 코딩
    질문 개수 N개가 주어지고, 스트라이크와 볼 여부가 주어진다.
    처음에 1~9로 만들어질 수 있는 모든 숫자 리스트를 가지고 스트라이크와 볼 여부에 따라 필터링해가는 방식으로 진행
    1 스트라이크면 3자리중 1자리라도 일치하는 애들만 남기고 필터링
    1 볼이면 숫자 하나라도 포함되면 남기고 필터링

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)

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

from itertools import permutations
N = int(input())
cases = list(permutations(range(1,10),3))
for _ in range(N):
    after_cases = []
    num,st,ba = input().split()
    for case in cases:
        strike=0
        ball=0
        for i in range(3):
            if int(num[i])==case[i]:
                strike += 1
            elif int(num[i]) in case:
                ball += 1
        if int(st)==strike and int(ba)==ball:
            after_cases.append(case)
    cases = after_cases.copy()
print(len(cases))


