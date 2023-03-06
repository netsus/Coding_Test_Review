"""
날짜 <2023/03/06 (월)>
- 문제 링크: https://www.acmicpc.net/problem/1743
- 문제 요약
    첫째 줄에 통로의 세로 길이 N(1 ≤ N ≤ 100)과 가로 길이 M(1 ≤ M ≤ 100) 그리고 음식물 쓰레기의 개수 K(1 ≤ K ≤ NxM)이 주어진다.  그리고 다음 K개의 줄에 음식물이 떨어진 좌표 (r, c)가 주어진다.
    좌표 (r, c)의 r은 위에서부터, c는 왼쪽에서부터가 기준이다. 입력으로 주어지는 좌표는 중복되지 않는다.
    음식물이 서로 상하좌우로 연결되어있으면 붙어서 덩어리가 된다.
    가장 큰 덩어리에 포함된 음식물의 개수는?
- 상상 코딩
    NxM 0으로된 매트릭스를 만들고 음식물이 있는 r,c를 1로 채웁니다.
    같은 크기의 visted 매트릭스를 만들고, 음식물 리스트를 반복하며
    방문하지 않은 경우 BFS로 방문하며 상하좌우로 음식물이 있는 경우만 방문하며 크기를 계산합니다.
    끝나면 최대 크기를 max로 갱신합니다.

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    2
- 문제 분석

    - 알고리즘 유형 분석
        그래프 탐색(BFS나 DFS 모두 가능)을 이용해야하는 유형입니다.

    - 시간복잡도 분석
        N행 M열에 대해, 각 food 별로 탐색을 하니, 최악의 경우 O(NM)시간 만큼 쓰입니다.
        그러므로, 전체 시간복잡도 역시 O(NM)입니다.

    - 리팩토링 방향성
        BFS 부분을 더 간결하게 할 수 있을 것 같은데, 따로 보이지 않습니다.
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
import sys
from collections import deque
input = sys.stdin.readline
N,M,K = map(int,input().split())
foods = [tuple(map(int,input().split())) for _ in range(K)]
mat = [[0 for _ in range(M+1)] for _ in range(N+1)]
vst = [[0 for _ in range(M+1)] for _ in range(N+1)]
for r,c in foods:
    mat[r][c]=1
dirs=[(-1,0),(1,0),(0,-1),(0,1)] # 상,하,좌,우
result=0
for r,c in foods:
    if vst[r][c]==0:
        q = deque([(r,c)])
        food_size=1
        vst[r][c]=1
        while q:
            r,c = q.popleft()
            for x,y in dirs:
                nr,nc=r+x,c+y
                if 0<nr<=N and 0<nc<=M and mat[nr][nc]==1 and vst[nr][nc]==0:
                    food_size+=1
                    vst[nr][nc]=1
                    q.append((nr,nc))
        result = max(result,food_size)
print(result)

    


