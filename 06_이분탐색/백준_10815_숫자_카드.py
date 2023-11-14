"""
날짜 <2023/11/14 (화)>
- 문제 링크: https://www.acmicpc.net/problem/10815
- 문제 요약
    카드들이 주어진다. (개수와 카드 번호)
    두번쨰로 또 카드들이 주어지는데, 처음에 주어진 카드에 속하면 1 아니면 0을 출력하시오.

- 상상 코딩
    처음 카드를 정렬해서 저장하고, 두번째 카드들이 주어질때 이분탐색으로 찾아서 있으면 1 없으면 0을 출력.

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    2
- 문제 분석

    - 알고리즘 유형 분석

    - 시간복잡도 분석
        n과 m에 대해서, 처음에 정렬은 O(nlogn)이 걸리고 m 입력은 O(m)이 걸린다.
        m개의 카드를 반복하며 n_cards에 대해 binary search를 하는데 이는 O(mlogn)이 걸린다.
        즉, 최종 시간복잡도는 O(nlogn) + O(mlogn) 이 되고,
        n과 m중에 더 큰 값이 최종 시간복잡도에 영향을 미친다.

    - 리팩토링 방향성
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
import sys
input = sys.stdin.readline
N = int(input())
n_cards = sorted(map(int,input().split()))
M = int(input())
m_cards = [*map(int,input().split())]

def binary_search(t,cards):
    s,e = 0, len(cards)-1
    while s<=e:
        mid = (s+e)//2
        if t == cards[mid]:
            return 1
        elif t < cards[mid]:
            e = mid-1
        else:
            s = mid+1
    return 0
result = [binary_search(card,n_cards) for card in m_cards]
print(*result)

    
        

