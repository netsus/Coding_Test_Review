"""
날짜 <2023/11/13 (월)>
- 문제 링크: https://www.acmicpc.net/problem/1912
- 문제 요약
    n개의 정수로 이루어진 임의의 수열. 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합 구하기
- 상상 코딩
    k번쨰 에서 이전까지의 최대합, 그 최대합과 k 번째인 자기자신을 더한값, 그리고 k번째 값
    dp[k]에는 그까지 최대합 vs 자기자신 중 큰값이 저장
    dp의 최대값을 출력

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

n = int(input())
arr = list(map(int,input().split()))
dp = [-1000]*len(arr)
dp[0] = arr[0]
for i in range(1,len(arr)):
    dp[i] = max(dp[i-1]+arr[i], arr[i])
print(max(dp))

