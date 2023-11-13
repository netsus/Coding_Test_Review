"""
날짜 <2023/11/13 (월)>
- 문제 링크: https://www.acmicpc.net/problem/2776
- 문제 요약
    수첩1의 숫자가 주어지고, 수첩2의 숫자에 대해 수첩1에 있으면 1, 없으면 0을 출력하는 프로그램

- 상상 코딩
    정수는 백만개까지 주어진다. 일일이 탐색하기 어렵다.
    수첩1을 정렬한 뒤에, 이분탐색해서 있는지 없는지 출력해보자.

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    2.5
- 문제 분석

    - 알고리즘 유형 분석

    - 시간복잡도 분석
        note1의 길이가 n, note2의 길이가M 일때, 이진탐색의 시간복잡도는 O(logn) 총 M번 수행하기 때문에 O(Mlogn)
        하지만 처음에 note1을 정렬할 때 O(nlogn)이 사용되었다.
        즉 O(nlogn)과 O(Mlogn) 중 큰게 시간복잡도.


    - 리팩토링 방향성
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')

##
import sys
input = sys.stdin.readline

def bs(num, arr):
    s,e = 0, len(arr)-1
    while s <= e:
        mid = (s+e)//2
        if arr[mid]==num:
            return 1
        elif arr[mid] < num:
            s = mid+1
        else:
            e = mid-1
    return 0
        
T = int(input())
for _ in range(T):
    N = int(input())
    note1 = sorted(map(int,input().split()))
    M = int(input())
    note2 = map(int,input().split())
    for num in note2:
        print(bs(num,note1))
            



