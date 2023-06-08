"""
날짜 <2023/06/01 (목)>
- 문제 링크: https://www.acmicpc.net/problem/9663
- 문제 요약

- 상상 코딩
    특정 행,열에 퀸을 둠으로써 두지 못하는 곳에 대해
    행과 열은 못두는걸 블락할 수 있는데, 대각선에 두지 못하게 하는 부분은 어떻게 해야하지?
    2차원 배열을 만들어 두지 못하는 곳을 모두 마킹하는 방법이 있고,
    퀸을 둔 행과 열만 저장하여 그 퀸들로 인해 두지 못하는 곳을 그때 그때 계산하는 방법이 있다.
    근데, 퀸을 바꿔가며 두어야 하기 때문에 두 번째 방법이 좀 더 신빙성 있다. 백트래킹으로 계산이 쉽기 때문
    대각선 계산법과 함께 N개를 두는 경우일 때마다 +1
    이중 포문으로 시작 퀸 지정 각 퀸에 대하선 오른쪽, 아래로만 탐색해도 된다.

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)

- 문제 분석

    - 알고리즘 유형 분석

    - 시간복잡도 분석

    - 리팩토링 방향성
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
N=int(input())
queens = []
diagonal=[(-1,-1),(1,-1),(1,1),(-1,1)]
cnt=0
print(N)
def chess(n):
    global cnt
    for r in range(N):
        for c in range(N):
            allow=True
            for (y,x) in queens:
                if r!=y and c!=x:
                    for dx,dy in diagonal:
                        while 1:
                            x,y=x+dx,y+dy
                            if not(0<=x<N and 0<=y<N):
                                break
                            if x==c and y==r:
                                allow=False
                                break
                        if not allow:
                            break
                    if not allow:
                        break    
                else:
                    allow=False
                    print(">>>>>>>")
            if allow:
                print(r,c,n)
                if n==N-1:
                    cnt+=1
                    continue
                else:
                    queens.append((r,c))
                    print(queens)
                    chess(n+1)
    if 0<n<N-1:
        queens.pop()
        chess(n-1)
chess(0)
                





        



