"""
날짜 <2023/11/14 (화)>
- 문제 링크: https://www.acmicpc.net/problem/1461
- 문제 요약
    세준이는 현재 0에 있고, 사람들이 놓은 책도 전부 0에 있다.
    책들의 원래 위치가 주어질 때, 책을 모두 제자리에 놔둘 때 드는 최소 걸음수 계산
    책을 놔둔 후에는 다시 0으로 돌아올 필요는 없다.
    첫줄에 책 개수 N과 한 번에 들 수 있는 책 개수 M이 주어진다.
    둘째 줄에는 책의 위치. 책의 위치는 0이 아니다.
- 상상 코딩
    마지막에 가장 멀리가야 돌아오지 않아도 되는 이득을 가장 크게 가져갈 수 있다.
    음수와 양수중 가장 멀리 있는 곳을 마지막에 가야한다.
    한 번에 들 수 있는 책 개수 M
    음수리스트와 양수리스트를 M개씩 자른다. 각 M개 중에서 가장 큰수들을 모두 2배씩 해서 더하고, 가장 큰수만 마지막에 빼주면 된다. (다시 안돌아가니까)
    여기서 중요한 점은 각 거리의 리스트를 역순으로 정렬해서, 먼것 부터 M 개씩 잡아야 한다.
    그렇게 해야 먼거리의 책들부터 채워 넣어, 전체 이동 거리를 최소화 할 수 있기 때문입니다.
- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    3.5
- 문제 분석

    - 알고리즘 유형 분석

    - 시간복잡도 분석
        books를 반복하는 부분은 O(N) 두개로 나누어 정렬하지만, 정렬 원소의 개수는 총 N 개이므로 정렬 부분이 O(NlogN)
        슬라이싱하는 부분 역시 O(N) 이므로 전체 시간복잡도는 O(NlogN)입니다.

    - 리팩토링 방향성
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
books = map(int,input().split())
pos_li = [];neg_li = []
most_far=0
result=0
for b in books:
    if b>0:
        pos_li.append(b)
    elif b<0:
        neg_li.append(-b)
    most_far=max(most_far,abs(b))
pos_li.sort(reverse=True)
neg_li.sort(reverse=True)
result+=sum(pos_li[::M])*2
result+=sum(neg_li[::M])*2
print(result - most_far)