"""
날짜 <2023/03/06 (월)>
- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43162
- 문제 요약
    그래프를 인접행렬 모양으로 줬을 때, 연결 성분의 개수를 구하라

- 상상 코딩
    그래프를 defaultdict(list) 형태로 변환하고, DFS를 이용해서 한번 돌때 마다 연결 성분 +=1 하기

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    2
- 문제 분석

    - 알고리즘 유형 분석
        DFS를 이용한 연결 성분 개수 확인
    - 시간복잡도 분석
        그래프 생성할때 컴퓨터별로 연결된 컴퓨터개수로 생성 O(N**2)
        각 컴퓨터 별로 DFS O(V+E) 정점과 엣지 개수 인데, 여기선 최악의 경우 모든 컴퓨터에 모든게 연결된 경우
        O(N**2)

    - 리팩토링 방향성
        vst를 인자로 전달하고 반환했는데, solution 내부에서 dfs를 정의하면 그렇게할 필요가 없습니다.

    
"""

n1,c1 = 3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]] # 2
n2,c2 = 3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]] # 1

from collections import defaultdict

def dfs(c,graph,vst):
    if vst[c]==0:
        vst[c]=1
        for nc in graph[c]:
            vst = dfs(nc,graph,vst)
    return vst


def solution(n,computers):
    answer=0
    graph = defaultdict(list)
    vst = [0]*n 
    for i,cons in enumerate(computers):
        for j,con in enumerate(cons):
            if con==1 and i!=j:
                graph[i]+=[j]
    for c in range(n):
        if vst[c]==0:
            vst = dfs(c,graph,vst)
            answer+=1
    return answer


## 리팩토링 풀이
from collections import defaultdict
def solution(n,computers):
    answer=0
    graph = defaultdict(list)
    vst = [0]*n 
    for i,cons in enumerate(computers):
        for j,con in enumerate(cons):
            if con==1 and i!=j:
                graph[i]+=[j]
    def dfs(c,graph):
        vst[c]=1
        for nc in graph[c]:
            if vst[nc]==0:
                dfs(nc,graph)
    for c in range(n):
        if vst[c]==0:
            dfs(c,graph)
            answer+=1
    return answer


# 기존 풀이 - 제일 깔끔
def solution(n, computers):
    visited=[0]*n
    answer=0
    def dfs(pc): # dfs로 연결된 부분 쭉 탐색
        visited[pc]=1
        for idx,c in enumerate(computers[pc]):
            if c and visited[idx]==0:
                dfs(idx)
                
    for pc in range(n):
        if visited[pc] == 0:
            dfs(pc)
            answer+=1
    return answer

print(solution(n2,c2))
        


