"""
날짜 <2023/04/27 (목)>
- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/118667
- 문제 요약

- 상상 코딩
    BFS를 이용해서 q1, q2에서 pop하여 전체의 절반 큐를 만드는 횟수 확인

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    3.5
- 문제 분석

    - 알고리즘 유형 분석

    - 시간복잡도 분석

    - 리팩토링 방향성
    
"""
from collections import deque

def solution(queue1, queue2):
    q1,q2 = deque(queue1), deque(queue2)
    s1,s2 = sum(q1), sum(q2)
    cnt = 0
    for _ in range(300_000):
        if s1==s2:
            return cnt
        elif s1 > s2:
            e = q1.popleft()
            q2.append(e)
            s1 -= e
            s2 += e
        else:
            e = q2.popleft()
            q1.append(e)
            s1 += e
            s2 -= e
        cnt += 1
    return -1

q1,q2 = [3, 2, 7, 2], [4, 6, 5, 1] #2
print(solution(q1,q2))
q1,q2 = [1, 2, 1, 2], [1, 10, 1, 2] #7
print(solution(q1,q2))
q1,q2 = [1, 1], [1, 5] #-1
print(solution(q1,q2))



