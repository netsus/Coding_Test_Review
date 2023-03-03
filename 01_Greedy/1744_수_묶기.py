## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##

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