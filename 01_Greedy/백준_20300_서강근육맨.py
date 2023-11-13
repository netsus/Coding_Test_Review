"""
날짜 <2023/11/13 (월)>
- 문제 링크: https://www.acmicpc.net/problem/20300
- 문제 요약
    첫째 줄에 서강헬스클럽에 비치된 운동기구의 개수를 나타내는 정수 (1~10,000)
    둘째 줄에는 각 운동기구의 근손실 정도를 나타내는 정수 (매우큰숫자 1경 이상)
    PT를 한 번 받을 때의 근손실 정도가 M을 넘지 않도록 하고 싶다. 이때, M의 최솟값을 구하라
    PT를 받을 때 운동기구를 최대 2개 사용, 어쩔 수 없으면 1개 사용
    PT를 받을 때마다 이전에 사용하지 않았던 운동기구를 선택
    입력)
    5
    1 2 3 4 5
    출력)
    5
    -> 1-4, 2-3, 5 이렇게 짝지으면 최대의 최솟값이 5이다.
    즉, 2개 씩 더하고, 1개가 남는 경우만 존재 -> 2개씩 더한 값 or 1개의 값중 최대가 최소가 되도록 선택해야 한다.
    2개 혹은 1개로 짝지을때 최대의 최솟값 출력
- 상상 코딩
    짝수일 땐, 최소 최대를 한 묶으로 묶어서 그중 최대값
    홀수일 땐, 최대값 제외하고 나머지를 짝수일때와 같이

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    3.5
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
muscle_losses = sorted(map(int,input().split()))
num = len(muscle_losses)
even = True if num%2==0 else False
result = muscle_losses[-1]
if not even:
    muscle_losses = muscle_losses[:-1]

for i in range(num//2):
    loss = muscle_losses[i] + muscle_losses[-(i+1)]
    result = max(loss,result)
print(result)

# 투포인터 풀이
N = int(input())
muscle_losses = sorted(map(int,input().split()))
result = muscle_losses.pop() if len(muscle_losses)%2==1 else 0
start, end = 0, len(muscle_losses)-1
while start <= end:
    cur_w = muscle_losses[start] + muscle_losses[end]
    result = max(cur_w, result)
    start+=1
    end-=1
print(result)