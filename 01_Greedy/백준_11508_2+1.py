"""
날짜 <2023/11/12 (일)>
- 문제 링크: https://www.acmicpc.net/problem/11508
- 문제 요약
    유제품 수와, 그 가격들이 주어진다.
    유제품 3개를 한번에 사면, 가장 싼것은 무료로 주는 2+1 행사를 할때, 최소비용으로 유제품을 구입하는 그 비용을 출력해야합니다.

- 상상 코딩
    가격을 내림차순으로 정렬.
    앞에서부터 3개씩 짤라서 2개의 가격만 더하기
    마지막에 3개로 안묶이고 남은 유제품들의 가격은 모두 더하기
    앞에서부터 3개씩 자르는 이유는 그렇게 해야 그나마 가장 비싼 유제품들을 무료로 할인받아 살 수 있기 때문입니다.
    그렇게 할인율이 높다는 것은 가장 할인을 많이 받는 것을 의미하며, 최소 비용을 의미하게되기 때문입니다.

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    2
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
prices = sorted([int(input()) for _ in range(N)], reverse=True)
result=sum(prices)
for i in range(2,N,3):
    result -= prices[i]
print(result)


## 또 다른 풀이
N = int(input())
prices = sorted([int(input()) for _ in range(N)], reverse=True)
print(sum(prices) - sum(prices[2::3]))