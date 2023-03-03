"""
날짜 <2023/03/03 (금)>
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
- 상상 코딩
    홀수면 가장 큰 수 제외하고, 최소-최대 짝짓기
    짝수면, 바로 최소-최대 짝짓기
    정렬하고, 투포인터 사용? 
- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    1.5

- 문제 분석

    - 알고리즘 유형 분석
        주어진 순간에 근손실이 최대한 적게나는 최적의 선택을 해야하기 때문에 그리디 알고리즘 입니다.
        또한, 투포인터를 사용하였습니다.

    - 시간복잡도 분석
        초기에 주어진 N개에 대해 정렬을 하여 O(NlogN)이 사용되었고,
        max값을 찾는데 O(1), 투포인터로 while문 도는 것도 내부는 상수시간 이므로 O(N)
        정렬이 가장 오래걸려 전체 시간복잡도는 O(NlogN) 입니다.

    - 리팩토링 방향성
        weight_loses가 홀수일 때 조건문에서 굳이 max를 안해도 될 것 같습니다.
        삼항 연산자로 line 47~49을 아래처럼 고칠 수 있을 것 같습니다.
        result = weight_loses.pop() if len(weight_loses)%2==1 else 0
        -> 고친 결과 맞았습니다.
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
N=int(input())
weight_loses=sorted(map(int,input().split())) # O(NlogN)
# result=0
# if len(weight_loses)%2==1:
#     result=max(result,weight_loses.pop()) # O(N)
result = weight_loses.pop() if len(weight_loses)%2==1 else 0
start,end=0,len(weight_loses)-1
while start <= end:
    cur_weight = weight_loses[start] + weight_loses[end]
    result = max(cur_weight, result)
    start+=1;end-=1
print(result)