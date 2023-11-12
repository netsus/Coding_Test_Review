"""
날짜 <2023/11/13 (월)>
- 문제 링크: https://www.acmicpc.net/problem/2812
- 문제 요약
    N자리 숫자가 주어졌을 때, K개를 지워서 얻을 수 있는 가장 큰수 출력

- 상상 코딩
    스택을 이용해서 수를 넣고, 다음에 넣을 수에 대해 스택의 마지막수보다 넣을 수가 크면 K번 지운다는 것을 횟수를 세가면서
    넣을 수보다 큰 수가 나올때 까지 스택을 pop 한다.
    이렇게 하는 이유는 숫자가 클려면 앞자리 수가 클 수록 숫자는 커지기 때문에
    stack을 이용해서 앞자리수가 크도록 수를 제외하는 것이다.
    만약 수가 내림차순으로 되어있다면, 모두 스택에 들어갈 것이고 하나도 지워지지 않는다.
    이런 경우 앞에서 K개만 출력하면 된다.

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    3
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
N,K = map(int,input().split())
k=K
num = list(input())
stack=[]
for n in num:
    while K>0 and stack and stack[-1] < n:
        stack.pop()
        K-=1
    stack.append(n)
print(''.join(stack[:N-k]))