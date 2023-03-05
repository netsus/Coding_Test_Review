"""
날짜 <2023/03/05 (일)>
- 문제 링크: https://www.acmicpc.net/problem/7682
- 문제 요약
     3×3 격자판 틱택토
     첫 번째 사람이 X를 놓고 두 번째 사람이 O를 놓는다.
     가로, 세로, 대각선 방향으로 3칸을 잇는 데 성공하면 게임은 즉시 끝난다.
     게임판이 가득 차도 게임은 끝난다.
     게임판의 상태가 주어지면, 그 상태가 틱택토 게임에서 발생할 수 있는 최종 상태인지를 판별

- 상상 코딩
    X를 먼저 두니까, X개수가 O개수와 같거나 1개 큰경우만 성립하는 판이다. 그 외에는 모두 invalid
    이를 통과하면 X개수와 O개수가 같은 경우는 O가 이긴 경우 뿐이다. 이런 경우, 모든 가로, 세로, 대각선을 보면서 3개가 완성된것을 체크하고 그것이 O로 된 1개인 경우만 valid 이다.
    X가 1개 더 많은 경우는 판이 꽉찼거나, X가 이긴 경우이다. 이런 경우도 모든 가로, 세로, 대각선을 보면서 3개가 완성된 문양들을 체크 그것이 X로 된 1개인 경우만 valid
    완성된 문양이 없는 경우 -> 꽉찬 경우라면 valid

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    3

- 문제 분석

    - 알고리즘 유형 분석
        경우의 수를 나누어 틱택토의 모든 판에 대해 3개가 완성되는 경우를 모두 조사하여 valid, invalid를 판단하므로, 브루트포스를 이용한 구현입니다.

    - 시간복잡도 분석
        각 조건문에서  get_winner 부분 외엔 모두 상수시간 입니다.
        get_winner는 8번 반복하며 각 경우에 대해 3번 반복합니다.
        따로 빅오 표기법으론 어렵지만, O(N)에 가깝다고 볼 수 있습니다.

    - 리팩토링 방향성
        x가 이긴 경우와 o가 이긴 경우를 구하는 함수 get_winner를 좀 더 간략하고 파이써닉하게 바꿀 수 있어 보입니다. X가 가로와 대각선, 대각선 2개 겹쳐서 2 빙고로 이긴 경우를 나중에 예외처리해줬는데, 이부분을 설계 초기에 고려하면 좀더 간략한 코드를 짤 수 있을것 같습니다.
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
import sys
from collections import Counter
input = sys.stdin.readline
bingos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
def get_winner(tics):
    x_win=o_win=0
    for bingo in bingos:
        x_cnt=o_cnt=0
        for idx in bingo:
            if tics[idx]=="X":
                x_cnt+=1
            elif tics[idx]=="O":
                o_cnt+=1
        if x_cnt==3:
            x_win+=1
        elif o_cnt==3:
            o_win+=1
    return x_win, o_win

while 1:
    tics = input().rstrip()
    if tics=='end':
        break
    cnts = Counter(tics)
    # print(cnts)
    valid=1
    if not(cnts['X']-1==cnts['O'] or cnts['X']==cnts['O']):
        # print("애초에 invalid")
        valid=0
    elif cnts['X']==cnts['O']:
        # print("X와 O개수 같은 경우")
        x_win,o_win = get_winner(tics)
        if not(o_win==1 and x_win==0):
            valid=0
    elif cnts['X']-1==cnts['O']:
        # print("X가 O보다 1개 많은 경우")
        x_win,o_win = get_winner(tics)
        if x_win==0 and o_win==0 and cnts['.']==0:
            valid=1
        elif (x_win==1 or x_win==2) and o_win==0:
            valid=1
        else:
            valid=0
    print("valid" if valid else "invalid")

            
        






