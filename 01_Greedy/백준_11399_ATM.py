"""
날짜 <2023/11/13 (월)>
- 문제 링크: https://www.acmicpc.net/problem/11399
- 문제 요약
    N명의 사람들에 대해 N이 주어지고, 각 사람들이 돈을뽑는데 걸리는 시간이 주어집니다.
    줄을 세워서, 각 사람은 앞사람이 돈을 뽑을때까지 기다려야 합니다.
    각 사람이 돈을 인출하는데 필요한 시간의 합이 최소값일떄 출력

- 상상 코딩
    오래걸리는 사람이 앞으로 오면 뒤의 모든 사람들이 그 시간을 기다려야 되기 때문에 전체 시간이 증가합니다.
    그러므로, 빨리끝나는 사람이 앞으로 오게하여 다같이 기다리는 시간을 최소화 하는게 최소값이 됩니다.

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    1.5
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

N = int(input())
times = sorted(map(int,input().split()))
print(sum(sum(times[:i+1]) for i in range(N)))

