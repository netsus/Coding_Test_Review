"""
날짜 <2023/11/14 (화)>
- 문제 링크: https://www.acmicpc.net/problem/2961
- 문제 요약
    재료 N개, 각 재료의 신맛 S와 쓴맛 B
    여러 재료를 이용해서 요리 -> 음식
    음식의 신맛은 재료 신맛의 곱, 쓴맛은 합
    적절히 섞어서 신맛꽈 쓴맛차이를 작게 만들려고 한다.
    재료는 적어도 하나 사용
- 상상 코딩
    각 재료의 신맛과 쓴맛
    재료는 총 10개 -> 1개, 2개, 3개, ... 10개 고를떄까지 신맛을 다 곱하고, 쓴맛을 다 더해서 그 차이를 모두 저장
    모든 재료의 조합으로 요리를 만들고 -> 각 요리에 대해 신맛 쓴맛 차이 구하기
- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    2.5

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

from itertools import combinations
N = int(input())
mats = []
result=1e9
for _ in range(N):
    mat = tuple(map(int,input().split()))
    mats.append(mat)
for i in range(1,N+1):
    cooks = list(combinations(mats,i))
    for cook in cooks:
        S=1;B=0
        for mat in cook:
            S*=mat[0]
            B+=mat[1]
        result=min(result,abs(S-B))
print(result)