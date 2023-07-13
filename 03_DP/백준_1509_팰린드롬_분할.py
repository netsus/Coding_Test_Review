"""
날짜 <2023/07/13 (목)>
- 문제 링크: 
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
import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

s = input()
L = len(s)


dp = [2500 for _ in range(L + 1)]
dp[-1] = 0
is_p = [[0 for j in range(L)] for i in range(L)]


for i in range(L):  # 길이 1 짜리 팰린드롬
    is_p[i][i] = 1

for i in range(1, L):  # 길이 2 짜리 팰린드롬 (AA, DD 같은 놈들)
    if s[i - 1] == s[i]:
        is_p[i - 1][i] = 1

for l in range(3, L + 1):  # 길이 3 ~ L 짜리 팰린드롬
    for start in range(L - l + 1):
        end = start + l - 1
        if s[start] == s[end] and is_p[start + 1][end - 1]:
            # 처음과 끝이 같고, 그 사이가 팰린드롬이면
            is_p[start][end] = 1  # start~end 도 팰린드롬

for end in range(L):
    for start in range(end + 1):
        if is_p[start][end]:
            dp[end] = min(dp[end], dp[start - 1] + 1)
        else:
            dp[end] = min(dp[end], dp[end - 1] + 1)

print(dp[L - 1])