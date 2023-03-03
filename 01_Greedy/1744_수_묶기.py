"""
날짜 <2023/03/03 (금)>
- 체감 난이도: 3
- 문제 링크: https://www.acmicpc.net/problem/1744
- 문제 요약
    수열이 주어졌을 때, 수열의 합을 구한다.
    다만, 수열 중 위치 상관없이 두 수를 묶을 수 있는데, 그 묶은 수는 서로 곱한 후 하나의 숫자로 취급한다.
    수열의 각 수를 적절히 묶었을 때, 그 합이 될 수 있는 최대값을 구하시오.
    첫째 줄에 수열의 크기 N이 주어진다. N은 50보다 작은 자연수
    수열의 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수
    ex) {0, 1, 2, 4, 3, 5} ⇒ 0 + 1 + (2*3) + (4*5) = 27
    ex) {-1, 0, 1} ⇒ (-1*0) + 1 = 1
- 상상 코딩
    음수 개수가 짝수개 -> 0이 있거나 없거나 0을 묶지 않는다.
    음수 개수가 홀수개 -> 음수중 가장 큰수를 0과 묶는다.
        0이 없다면 -> 묶지 않는다.
    양수 개수가 짝수개 -> 큰수부터 2개씩 묶는다.
    양수 개수가 홀수개 -> 큰수부터 2개씩 묶고, 양수중 가장 작은 수 1개는 묶지 않는다.

    정렬해주고, 음수리스트 따로, 양수 리스트 따로 만들기, 0있는지 변수로 체크
    음수 리스트 길이, 양수 리스트 길이 체크 -> 짝수 홀수인지
    조건문으로 짝수냐 홀수냐에 따라 알고리즘 작성
- 문제 분석
    - 그리디(선택의 순간 최적의 선택)인 이유
        양수와 음수를 나눠, 두 수를 묶는 선택을 값이 최대가 되도록 만드는 알고리즘이기 때문
    - 시간복잡도 분석
        정렬부분에서 가장 오래걸려 O(NlogN)
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##

## 제출 코드
from typing import List
def grouping(nums:List) -> List:
    grp_list=[]
    for i in range(0,len(nums),2):
        grp_list.append(nums[i]*nums[i+1])
    return grp_list

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort() #nlogn

minus_nums=[]
plus_nums=[]
one_list=[]
zero=False

for n in nums: # n
    if n<0:
        minus_nums.append(-n)
    elif n==1:
        one_list.append(n)
    elif n>0:
        plus_nums.append(n)
    else:
        zero=True
        
minus_len = len(minus_nums)
plus_len = len(plus_nums)

result=0
if minus_len%2==0: # N
    grp_nums = grouping(minus_nums)
else:
    grp_nums = grouping(minus_nums[:-1])
    if not zero:
        grp_nums.append(-minus_nums[-1])
result += sum(grp_nums) #n
if plus_len%2==0: #n
    grp_nums = grouping(plus_nums)
else:
    grp_nums = grouping(plus_nums[1:])
    grp_nums.append(plus_nums[0])
result += sum(grp_nums) #n
print(result+sum(one_list) if one_list else result) 