"""
날짜 <2023/03/30 (목)>
- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/17679
- 문제 요약

- 상상 코딩
    m행, n열에 대해, 0 ~ m-1, 0 ~ n-1 까지를 돌면서 4개씩 보며 "-"가 아닌 문자중 똑같은게 4개가 반복되면 시작인덱스 기록
    4개짜리 있으면, 시작인덱스에서 4칸을 모두 "-"로 변경
    4개짜리 없으면 종료
    각 열을 반복하며 위에서 아래로 떨어뜨리기 -> "-"를 모두 없앤뒤 앞에다가 채워넣기
    행 리스트 재 생성
    -> 맨 윗줄부터 반복

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    3

- 문제 분석

    - 알고리즘 유형 분석
        브루트포스를 이용한 구현 문제입니다.

    - 시간복잡도 분석
        카드가 전체 N개라고 했을 때, 2x2 빙고 찾을때 O(N), 빙고 처리도 O(N), 행과 열을 바꾸는 것도 O(N)입니다.
        while 문으로 빙고를 반복하니 전체 시간복잡도는 O(N^2)입니다.

    - 리팩토링 방향성
        행과 열을 바꾸는 부분을 zip 을 이요하면 짧고 간단하게 바꿀 수 있습니다.
    
"""

def solution(m, n, board):
    answer=0
    board = [list(r) for r in board]
    while 1:
        bingos=[]
        for c in range(n-1):
            for r in range(m-1):
                four = [board[r+x][c+y] for x,y in [(0,0),(1,0),(0,1),(1,1)]]
                if len(set(four))==1 and four[0] != '-':
                    bingos.append((r,c))
        if len(bingos)==0:
            break
        else:
            for b in bingos:
                for x,y in [(0,0),(1,0),(0,1),(1,1)]:
                    r,c=b[0]+x,b[1]+y
                    if board[r][c] != "-":
                        board[r][c] = "-"
                        answer+=1
            cols=[]                        
            for c in range(n):
                col = [board[r][c] for r in range(m) if board[r][c] != '-']
                col = ["-" for _ in range(m-len(col))] + col
                cols.append(col)
            board=[]
            for r in range(m):
                row = [cols[c][r] for c in range(n)]
                board.append(row)
    return answer


## 리팩토링 풀이
def solution(m, n, board):
    answer=0
    board = [list(r) for r in board]
    while 1:
        bingos=[]
        for c in range(n-1):
            for r in range(m-1):
                four = [board[r+x][c+y] for x,y in [(0,0),(1,0),(0,1),(1,1)]]
                if len(set(four))==1 and four[0] != '-':
                    bingos.append((r,c))
        if len(bingos)==0:
            break
        else:
            for b in bingos:
                for x,y in [(0,0),(1,0),(0,1),(1,1)]:
                    r,c=b[0]+x,b[1]+y
                    if board[r][c] != "-":
                        board[r][c] = "-"
                        answer+=1
            cols=[]                        
            for c in range(n):
                col = [board[r][c] for r in range(m) if board[r][c] != '-']
                col = ["-" for _ in range(m-len(col))] + col
                cols.append(col)
            board = list(map(list,zip(*cols)))
    return answer


m,n,board = 4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"] #    14
print(solution(m, n, board))
m,n,board = 6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"] #	15
print(solution(m, n, board))