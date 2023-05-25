"""
날짜 <2023/05/11 (목)>
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
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
left=[];right=[]
for i in arr:
    if len(left)==len(right):
        heappush(left,-i)
    else:
        heappush(right,i)
    if right and right[0] < -left[0]:
        l_value = -heappop(left)
        r_value = -heappop(right)
        heappush(left,r_value)
        heappush(right,l_value)
    print(-left[0])


    





