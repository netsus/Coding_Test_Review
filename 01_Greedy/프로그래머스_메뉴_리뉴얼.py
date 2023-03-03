"""
날짜 <2023/03/03 (금)>
- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/72411
- 문제 요약
    orders에서 사람들이 고른 메뉴들이 있습니다. course에 코스 요리로 만들 메뉴 개수가 있는데, 메뉴 개수별로 사람들이 동시에 가장 많이 먹은 메뉴들을 코스요리로 묶어 사전순으로 출력하는 프로그램.

    orders 배열의 크기는 2 이상 20 이하입니다.
    orders 배열의 각 원소는 크기가 2 이상 10 이하인 문자열입니다.
    각 문자열은 알파벳 대문자로만 이루어져 있습니다.
    각 문자열에는 같은 알파벳이 중복해서 들어있지 않습니다.

    course 배열의 크기는 1 이상 10 이하입니다.
    course 배열의 각 원소는 2 이상 10 이하인 자연수가 오름차순으로 정렬되어 있습니다.
    
    최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함

    orders	course	result
    ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	[2,3,4]	["AC", "ACDE", "BCFG", "CDE"]

- 상상 코딩
    모든 알파벳 26, orders는 최대 20, course는 최대 10, course의 원소는 2이상 10이하 자연수
    가능한 모든 조합별로, orders에 몇번 포함되는지 모두 연산?
    26C10만 해도 너무 크다 안된다.
    "사람들이 가장 많이 공통적으로 선택한 메뉴들"
    코스의 숫자에 대해 각 order별로 조합을 카운터에 넣는다. 카운터에서 most common을 모두 저장
    -> 정렬


- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    2.5

- 문제 분석

    - 알고리즘 유형 분석
        모든 주문(order)의 조합들의 갯수를 세고, 그중 최대 조합의 개수를 코스 요리로 만들기 때문에 브루트포스입니다.
        조합을 사용해서 풉니다.

    - 시간복잡도 분석
        모든 코스별로, 모든 주문에 대해서, 모든 조합을 찾습니다.
        코스는 최대 10개, 코스 원소의 최대는 10.
        orders 배열크기는 최대 20, order 최대 문자열 길이는 10
        즉 최악의 경우, 10개 메뉴중 5개 선택 -> 10C5 = 262
        그리고 이런게 최대 20 -> 20 x 262 = 5240 번
        코스는 최대 10개 -> 10 * 5240 = 52,400 번
        즉, 브루트포스로해도 넉넉하다.

    - 리팩토링 방향성
        카운터 += 1이 아니라, 조합자체를 카운터에 바로 넣어 풀이해도 괜찮겠다.
        (다른 사람 풀이)를 보면 그렇게 풀었다.
    
"""

orders,	course = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]
# answer ["AC", "ACDE", "BCFG", "CDE"]
orders, course = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]
# answer ["ACD", "AD", "ADE", "CD", "XYZ"]
orders, course = ["XYZ", "XWY", "WXA"],[2,3,4]
# answer ["WX", "XY"]
from collections import Counter
from itertools import combinations
def solution(orders, course):
    answer=[]
    for c in course:
        course_cnter = Counter()
        for order in orders:
            for comb in combinations(sorted(order),c):
                comb_str = "".join(comb)
                course_cnter[comb_str] += 1
        if course_cnter:
            most_com = course_cnter.most_common()
            max_vals = [v for v,cnt in most_com if cnt>1 and cnt==most_com[0][1]]
            answer.extend(max_vals)
    answer.sort()
    return answer

solution(orders, course)