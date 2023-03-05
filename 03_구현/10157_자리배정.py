"""
날짜 <2023/03/04 (토)>
- 문제 링크: https://www.acmicpc.net/problem/10157
- 문제 요약
    가로로 C개, 세로로 R개의 좌석이 C×R격자형으로 배치
    7×6공연장 -> 6행 7열. 맨 왼쪽 아래부터 위, 오른쪽, 아래, 왼쪽 (시계방향)으로 빙글빙글 찬다
    대기 순서가 K인 관객에게 배정될 좌석 번호 (x,y)를 찾는 프로그램
    해당 대기번호의 관객에게 좌석을 배정할 수 없는 경우에는 0(숫자 영)을 출력
    5 ≤ C, R ≤ 1,000
    1 ≤ K ≤ 100,000,00
- 상상 코딩
    K만큼 반복하며, 
    +R +(0,1), +C +(1,0)
    방향으로 각 분기별로 꺾어서, 이동

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    3.5

- 문제 분석

    - 알고리즘 유형 분석
        주어진 K에 대해 시계방향 달팽이 모양으로 테두리가 채워지는 것을, 따라가며 찾아야 한다. 즉 완전 탐색을 이용한 구현 문제입니다.

    - 시간복잡도 분석
        K를 N이라고 했을 떄, O(N)이지만, 매우 낮은 수준의 N으로 속도를 개선시켰습니다.

    - 리팩토링 방향성
        처음에 for문을 했는데, 시간초과가 나서, 개선을 시켰는데, 알고보니 원인은 C*R보다 K가 큰 경우 예외처리를 안해줘서 그랬습니다. 그래도 for문을 썼을 때 200ms 수준이였는데, 현재 while문으로 개선시킨게 40ms로 매우빨라졌습니다. 블로그의 일반적인 풀이가 600ms수준인 것을 보면 많은 개선을 시켰습니다. 다만, 코드자체가 좀 길어서 mode별로 처리되는 부분을 변수로 나누어 리팩토링할 수 있을 것으로 보입니다.
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
import sys
input = sys.stdin.readline

C, R = map(int,input().split()) # 7 6
K = int(input())
c,r = 2,1
result=[1,0] # C, R
mode=0
if K > C*R:
    print(0)
else:
    while K:
        if mode==0: # R 증가
            if R<K:
                result[1]+=R
                K-=R;R-=1
            else:
                result[1]+=K
                break
            mode=1
        elif mode==1: # C 증가
            if C-1<K:
                result[0]+=C-1
                K-=C-1;C-=1
            else:
                result[0]+=K
                break
            mode=2
        elif mode==2: # R 감소
            if R<K:
                result[1]-=R
                K-=R;R-=1
            else:
                result[1]-=K
                break
            mode=3
        elif mode==3: # C 감소
            if C-1<K:
                result[0]-=C-1
                K-=C-1;C-=1
            else:
                result[0]-=K
                break
            mode=0
    print(*result)