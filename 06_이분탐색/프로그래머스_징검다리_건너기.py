"""
날짜 <2023/04/06 (목)>
- 문제 링크: 
- 문제 요약

- 상상 코딩
    stones에서 최소값과 최대값 사이를 이분탐색하며 
    그 숫자보다 크면 뺴고, 아니면 0으로만들기
    연속된 0의 개수 찾기


- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    3

- 문제 분석

    - 알고리즘 유형 분석
        이분 탐색을 이용한 문제입니다.
    - 시간복잡도 분석
        stones의 개수를 N이라고 할 때, O(NlogN)입니다.

    - 리팩토링 방향성
        for문으로 stones를 도는 O(N) 부분에서 중간에 조건이 만족되면 break를 하여 시간복잡도를 줄일 수 있습니다.
        또한, 기존에 continuos_zero를 사용하여 max를 갱신하는 부분이 있으면 시간초과가 되는데 이부분만 제외하니 시간복잡도가 내려갑니다.
        즉, O(N)부분에서 연산을 최소화하면 시간복잡도가 매우 감소하는 것을 볼 수 있습니다.
        또한 코끼리 연산자를 활용해 코드길이를 줄일 수 있습니다. 하지만 시간복잡도는 약간 증가함을 알 수 있습니다.
    
"""
s,k = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 2  # result: 3


def solution(stones, k):
    s,e=min(stones),max(stones)
    while s<=e:
        m = (s+e)//2
        continuous_zero=cnt=0
        for w in stones:
            if w<=m:
                cnt+=1
            else:
                cnt=0
            continuous_zero=max(continuous_zero,cnt)
            if continuous_zero>=k:
                break
        if continuous_zero >= k:
            answer = m
            e = m-1
        else:
            s = m+1
    return answer

def solution(stones, k):
    s,e=min(stones),max(stones)
    while s<=e:
        m, cnt = (s+e)//2, 0
        for w in stones:
            if w<=m:
                cnt+=1
            else:
                cnt=0
            if cnt>=k:
                break
        if cnt >= k:
            answer = m
            e = m-1
        else:
            s = m+1
    return answer


def solution(stones, k):
    s,e=min(stones),max(stones)
    while s<=e:
        m, cnt = (s+e)//2, 0
        for w in stones:
            (cnt:=cnt+1 if w<=m else 0)
            if cnt>=k:
                break
        if cnt >= k:
            answer = m
            e = m-1
        else:
            s = m+1
    return answer


print(solution(s,k))

