"""
날짜 <2023/11/12 (일)>
- 문제 링크: https://www.acmicpc.net/problem/2217
- 문제 요약
    N개의 로프가 있고, 로프마다 들 수 있는 중량이 서로 다르다.
    여러 로프를 병렬로 연결하면 로프에 중량을 나눌 수 있다. 
    로프들에 대한 정보가 주어졌을 때, 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구하는 프로그램
    
- 상상 코딩
    로프가 견디는 중량의 최솟값부터 하나씩 올라가면서, N개, N-1개, ... 해서 그중 최대값 출력

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    1

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
ropes = sorted([int(input()) for _ in range(N)])
result=0
for i in range(N):
    num = N-i
    w = ropes[i]*num
    result = max(w,result)
print(result)
