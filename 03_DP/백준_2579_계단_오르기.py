"""
날짜 <2023/11/14 (화)>
- 문제 링크: https://www.acmicpc.net/problem/2579
- 문제 요약
    이 코드는 계단 오르기 문제를 해결하기 위한 코드입니다. 
    각 계단에는 일정한 점수가 있고, 연속해서 3개의 계단을 밟을 수 없으며, 
    마지막 계단은 반드시 밟아야 하는 조건하에 최대한 많은 점수를 얻는 것이 목표
- 상상 코딩
    전전계단까지 최대값과 현재 계단을 합한것과 전계단값의 최대치를 비교해서 dp table 생성
    dp[k]가 k번째 계단을 밟았을떄의 최대값

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    3
- 문제 분석

    - 알고리즘 유형 분석

    - 시간복잡도 분석
        계단 개수 N에 대해 dp table을 N개에 대해 생성하니 O(N)
    - 리팩토링 방향성
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
import sys
input = sys.stdin.readline
## 리팩토링 풀이
N = int(input())
stairs = [int(input()) for _ in range(N)]
dp=[0]*N
dp[0] = stairs[0]
if N>=2:
    dp[1] = sum(stairs[:2])
if N>=3:
    dp[2] = max(stairs[:2]) + stairs[2]
    for i in range(3,N):
        dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])
print(dp[-1])
exit()
## 첫번째 풀이
N = int(input())
stairs = [int(input()) for _ in range(N)]
dp=[0]*N
dp[0]=stairs[0]
if len(stairs)>=2:
    dp[1]=stairs[0]+stairs[1]
if len(stairs)>=3:
    dp[2]=max(stairs[0]+stairs[2],stairs[1]+stairs[2])
    for i in range(3,N):
        dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])
print(dp[-1])
