"""
날짜 <2023/06/22 (목)>
- 문제 링크: https://www.acmicpc.net/problem/10986
- 문제 요약
    N개로 이루어진 배열과 M이 주어지면, 배열에서 M으로 나누어 떨어지는 구간의 개수를 출력

- 상상 코딩
    누적합 구간을 구하고,
    나머지가 같은 구간을 빼서 나머지가 0인 구간을 만들어야 한다.

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

N,M = map(int, input().split())
nums = map(int, input().split())
nsum, remainders = 0, [0]*M
for num in nums:
    nsum += num
    remainders[nsum % M] += 1
result = remainders[0]
for n in remainders:
    result += n*(n-1)//2
print(result)





