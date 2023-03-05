"""
날짜 <2023/03/05 (일)>
- 문제 링크: https://www.acmicpc.net/problem/21608
- 문제 요약
    NxN 개의 책상 존재. 각 자리에 학생이 앉을 때, 학생 별로 좋아하는 4명의 학생 리스트를 입력받습니다.
    인접하다의 의미: 상,하,좌,우
    1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다
    위 3가지 규칙을 만족하도록 학생을 앉히고, 모두 앉힌 다음, 학생별로 인접한 학생(상,하,좌,우)중 좋아하는 학생 명수에 따라 그 값이 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000.
    만족도의 총합을 구해야 합니다.

- 상상 코딩
    각 학생 별로, 모든 칸을 돌며 칸 별로, (좋아하는 학생수, 빈칸 수)를 구해서, 
    좋아하는 학생수가 크거나, 좋아하는 학생수가 같은데 빈칸수가 많은 경우를 구해 자리 배치
    자리배치 후 각 학생별로 상,하,좌,우에 좋아하는 학생 명수 계산하고 만족도 총합 구하기

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    3.5 (예외처리가 빡셈)
- 문제 분석

    - 알고리즘 유형 분석
        각 학생별로, 모든 자리에 대해 선호도를 계산해서 앉히고, 앉은 자리에 대해 선호도 점수를 계산합니다.
        즉, 브루트포스를 이용한 구현입니다.

    - 시간복잡도 분석
        학생 명수를 N(코드에선 N**2)이라고 하겠습니다.
        학생별로 모든 칸을 반복합니다. O(N^2)
        또, 학생별로 선호도 점수 계산 O(N)
        즉, 전체 시간복잡도는 O(N^2)입니다.

    - 리팩토링 방향성
        상하좌우에 빈칸도 없고, 좋아하는 학생도 없는 경우가 여러개라면 앞에있는 책상으로 배정하기 위해
        preferest에 0.5를 넣었습니다. 이 부분을 따로 예외처리 하지 않고, 자연스럽게 예외처리되도록 리팩토링 해보는 방향성이 있을 것 같습니다. 
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
import sys
from collections import defaultdict
input = sys.stdin.readline
N=int(input())
student_dict = defaultdict(list)
student_sits = defaultdict(list)
dirs = [(-1,0),(1,0),(0,-1),(0,1)] # 상, 하, 좌, 우
result=0

for _ in range(N*N):
    students = [*map(int,input().split())]
    student_dict[students[0]] = students[1:]
mat = [[0 for _ in range(N)] for _ in range(N)]
# 자리 배정
for student,likes in student_dict.items():
    preferest=0;pick=[]
    for r in range(N):
        for c in range(N):
            if mat[r][c]==0:
                prefer=0
                for d in dirs:
                    nr=r+d[0];nc=c+d[1]
                    if 0<=nr<N and 0<=nc<N:
                        if mat[nr][nc]==0:
                            prefer+=1
                        elif mat[nr][nc] in likes:
                            prefer+=10
                if preferest < prefer:
                    preferest=prefer
                    pick=[r,c]
                elif preferest==0 and len(pick)==0:
                    pick=[r,c]
                    # 상하좌우에 빈칸도 없고, 좋아하는 학생도 없는 경우가 여러개라면 앞에있는 책상으로
                    preferest=0.5 
    mat[pick[0]][pick[1]] = student
    student_sits[student] = pick

for student,likes in student_dict.items():
    like_cnt=0
    r,c = student_sits[student]
    for d in dirs:
        nr=r+d[0];nc=c+d[1]
        if 0<=nr<N and 0<=nc<N and mat[nr][nc] in likes:
            like_cnt+=1
    result += 10**(like_cnt-1) if like_cnt else 0
print(result)

            




