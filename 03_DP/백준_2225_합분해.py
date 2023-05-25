"""
날짜 <2023/05/25 (목)>
- 문제 링크: https://www.acmicpc.net/problem/2225
- 문제 요약

- 상상 코딩

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
N,K=map(int,input().split())
dp=[1]*(N+1)
for _ in range(K-1):
    for i in range(1,N+1):
        dp[i]+=dp[i-1]
    print(dp)
print(dp[-1]%1000000000)


