"""
날짜 <2023/03/04 (토)>
- 문제 링크: 
- 문제 요약
    첫 번째 줄에는 2차원 세계의 세로 길이 H과 2차원 세계의 가로 길이 W가 주어진다. (1 ≤ H, W ≤ 500)
    두 번째 줄에는 블록이 쌓인 높이를 의미하는 0이상 H이하의 정수가 W개 주어진다.
    2차원 세계에서는 한 칸의 용량은 1이다. 고이는 빗물의 총량을 출력하여라.
    빗물이 전혀 고이지 않을 경우 0을 출력하여라.
    왼쪽, 오른쪽 끝에 벽은 없다.
- 상상 코딩
    각 블록에 대해 왼쪽에 있는 블록중 최대값, 오른쪽에 있는 블록중 최대값을 계산
    둘중 최소값이 해당 블록보다 크다면, 그 값에서 현재 블록을 뺀 값이 현재 블록에 물이 고이는 양이다.

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    3

- 문제 분석

    - 알고리즘 유형 분석
        각 블록에 대해 왼쪽의 최대 블록과 오른쪽의 최대 블록중 최소값에 대해 각 블록을 계산.
        즉, 구현인데, 그리디에 가까운 구현으로 보입니다.

    - 시간복잡도 분석
        blocks를 왼쪽, 오른쪽으로 반복할 때 가각 O(N)이고,
        W를 반복하며 각 블록에 대해 빗물 계산 역시 O(N)
        그러므로, 전체 시간복잡도 역시 O(N) 입니다.

    - 리팩토링 방향성
        딱히 보이지 않습니다.
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
import sys
input = sys.stdin.readline

H,W = map(int,input().split())
blocks = [*map(int,input().split())]
if W<3: # W가 3이상이여야 물이 쌓일 수 있다.
    print(0)
result = rmax = lmax = 0
lmaxs=[];rmaxs=[]
for block in blocks:
    lmax = max(lmax,block)
    lmaxs+=[lmax]
for block in blocks[::-1]:
    rmax = max(rmax,block)
    rmaxs += [rmax]
for i in range(W):
    cap=min(lmaxs[i], rmaxs[W-1-i])
    cur=blocks[i]
    if cap > cur:
        result += cap-cur
print(result)

        
        




