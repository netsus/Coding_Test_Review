"""
날짜 <2023/03/03 (금)>
- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42885
- 문제 요약
    구명보트를 최대한 적게 사용하여 모든 사람을 구출
    사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return
    구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.
- 상상 코딩
    people을 내림차순 정렬하고, limit 이하일 때부터
    제일 무거운 사람(제일 왼쪽)과 제일 가벼운 사람(제일 오른쪽)의 합이 limit이하인지 조사하여 이하라면 둘을 태우고, 아니라면 무거운 사람 혼자 태우는 방식으로 보트를 띄우기
    한명 남았을 때는 혼자 보내기
- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    2
- 문제 분석
    처음에 list의 pop으로 풀었다가 문제는 맞았지만 시간초과가 났습니다.
    list.pop(0)의 시간복잡도가 O(N)이기 때문입니다.
    투포인터로 접근하니 시간초과 없이 풀 수 있었습니다.
    제한 조건에서 보트의 limit 보다 무거운 사람은 주어지지 않는 다는 조건도 봐야했습니다. 이를 따로 예외처리해줬는데, 그럴 필요가 없었기 때문입니다.
    - 그리디인 이유
        각 순간에 보트에 최적으로 사람을 태워야 보트를 최대한 적게 사용하기 때문
    - 시간복잡도 분석
        정렬은 O(NlogN)이고,
        while문 내부에서 각 분기문의 시간복잡도는 상수 시간 O(1)
        한 번에 1칸 혹은 2칸 움직이므로, while 문은 O(N)으로 볼 수 있습니다.
        즉, 정렬의 시간복잡도가 제일 커서 전체 시간복잡도는 O(NlogN)
    - 리팩토링 방향성
        elif 부분을 else로 처리해줘도 됩니다.


"""
## 파일로 예제 입력 읽기
# import sys
# sys.stdin = open("input.txt",'r')
##
# test1
people1,limit1=[70, 50, 80, 50],100 # return 3
# test2
people2,limit2=[70, 80, 50],100 # return 3

def solution(people, limit):
    answer=0
    people.sort(reverse=True)
    start,end=0,len(people)-1
    while start <= end:
        if people[start]+people[end] > limit:
            start+=1
            answer+=1
        elif people[start]+people[end] <= limit:
            start+=1;end-=1
            answer+=1
    return answer

print(solution(people1,limit1))
print(solution(people2,limit2))

