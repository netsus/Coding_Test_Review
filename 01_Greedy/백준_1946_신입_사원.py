"""
날짜 <2023/11/13 (월)>
- 문제 링크: https://www.acmicpc.net/problem/1946
- 문제 요약
    테스트 케이스별로, 지원자 수가 주어지고 그다음 줄 부터는 N개 줄에 지원자의 서류심사 성적, 면접 성적의 순위가 공백을 두고 주어진다.
    서류심사 성적, 면접 성적 중 적어도 하나가 다른 지원자보다 떨어지면 탈락이다.
    신입사원 최대 인원수 출력
- 상상 코딩
    서류 성적, 면접 성적 순위가 주어지니 이를 튜플의 리스트로 받는다.
    오름 차순 정렬하면 서류 1위, 서류 2위 이런 순으로 정렬될 것이다.
    서류 1위는 붙고 그 면접 순위를 기준으로 그보다 순위가 높은 사람을 한명씩 합격시키는 순으로 한다.

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    2.5
- 문제 분석

    - 알고리즘 유형 분석

    - 시간복잡도 분석

    - 리팩토링 방향성
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    rank = sorted(tuple(map(int,input().split())) for _ in range(N))
    result = 1
    itv_rank = rank[0][1]
    for i in range(1,N):
        if rank[i][1] < itv_rank:
            result += 1
            itv_rank = rank[i][1]
        else:
            break
    print(result)
