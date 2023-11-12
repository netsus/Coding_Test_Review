"""
날짜 <2023/11/11 (토)>
- 문제 링크: https://www.acmicpc.net/problem/13305
- 문제 요약
    처음 출발할때 기름이 없어서 주유소에서 기름을 넣는다. 거점별 기름값이 다르고, 거점에서 거점사이에 길의 길이도 다르다.
    1km 마다 1리터의 기름을 사용한다.
    도시의 개수 N과 도로의 길이들 N-1개, 주유소 리터당 가격 N개가 주어진다.
    제일 왼쪽 도시에서 제일 오른쪽 도시로 가는 최소 비용 출력
    
- 상상 코딩
    처음 도시에서 처음 길만큼 기름 충전하고, 기름값 저장
    이 기름값보다 싼 곳이 나올 떄까지 이 기름값으로 길을 이동.

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

N = int(input())
loads = list(map(int,input().split()))
prices = list(map(int,input().split()))
result = 0
min_price = prices[0]
for i in range(N-1):
    min_price = min(prices[i],min_price)
    result += min_price * loads[i]
print(result)


