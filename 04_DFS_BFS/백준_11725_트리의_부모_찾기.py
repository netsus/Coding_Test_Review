"""
날짜 <2023/11/19 (일)>
- 문제 링크: https://www.acmicpc.net/problem/11725
- 문제 요약
    루트 없는 트리가 주어진다.
    트리의 루트 1. 각 노드의 부모를 구하는 프로그램
    노드 개수 N과 트리 상에 연결된 두 정점이 주어진다.
    2번 노드 부터 부모 노드 출력

- 상상 코딩
    그래프를 만들고, BFS로 순회
    1번 노드에서 방문가능한 모든 노드의 부모는 1번
    그 x 노드에서 방문가능한 모든 노드의 부모는 x번임을 이용
    인덱스가 부모고, 값이 자식인 트리를 만든다.
    2번 부터 반복하면서 출력.

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    2.5
- 문제 분석

    - 알고리즘 유형 분석

    - 시간복잡도 분석
        graph 생성하는데 2N, bfs 도는데 2N 총 O(N)

    - 리팩토링 방향성
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
import sys
input = sys.stdin.readline
from collections import defaultdict, deque
graph = defaultdict(list)
N = int(input())
bfs = deque([1])
visited = [0] * (N+1)
visited[1]=1
tree = [0] * (N+1)
for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
while bfs:
    n = bfs.popleft()
    for nx in graph[n]:
        if visited[nx]==0:
            visited[nx]=1
            tree[nx]=n
            bfs.append(nx)
print(*tree[2:],sep='\n')