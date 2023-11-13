"""
날짜 <2023/11/13 (월)>
- 문제 링크: https://www.acmicpc.net/problem/2606
- 문제 요약
    네트워크 상에 컴퓨터들이 연결되어 있습니다.
    1번 컴퓨터를 통해 원 바이러스가 전파될때 바이러스에 걸리게 되는 컴퓨터 수를 출력하시오.
    컴퓨터 수가 주어지고, 연결된 수가 주어진다.
    연결수만큼 A컴퓨터에서 B컴퓨터로 연결된것이 주어집니다.

- 상상 코딩
    그래프를 이중 리스트로 표현
    1번 인덱스가 1번 노드. 1번 인덱스의 리스트가 1번 노드에 연결된 노드들의 리스트
    visted를 만들고, dfs를 통해 1번 노드부터 visted가 아닌 노드를 방문하며 바이러스에 걸리는 컴퓨터수 카운팅

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    2.5
- 문제 분석

    - 알고리즘 유형 분석

    - 시간복잡도 분석
        그래프의 edge만큼 반복하여 입력받고, node 개수만큼 반복하며 dfs를 순회하기 때문에
        DFS는 각 노드를 한번씩 방문하고, 각 간선을 한번씩 검사하기 때문에 O(n+e)이다.

    - 리팩토링 방향성
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
import sys
input = sys.stdin.readline

## defaultdict를 사용한 풀이
from collections import defaultdict
n = int(input())
e = int(input())
graph = defaultdict(list)
vsted = [0]*(n+1)
for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
result=0
def dfs(node):
    global result
    if vsted[node]==0:
        vsted[node] = 1
        result += 1
        for nx in graph[node]:
            dfs(nx)
dfs(1)
print(result-1)


# # 기본 풀이
# n = int(input())
# e = int(input())
# graph = [[] for _ in range(n+1)]
# vsted = [0]*(n+1)
# for _ in range(e):
#     a,b = map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# result=0
# def dfs(node):
#     global result
#     if vsted[node] == 0:
#         vsted[node] = 1
#         result += 1
#         for n in graph[node]:
#             dfs(n)
# dfs(1)
# print(result-1)
