"""
날짜 <2023/03/06 (월)>
- 문제 링크: https://www.acmicpc.net/problem/5014
- 문제 요약
    첫째 줄에 F, S, G, U, D가 주어진다. (1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000) 건물은 1층부터 시작하고, 가장 높은 층은 F층
    S에서 G로가는데 엘리베이터에 위로 U만큼, 아래로 D만큼만 이동가능하다. 최소 버튼횟수를 출력하라.
    못가면 use the stairs 반환

- 상상 코딩
    vst를 1~F층까지 1 based로 생성 (디폴트 -1값)
    왜나면 처음 지점을 0으로 해줘야 한다.
    S를 시작으로 BFS 탐색을 하며 G에 도착하면 break
    주어진 점에서 U만큼 위로 간 경우와 D만큼 아래간 경우를 BFS로 탐색하며 간만큼 vst에 갱신
    최종적으로 
    print("use the stairs" if vst[G]==-1 else vst[G])

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    2.5

- 문제 분석

    - 알고리즘 유형 분석
        BFS를 이용한 탐색 유형

    - 시간복잡도 분석
        S에서 G로갈때 전체 층이 F이다.
        BFS의 시간복잡도는 O(V+E)이다. 방문해가며 가기떄문에 시간복잡도는 최악의 경우 O(F)이다.
        F는 최대 100만

    - 리팩토링 방향성
        처음에 자기자신을 방문처리 하지 않아서 계속 틀렸습니다.
        그에 따라 vst를 초기에 -1로 초기화하고 시작점을 0으로 표기하였더니 맞았습니다.    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
import sys
input = sys.stdin.readline
from collections import deque

F,S,G,U,D=map(int,input().split())
vst = [-1]*(F+1)
q=deque([S])
vst[S]=0
while q:
    cur=q.popleft()
    if cur==G:
        break
    for nx in (cur+U,cur-D):
        if 1<=nx<=F and vst[nx]==-1:
            vst[nx] = vst[cur]+1
            q.append(nx)
print("use the stairs" if vst[G]==-1 else vst[G])