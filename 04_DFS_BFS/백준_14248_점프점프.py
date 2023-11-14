"""
날짜 <2023/11/14 (화)>
- 문제 링크: https://www.acmicpc.net/problem/14248
- 문제 요약
    돌다리에 숫자 적혀있는 만큼 오니쪽이나 오른쪽으로 점프
    돌다리에서 자기가 방문 가능한 돌들의 개수알고싶다.
    현재 위치가 주어졌을 떄, 방문 가능한 돌들의 개수 출력
- 상상 코딩
    visted를 만들고, 주어진 위치에서 BFS를 이용해 탐색

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    2
- 문제 분석

    - 알고리즘 유형 분석

    - 시간복잡도 분석
        처음에 list로 stone를 만들때 O(N)
        stones를 BFS를 통해 모두 방문할 때 O(N)
        마지막에 sum(visited) 도 O(N)
        총 O(3N) -> 상수항 제거 O(N)

    - 리팩토링 방향성
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
import sys
input = sys.stdin.readline

from collections import deque
N = int(input())
stones = list(map(int,input().split()))
start = int(input())-1
visited = [0]*N
queue = deque([start])
while queue:
    s = queue.popleft()
    if visited[s]==0:
        visited[s]=1
        for nx in (s-stones[s], s+stones[s]):
            if 0<= nx <=N-1:
                queue.append(nx)
print(sum(visited))


