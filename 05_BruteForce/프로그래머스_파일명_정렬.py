"""
날짜 <2023/03/23 (목)>
- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/17686?language=python3
- 문제 요약
    - 파일명은 우선 **HEAD 부분을 기준으로 사전 순으로 정렬 (대소문자 구분X)**
    - **NUMBER의 숫자 순으로 정렬**한다. 9 < 10 < 0011 < 012 < 13 < 014 순으로 정렬 (**숫자 앞의 0은 무시**되며, 012와 12는 정렬 시에 같은 같은 값)
    - **두 파일의 HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지**

- 상상 코딩
    - head와 number를 나누기
    - foo010bar020.txt 이런 경우, head를 foo로 number를 010으로 나눠야 한다 어떻게?
        - HEAD는 숫자가 아닌 문자(최소 1글자 이상)
        - 정규식을 사용하여 search로 처음 나오는 숫자가 아닌 문자열 덩어리와, 숫자 덩어리를 찾는다
    - 헤드 lower 처리해서 사전순 정렬, 넘버 맨앞 0들 모두 지워서 정렬
        - 넘버 맨 앞 0들만 어떻게 지울까?
        - 문자열 숫자에 대해 int 처리해주면 된다. ex) int(”0010”) → 10
    - 맨 마지막에 입력으로들어온 순서를 기억하여 정렬 → head, number, 들어온 순서로 정렬된다.
    - 정렬된 인덱스를 바탕으로 files 출력

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    2.5

- 문제 분석

    - 알고리즘 유형 분석
        정규식을 사용한 정렬 문제.

    - 시간복잡도 분석
        files 길이가 N -> 1000이하, 각 단어의 길이 평균이 M -> 100이하
        files를 반복하며 re.search 하는 부분이 O(N*M)
        pre_answer를 정렬하는 게 O(NlogN)
        둘 중 최대값이 시간복잡도이다.

    - 리팩토링 방향성
        re.search로 개별 검색하는게 아니라 match를 이용해서 한 번에 정렬
        시간복잡도는 O(NlogN*M)
    
"""
## 파일로 예제 입력 읽기
i1 = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
o1 = ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

i2 =  ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
o2 = ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

import re
def solution(files):
    pre_answer = []
    for i,file in enumerate(files):
        head = re.search('[^\d]+', file).group(0)
        number = re.search('[\d]+', file).group(0)
        pre_answer.append((head.lower(), int(number), i))
    pre_answer.sort()
    answer = [files[i] for _,_,i in pre_answer]
    return answer

# 리팩토링 풀이
import re
def solution(files):
    def sorter(file):
        head,number,tail = re.match(r'([^\d]+)([\d]+)(.*)',file).groups()
        return [head.lower(), int(number)]
    return sorted(files,key=sorter)


# print(solution(i1))
print(solution(i1)==o1)
# print(solution(i2))
print(solution(i2)==o2)
