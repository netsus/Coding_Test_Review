"""
날짜 <2023/03/06 (월)>
- 문제 링크: https://www.acmicpc.net/problem/17836
- 문제 요약
    첫 번째 줄에는 성의 크기인 N, M 그리고 공주에게 걸린 저주의 제한 시간인 정수 T가 주어진다.
    첫 줄의 세 개의 수는 띄어쓰기로 구분된다. (3 ≤ N, M ≤ 100, 1 ≤ T ≤ 10000)
    두 번째 줄부터 N+1번째 줄까지 성의 구조를 나타내는 M개의 수가 띄어쓰기로 구분되어 주어진다. 
    0은 빈 공간, 1은 마법의 벽, 2는 그람이 놓여있는 공간을 의미한다. (1,1)과 (N,M)은 0이다.
    용사는 1,1에서 출발, 공주는 N,M에 위치
    용사가 제한 시간 T시간 이내에 공주에게 도달할 수 있다면, 공주에게 도달할 수 있는 최단 시간을 출력한다.
    만약 용사가 공주를 T시간 이내에 구출할 수 없다면, "Fail"을 출력한다.
- 상상 코딩
    vstd에 간 만큼을 저장하며 BFS로 탐색하고 그람 발견시 공주와의 거리 계산해서 gram에 거리 저장
    BFS 탐색하다가, N,M에 도달하면 그때까지간 시간을 result에 저장하고 while 끝
    T이하에 성공한 경우 result와 gram중 최소값 출력, 그 외에는 Fail 출력

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    3.5
- 문제 분석

    - 알고리즘 유형 분석
        BFS를 이용한 그래프 탐색 유형입니다.
    - 시간복잡도 분석
        N행 M열의 그래프를 BFS로 탐색하므로 O(MN)입니다.
    - 리팩토링 방향성
        gram에 대한 예외처리가 복잡하여 result 변수를 따로 두고, gram이 T이하인 경우 result를 갱신하여 마지막에 한 번에 result를 출력할 수 있도록 리팩토링하였습니다.
        
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
import sys
from collections import deque
input = sys.stdin.readline
N,M,T = map(int,input().split())
mat = [[*map(int,input().split())] for _ in range(N)]
vst = [[0 for _ in range(M)] for _ in range(N)]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
result = gram = 1e9
que = deque([(0,0)])
while que:
    r,c = que.popleft()
    if r==N-1 and c==M-1:
        result=vst[r][c]
        break
    for x,y in dirs:
        nr,nc = r+x,c+y
        if 0<=nr<N and 0<=nc<M and mat[nr][nc]!=1 and vst[nr][nc]==0:
            vst[nr][nc]=vst[r][c]+1
            que.append((nr,nc))
            if mat[nr][nc]==2:
                gram=vst[nr][nc]+(N-1-nr)+(M-1-nc)
if gram<=T:
    result = min(result,gram)
print("Fail" if result>T else result)