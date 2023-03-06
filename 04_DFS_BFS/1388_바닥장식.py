"""
날짜 <2023/03/06 (월)>
- 문제 링크: https://www.acmicpc.net/problem/1388
- 문제 요약
    세로 크기N과 가로 크기 M
    둘째 줄부터 N개의 줄에 M개의 문자가 주어진다. 이것은 바닥 장식 모양이고, '-‘와 ’|‘로만 이루어져 있다. N과 M은 50 이하인 자연수
    가로로 연속된 -는 하나의 바닥 장식이고, 세로로 연속된 | 역시 하나의 바닥장식이다.
    바닥장식의 개수를 구하라.

- 상상 코딩
    스택을 사용하여 행별로 가로만 보는 for문으로, 각 행의 "-"로 이루어진 바닥 장식 개수를 구합니다.
        -가 있으면 스택에 넣고, |가 있으면 pop하며 바닥 장식 개수 +=1 하고 마지막에 스택에 -가 있으면 1을 더해줍니다.
    마찬가지로 열 별로 세로만 보는 for문으로 각 열의 "|"로 이루어진 바닥 장식 개수를 구합니다.
    이를 합칩니다.

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    3

- 문제 분석

    - 알고리즘 유형 분석
        가로와 세로를 각각 for문으로 반복하며 이어진 바닥 장식을 찾는 문제입니다. 완전 탐색 유형으로 보입니다.
        이를 그래프 탐색으로 풀수도 있어서 그래프 탐색 유형으로 적혀있습니다.

    - 시간복잡도 분석
        행은 N개, 열은 M개 입니다. 각 행을 반복하며 행에 대해 replace와 split을 했습니다. 각각 O(M)입니다.
        즉, 행을 반복하며 "-"로 된 블록 개수 세는데 O(MN) 시간복잡도가 쓰입니다.
        다음으로 열을 반복하며 join과 replace, split이 쓰입니다. 모두 O(N)입니다. 
        즉, 열을 반복하며 "|"로 된 블록 개수를 세는데 O(NM) 시간복잡도가 쓰입니다. (join연산이 더있으므로 행보단 오래걸립니다.)
        전체 시간복잡도 역시 O(MN)입니다.

    - 리팩토링 방향성
        각 열에 대해 따로 반복문을 돌렸는데, zip(*tiles)를 통해 각 열도 반복할 수 있습니다. 이를 이용하면 코드가 좀 더 간결해집니다.
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
tiles = [input().rstrip() for _ in range(N)]
result = sum(len(row.replace('|',' ').split()) for row in tiles)
result += sum(len("".join(col).replace("-",' ').split()) for col in zip(*tiles))
print(result)


## 숏코딩
T=[input()for _ in range(int(input().split()[0]))]
print(sum(len(R.replace('|',' ').split())for R in T)+sum(len("".join(C).replace("-",' ').split()) for C in zip(*T)))


